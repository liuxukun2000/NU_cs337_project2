from typing import List
from lxml import etree
from scrapper.base import BaseSpider
import requests
from bs4 import BeautifulSoup

class BonappetitSpider(BaseSpider):
    def __init__(self, title: str, ingredients: List[str], steps: List[str]):
        self.title = title.strip(" \n")
        self.ingredients = [item for item in ingredients if item]
        self.steps = [item for item in steps if item]

    def __str__(self):
        return f"{self.title}\n\nIngredients:\n" + "\n".join(self.ingredients) + "\n\nSteps:\n" + "\n".join(self.steps)

    @staticmethod
    def name() -> str:
        return "bonappetit"

    @staticmethod
    def get(url: str) -> "BonappetitSpider":
        response = requests.get(url).text
        tree = etree.HTML(response)
        title = tree.xpath("/html/body/div[1]/div/main/article/div[1]/header/div[1]/div[1]/div/h1")[0].text
        _ingredients = tree.xpath("/html/body/div[1]/div/main/article/div[2]/div[1]/div[1]/div/div[4]/div")[0]
        ingredients = []
        for id, i in enumerate(_ingredients):
            text = i.text
            if text is None:
                text = ""
            if id % 2 == 0:
                ingredients.append(text.strip(" \n"))
            else:
                ingredients[-1] += " " + text.strip(" \n")
        _steps = tree.xpath("/html/body/div[1]/div/main/article/div[2]/div[1]/div[1]/div/div[5]/ol/li")[0]
        steps = []
        for id, i in enumerate(_steps):
            text = i.text
            if text is None:
                text = ""
            if id % 2 == 0:
                steps.append(text.strip(" \n"))
            else:
                steps[-1] += " " + text.strip(" \n")

        return BonappetitSpider(title, ingredients, steps)

if __name__ == "__main__":
    x = BonappetitSpider.get("https://www.bonappetit.com/recipe/sheet-pan-turkey-and-gravy")
    print(x)


