from typing import List

from base import BaseSpider
import requests
from bs4 import BeautifulSoup
from extracter_list import TOOLS
from extracter_list import PRIMARY_COOKING_METHODS
from extracter_list import SECONDARY_COOKING_METHODS
import string


class Tool_Method_Info_Spider(BaseSpider):
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
    def info_from_steps(url:str):
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        steps_ol = soup.select_one("#mntl-sc-block_2-0")
        if steps_ol:
            step_elements = steps_ol.find_all('li')
            steps = []

            for step in step_elements:
                p_tag = step.find('p')
                if p_tag:
                    steps.append(p_tag.text.strip())
        
        return steps
    
    @staticmethod
    def get_tools(url:str):
        steps = Tool_Method_Info_Spider.info_from_steps(url)
        tool_in_each_step={}
        for i in range(len(steps)):
            #tool_list=[]
            normalized_sentence = steps[i].lower().translate(str.maketrans('', '', string.punctuation))

            # Normalize the search_list items and check if they are in the normalized sentence
            tool_list= [item for item in TOOLS if item.lower() in normalized_sentence]
            tool_in_each_step["step "+str(i+1)]=tool_list
        
        return tool_in_each_step

    @staticmethod
    def get_methods(url:str):
        steps = Tool_Method_Info_Spider.info_from_steps(url)
        primary_method_in_each_step={}
        secondary_method_in_each_step={}
        for i in range(len(steps)):
            normalized_sentence = steps[i].lower().translate(str.maketrans('', '', string.punctuation))

            primary_method_list= [item for item in PRIMARY_COOKING_METHODS if item.lower() in normalized_sentence]
            secondary_method_list= [item for item in SECONDARY_COOKING_METHODS if item.lower() in normalized_sentence]
            primary_method_in_each_step["step "+str(i+1)]=primary_method_list
            secondary_method_in_each_step["step "+str(i+1)]=secondary_method_list
        
        return (primary_method_in_each_step,secondary_method_in_each_step)
        


if __name__ == "__main__":
    #x = AllrecipesSpider.get("https://www.allrecipes.com/recipe/234860/butternut-squash-lasagna/")
    #x = AllrecipesSpider.get('https://www.allrecipes.com/recipe/19354/cheese-lasagna/')
    #print(x)
    website_url='https://www.allrecipes.com/recipe/19354/cheese-lasagna/'
    tools=Tool_Method_Info_Spider.get_tools(website_url)
    print("printing_tools: \n",tools)

    primary_method, secondary_method=Tool_Method_Info_Spider.get_methods(website_url)
    print("\n primary_method: \n", primary_method)
    print("\n secondary_method: \n", secondary_method)


