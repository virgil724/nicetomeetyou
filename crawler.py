import asyncio
import json
import requests
import re
import aiohttp
from bs4 import BeautifulSoup
from pydantic import BaseModel, HttpUrl, field_serializer
from datetime import datetime


class NewsPhoto(BaseModel):
    imgUrl: HttpUrl
    comment: str

    @field_serializer("imgUrl")
    def serialize_imgUrl(self, imgUrl: HttpUrl, _info):
        return str(imgUrl)


class News(BaseModel):
    title: str
    detail_url: HttpUrl
    content: str | None = None
    full_title: str | None = None
    update_time: datetime | None = None
    paper: str | None = None
    author: str | None = None
    news_photo: NewsPhoto | None = None


class PostBody(BaseModel):
    title: str
    url: str
    content: str
    update_time: str
    paper: str
    author: str
    news_photo: list[NewsPhoto]


def get_news_block(soup: BeautifulSoup) -> list[News]:
    news_blocks = soup.select(
        "#focus > div.focus_body > section > div.splide__track > ul"
    )[0].find_all("li")

    news: list[News] = []
    for block in news_blocks:
        title = block.find("h1").text
        link = block.a.get("href").split("?")[0]
        news.append(News(title=title, detail_url=link))
    return news


def grab_news_detail(news: News) -> str:
    resp = requests.get(news.detail_url)
    soup = BeautifulSoup(resp.text, "html.parser")

    detail_title = soup.select("#story_body_content > h1")[0].text
    author = soup.select("#shareBar > div.shareBar__info > div")[0].text
    datetime, paper, author = parse_news_info(author)
    img_detail = soup.select_one("#story_body_content").figure
    img_url = img_detail.img.get("src")
    img_comment = img_detail.figcaption.text
    content = soup.select_one("#story_body_content").find_all("p")
    content = "".join([str(para) for para in content[1:]])
    updated_news = News(
        **news.model_dump(exclude_unset=True),
        full_title=detail_title,
        author=author,
        update_time=datetime,  # 這裡會觸發驗證器
        paper=paper,
        news_photo=NewsPhoto(imgUrl=img_url, comment=img_comment),
        content=content,
    )

    return updated_news


async def async_grab_news_detail(session: aiohttp.ClientSession, news: News) -> News:
    async with session.get(str(news.detail_url)) as resp:
        html_doc = await resp.text()
    soup = BeautifulSoup(html_doc, "html.parser")

    detail_title = soup.select("#story_body_content > h1")[0].text
    author_info = soup.select("#shareBar > div.shareBar__info > div")[0].text
    datetime_str, paper, author = parse_news_info(author_info)
    img_detail = soup.select_one("#story_body_content").figure
    img_url = img_detail.img.get("src")
    img_comment = img_detail.figcaption.text
    content = soup.select_one("#story_body_content").find_all("p")
    content = "".join([str(para) for para in content[1:]])

    return News(
        **news.model_dump(exclude_unset=True),
        full_title=detail_title,
        author=author,
        update_time=datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        if datetime_str
        else None,
        paper=paper,
        news_photo=NewsPhoto(imgUrl=img_url, comment=img_comment),
        content=content,
    )


async def update_django(session: aiohttp.ClientSession, news: News) -> int:
    body = PostBody(
        title=news.full_title,
        url=str(news.detail_url),
        update_time=news.update_time.isoformat(),
        news_photo=[news.news_photo.model_dump()],
        **news.model_dump(exclude=["title", "update_time", "news_photo"]),
    )


    async with session.post(
        "http://localhost:8000/api/nba-edit/", json=body.model_dump()
    ) as resp:
        return await resp.status


def parse_news_info(text):
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2})(\S+) / (.+)"
    match = re.match(pattern, text)

    if match:
        datetime, paper, author = match.groups()
        return datetime, paper, author
    else:
        return None


async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://tw-nba.udn.com/nba/index/"
        resp = await session.get(url)
        news_blocks = get_news_block(BeautifulSoup(await resp.text()))
        tasks = [async_grab_news_detail(session, item) for item in news_blocks]
        news = await asyncio.gather(*tasks)

        tasks = [update_django(session, item) for item in news]
        await asyncio.gather(*tasks)
    # Here you can process the 'news' list as needed
    # for item in news:
    #     print(f"Title: {item.title}")
    #     print(f"URL: {item.detail_url}")
    #     print(f"Update time: {item.update_time}")
    #     print("---")


if __name__ == "__main__":
    
    asyncio.run(main())

