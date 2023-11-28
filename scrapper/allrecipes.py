from typing import List

from base import BaseSpider
import requests
from bs4 import BeautifulSoup

class AllrecipesSpider(BaseSpider):
    def __init__(self, title: str, ingredients: List[str], steps: List[str], servings: int = -1):
        self.title = title.strip(" \n")
        self.ingredients = [item for item in ingredients if item]
        self.steps = [item for item in steps if item]
        self.servings = servings

    def __str__(self):
        return f"**{self.title}**\n\n**Ingredients:**\n\n" + "\n\n".join(self.ingredients) + "\n\n**Steps:**\n\n" + "\n\n".join(self.steps) +\
    f"\n\nServings\n\n{self.servings}"

    @staticmethod
    def name() -> str:
        return "allrecipes"

    @staticmethod
    def get(url: str) -> "AllrecipesSpider":
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        title = soup.select_one("#article-heading_1-0").text
        ingredients_list = soup.select("#mntl-structured-ingredients_1-0 > ul")
        ingredients = []
        for item in ingredients_list:
            ingredients.extend([ingredient.text.strip(" \n") for ingredient in item.children if ingredient != "\n"])
        steps = soup.select_one("#mntl-sc-block_2-0")
        steps = [step.text.strip(" \n") for step in steps.children if step != "\n"]
        servings = soup.select_one("#recipe-details_1-0 > div.mntl-recipe-details__content > div:nth-child(4) > div.mntl-recipe-details__value").text
        return AllrecipesSpider(title, ingredients, steps, int(servings))

if __name__ == "__main__":
    x = AllrecipesSpider.get("https://www.allrecipes.com/recipe/230904/hearty-barley-turkey-soup/")
    print(x)


