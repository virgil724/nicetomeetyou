import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, HttpUrl
from typing import Optional


class News(BaseModel):
    title: str
    detail_url: HttpUrl
    content: str | None = None


def get_total_pages(soup: BeautifulSoup) -> int:
    pages = int(soup.select("#news_list > div.pagelink > span")[0].text.split()[1])
    return pages


def get_news_block(soup: BeautifulSoup) -> list[News]:
    news_blocks = soup.select("#news_list_body")[0].find_all("dt")

    news: list[News] = []
    for block in news_blocks:
        title = block.find("h3").text
        link = block.a.get("href")

        news.append(News(title=title, detail_url=link))
    return news


def grab_news_detail(link: HttpUrl) -> str:
    
    return "news Content"


resp = requests.get("https://tw-nba.udn.com/nba/news/")
html_doc = resp.text
soup = BeautifulSoup(html_doc, "html.parser")
