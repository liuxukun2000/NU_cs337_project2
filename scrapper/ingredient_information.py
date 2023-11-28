from typing import List

from base import BaseSpider
import requests
from bs4 import BeautifulSoup


class Ingredient_Info_Spider(BaseSpider):
    def __init__(self, title: str, ingredients: List[str], steps: List[str]):
        self.title = title.strip(" \n")
        self.ingredients = [item for item in ingredients if item]
        self.steps = [item for item in steps if item]

    def __str__(self):
        return f"{self.title}\n\nIngredients:\n" + "\n".join(self.ingredients) + "\n\nSteps:\n" + "\n".join(self.steps)

    @staticmethod
    def name() -> str:
        return "allrecipes"
    
    @staticmethod
    def ingredient_details(url:str):
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        

        ingredient_elements = soup.select(".mntl-structured-ingredients__list-item")

        
        formatted_ingredients_dict = {}
        formatted_ingredients_list = []


        
        #print("hereeeeeee")
        for ingredient in ingredient_elements:
            
            quantity = ingredient.find('span', {'data-ingredient-quantity': 'true'}).text.strip()
            unit = ingredient.find('span', {'data-ingredient-unit': 'true'}).text.strip()
            name = ingredient.find('span', {'data-ingredient-name': 'true'}).text.strip()
            # print("quantity ",quantity)
            # print("unit ",unit)
            #print("name ",name)
            ingredient_information = name.split(',',1)
            name=ingredient_information[0]
            descriptor = ingredient_information[1] if len(ingredient_information) > 1 else ''
            
            formatted_ingredients_dict[name]={"unit":unit, "quantity":quantity,"descriptor":descriptor}
            formatted_ingredients_list.append([name,unit, quantity,descriptor])
        
        
        # for item in formatted_ingredients:
        #     print(item)
        #print(formatted_ingredients_dict)
        return formatted_ingredients_dict

    # @staticmethod
    # def get(url: str) -> "AllrecipesSpider":
    #     response = requests.get(url).text
    #     soup = BeautifulSoup(response, "html.parser")
    #     title = soup.select_one("#article-heading_1-0").text
    #     ingredients = soup.select_one("#mntl-structured-ingredients_1-0 > ul")
    #     #print("1111ingredients",ingredients)
    #     ingredients = [ingredient.text.strip(" \n") for ingredient in ingredients.children if ingredient != "\n"]
    #     steps = soup.select_one("#mntl-sc-block_2-0")
    #     # print("STEPSSSS",steps)
    #     # steps = [step.text.strip(" \n") for step in steps.children if step != "\n"]
    #     #steps=["STEEPSSS"]
    #     steps_ol = soup.select_one("#mntl-sc-block_2-0")

        
    #     if steps_ol:
    #         step_elements = steps_ol.find_all('li')
    #         steps = []

    #         for step in step_elements:
    #             p_tag = step.find('p')
    #             if p_tag:
    #                 steps.append(p_tag.text.strip() + ("\n"))


    #     return AllrecipesSpider(title, ingredients, steps)

if __name__ == "__main__":
    #x = AllrecipesSpider.get("https://www.allrecipes.com/recipe/234860/butternut-squash-lasagna/")
    #x = AllrecipesSpider.get('https://www.allrecipes.com/recipe/19354/cheese-lasagna/')
    #print(x)
    ingredients=Ingredient_Info_Spider.ingredient_details("https://www.allrecipes.com/recipe/234860/butternut-squash-lasagna/")
    print(ingredients)


