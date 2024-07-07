import requests
import re
from bs4 import BeautifulSoup
from pydantic import BaseModel, HttpUrl
from datetime import datetime


class NewsPhoto(BaseModel):
    imgUrl: HttpUrl
    comment: str


class News(BaseModel):
    title: str
    detail_url: HttpUrl
    content: str | None = None
    full_title: str | None = None
    update_time: datetime | None = None
    paper: str | None = None
    author: str | None = None
    news_photo: NewsPhoto | None = None


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


def parse_news_info(text):
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2})(\S+) / (.+)"
    match = re.match(pattern, text)

    if match:
        datetime, paper, author = match.groups()
        return datetime, paper, author
    else:
        return None


resp = requests.get("https://tw-nba.udn.com/nba/index/")
html_doc = resp.text
soup = BeautifulSoup(html_doc, "html.parser")

news = get_news_block(soup)
news = [grab_news_detail(item) for item in get_news_block(soup)]
