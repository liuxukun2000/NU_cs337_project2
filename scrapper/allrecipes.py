from typing import List
import re
from utils.ingredient import RecipeIngredient
from utils.step import RecipeStep
from utils.utils import get_servings
from scrapper.base import BaseSpider
import requests
from bs4 import BeautifulSoup

class AllrecipesSpider(BaseSpider):
    def __init__(self, title: str, ingredients: List[str], steps: List[str], servings: int = -1):
        self.title = title.strip(" \n")
        self.ingredients = [RecipeIngredient.from_string(item) for item in ingredients if item]
        self.ingredients = [item for item in self.ingredients if item.name]
        tmp = 1
        self.steps = []
        for item in steps:
            if item:
                self.steps.append(RecipeStep.from_string(item, self.ingredients, tmp))
                tmp += 1
        self.servings = servings

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
        # remove substr like allrecipes/xxx\n from steps
        regex = re.compile(r"Allrecipes/.*")
        steps = [regex.sub("", step) for step in steps]
        return AllrecipesSpider(title, ingredients, steps, get_servings(servings))

if __name__ == "__main__":
    x = AllrecipesSpider.get("https://www.allrecipes.com/recipe/230904/hearty-barley-turkey-soup/")
    print(x)


