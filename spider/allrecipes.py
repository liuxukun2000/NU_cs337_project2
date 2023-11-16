from typing import List

from spider.base import BaseSpider
import requests
from bs4 import BeautifulSoup

class AllrecipesSpider(BaseSpider):
    def __init__(self, title: str, ingredients: List[str], steps: List[str]):
        self.title = title
        self.ingredients = [item for item in ingredients if item]
        self.steps = [item for item in steps if item]

    def __str__(self):
        return f"{self.title}\n\nIngredients:\n" + "\n".join(self.ingredients) + "\n\nSteps:\n" + "\n".join(self.steps)

    @staticmethod
    def get(url: str) -> "AllrecipesSpider":
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        title = soup.select_one("#article-heading_1-0").text
        ingredients = soup.select_one("#mntl-structured-ingredients_1-0 > ul")
        ingredients = [ingredient.text.strip(" \n") for ingredient in ingredients.children if ingredient != "\n"]
        steps = soup.select_one("#mntl-sc-block_2-0")
        steps = [step.text.strip(" \n") for step in steps.children if step != "\n"]
        return AllrecipesSpider(title, ingredients, steps)

if __name__ == "__main__":
    x = AllrecipesSpider.get("https://www.allrecipes.com/recipe/234860/butternut-squash-lasagna/")
    print(x)


