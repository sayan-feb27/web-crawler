import requests
from bs4 import BeautifulSoup


class Crawler:

    def __init__(self, url: str):
        self.url = url

    def crawl(self) -> list[str]:
        html_doc = self.__get_html()
        soup = BeautifulSoup(html_doc, "html.parser")
        return [link.get("href") for link in soup.find_all('a') if link.get("href")]

    def __get_html(self) -> str:
        with requests.Session() as session:
            response = session.get(self.url)
            return response.text
