import re
import random

from handler.base import BaseHandler
from utils.ontologies import *


class Cuisines(BaseHandler):
    def __init__(self):
        self.number = -1

    @staticmethod
    def type() -> str:
        return "cuisines"
    
    def transform_to_Indian(self, inp: str, cfg) -> str:
        inp = inp.lower()
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        ori_recipe = recipe_handler[-1].ori_recipe
        recipe = recipe_handler[-1].recipe
        
        pattern = r'\b(transform|make)\b.+?indian'
        if bool(re.search(pattern, inp)):
            for i in range(len(recipe.ingredients)):
                ingredient = recipe.ingredients[i]
                for type in ingredient.types:
                    if type == "meat_and_poultry" or type == "seafood":
                        # transform
                        found = False
                        for item in INGREDIENTS["south_asian_protein"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            new = random.choice(INGREDIENTS["south_asian_protein"])
                            recipe.transform(recipe.ingredients[i].name, new)
                            recipe.ingredients[i].name = new
                            recipe.ingredients[i].types = ["south_asian_protein"]
                    elif type == "milk_and_dairy" or type == "cheese":
                        new = random.choice(INGREDIENTS["south_asian_dairy"])
                        recipe.transform(recipe.ingredients[i].name, new)
                        recipe.ingredients[i].name = new
                        recipe.ingredients[i].types = ["south_asian_dairy"]
                    elif type == "herbs_and_spices":
                        found = False
                        for item in INGREDIENTS["south_asian_spices"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            new = random.choice(INGREDIENTS["south_asian_spices"])
                            recipe.transform(recipe.ingredients[i].name, new)
                            recipe.ingredients[i].name = new
                            recipe.ingredients[i].types = ["south_asian_spices"]
                    elif type == "sauces":
                        found = False
                        for item in INGREDIENTS["south_asian_sauces"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            new = random.choice(INGREDIENTS["south_asian_sauces"])
                            recipe.transform(recipe.ingredients[i].name, new)
                            recipe.ingredients[i].name = new
                            recipe.ingredients[i].types = ["south_asian_sauces"]
                    elif type == "vegetables":
                        found = False
                        for item in INGREDIENTS["south_asian_vegetable"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            new = random.choice(INGREDIENTS["south_asian_vegetable"])
                            recipe.transform(recipe.ingredients[i].name, new)
                            recipe.ingredients[i].name = new
                            recipe.ingredients[i].types = ["south_asian_vegetable"]
                    elif type == "carbs":
                        found = False
                        for item in INGREDIENTS["south_asian_carb"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            new = random.choice(INGREDIENTS["south_asian_carb"])
                            recipe.transform(recipe.ingredients[i].name, new)
                            recipe.ingredients[i].name = new
                            recipe.ingredients[i].types = ["south_asian_carb"]
                            
            return f"I've made the recipe Indian for you. Here are the ingredients of the Indian version of **{recipe.title}:**\n\n* [x] " + "\n\n* [x] ".join(map(str, recipe.ingredients))
        else:
            return "Sorry, I can't understand."
        
    def transform_to_Chinese(self, inp: str, cfg) -> str:
        inp = inp.lower()
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        ori_recipe = recipe_handler[-1].ori_recipe
        recipe = recipe_handler[-1].recipe
        
        pattern = r'\b(transform|make)\b.+?chinese'
        if bool(re.search(pattern, inp)):
            for i in range(len(recipe.ingredients)):
                ingredient = recipe.ingredients[i]
                for type in ingredient.types:
                    if type == "herbs_and_spices":
                        found = False
                        for item in INGREDIENTS["chinese_spices"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            new = random.choice(INGREDIENTS["chinese_spices"])
                            recipe.transform(recipe.ingredients[i].name, new)
                            recipe.ingredients[i].name = new
                            recipe.ingredients[i].types = ["chinese_spices"]
                    elif type == "sauces":
                        found = False
                        for item in INGREDIENTS["chinese_sauce"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            new = random.choice(INGREDIENTS["chinese_sauce"])
                            recipe.transform(recipe.ingredients[i].name, new)
                            recipe.ingredients[i].name = new
                            recipe.ingredients[i].types = ["chinese_sauce"]
                    elif type == "vegetables":
                        found = False
                        for item in INGREDIENTS["chinese_vegetable"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            new = random.choice(INGREDIENTS["chinese_vegetable"])
                            recipe.transform(recipe.ingredients[i].name, new)
                            recipe.ingredients[i].name = new
                            recipe.ingredients[i].types = ["chinese_vegetable"]
                    elif type == "carbs":
                        found = False
                        for item in INGREDIENTS["chinese_carb"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            new = random.choice(INGREDIENTS["chinese_carb"])
                            recipe.transform(recipe.ingredients[i].name, new)
                            recipe.ingredients[i].name = new
                            recipe.ingredients[i].types = ["chinese_carb"]
                            
            return f"I've made the recipe Chinese for you. Here are the ingredients of the Indian version of **{recipe.title}:**\n\n* [x] " + "\n\n* [x] ".join(map(str, recipe.ingredients))
        else:
            return "Sorry, I can't understand."
        
        
    def match(self, inp: str, cfg) -> int:
        # handler = [handler for handler in cfg['handler'] if handler.type() == "get_ingredient"]
        if "Sorry" not in self.transform_to_Indian(inp, cfg):
            return 1
        elif "Sorry" not in self.transform_to_Chinese(inp, cfg):
            return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        cfg['handler'].append(self)
        
        ans = self.transform_to_Indian(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.transform_to_Chinese(inp, cfg)
        if "Sorry" not in ans:
            return ans
        
        return "Sorry, I can't understand."
    
       
