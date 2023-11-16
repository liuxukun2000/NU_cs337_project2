from typing import List
from lxml import etree
from spider.base import BaseSpider
import requests
from bs4 import BeautifulSoup

class DelishSpider(BaseSpider):
    def __init__(self, title: str, ingredients: List[str], steps: List[str]):
        self.title = title.strip(" \n")
        self.ingredients = [item for item in ingredients if item]
        self.steps = [item for item in steps if item]

    def __str__(self):
        return f"{self.title}\n\nIngredients:\n" + "\n".join(self.ingredients) + "\n\nSteps:\n" + "\n".join(self.steps)

    @staticmethod
    def name() -> str:
        return "delish"

    @staticmethod
    def get(url: str) -> "DelishSpider":
        response = requests.get(url).text
        tree = etree.HTML(response)
        title = tree.xpath("/html/body/div[1]/div[1]/main/header/div/div/h1")[0]
        title = ''.join(title.itertext()).strip()
        _ingredients = tree.xpath("/html/body/div[1]/div[1]/main/div[3]/div[1]/div[2]/div[3]/section/div[2]/div[1]/ul/li")
        ingredients = []
        for i in _ingredients:
            ingredients.append(''.join(i.itertext()).strip())
        # ingredients = [i.text.split(" \n") for i in ingredients if i.text]
        _steps = tree.xpath("/html/body/div[1]/div[1]/main/div[3]/div[1]/div[2]/div[3]/div/ul/li/ol/li")
        steps = []
        for i in _steps:
            steps.append(''.join(i.itertext()).strip().replace("css-13o7eu2{display:block;}", ""))
        return DelishSpider(title, ingredients, steps)

if __name__ == "__main__":
    x = DelishSpider.get("https://www.delish.com/holiday-recipes/thanksgiving/a29178578/how-to-dry-brine-turkey-recipe/")
    print(x)


