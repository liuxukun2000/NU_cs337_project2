import re
import random

from handler.base import BaseHandler
from utils.ontologies import *


class DietaryRestrictions(BaseHandler):
    def __init__(self):
        self.number = -1

    @staticmethod
    def type() -> str:
        return "dietary_restrictions"

    def ask_is_vegetarian_vegan(self, inp: str, cfg) -> str:
        inp = inp.lower()
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."

        pattern = r'\bis\b.*?vegetarian'
        vegetarian = True
        non_vegetarian = []
        if bool(re.search(pattern, inp)):
            recipe = recipe_handler[-1].recipe
            for ingredient in recipe.ingredients:
                for type in ingredient.types:
                    if type == "meat_and_poultry" or type == "seafood":
                        vegetarian = False
                        non_vegetarian.append(ingredient.name)
            if vegetarian:
                return "This recipe is vegetarian."
            else:
                return "This recipe is not vegetarian. It contains " + ", ".join(non_vegetarian)
        
        pattern = r'\bis\b.+?vegan'
        vegan = True
        non_vegan = []
        if bool(re.search(pattern, inp)):
            recipe = recipe_handler[-1].recipe
            for ingredient in recipe.ingredients:
                for type in ingredient.types:
                    if type == "meat_and_poultry" or type == "seafood" or type == "milk_and_dairy" or type == "eggs" or type == "cheese":
                        vegan = False
                        non_vegan.append(ingredient.name)
            if vegan:
                return "This recipe is vegan."
            else: 
                return "This recipe is not vegan. It contains " + ", ".join(non_vegan)
        else:
            return "Sorry, I can't understand."
    
    def ask_is_kosher(self, inp: str, cfg) -> str:
        inp = inp.lower()
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        
        pattern = r'\bis\b.+?kosher'
        kosher = True
        non_kosher = []
        ing_types = []
        if bool(re.search(pattern, inp)):
            recipe = recipe_handler[-1].recipe
            for ingredient in recipe.ingredients:
                for type in ingredient.types:
                    ing_types.append(type)
                    if type == "meat_and_poultry" or type == "seafood":
                        found = False
                        for item in INGREDIENTS["kosher_meat"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            kosher = False
                            non_kosher.append(ingredient.name)
                        
            if ("meat_and_poulty" in ing_types and "milk_and_dairy" in ing_types) or ("meat_and_poulty" in ing_types and "cheese" in ing_types):
                    kosher = False
                    return "This recipe is not Kosher. It contains both meat and dairy."
            if kosher:
                return "This recipe is Kosher."
            else:
                return "This recipe is not Kosher. It contains " + ", ".join(non_kosher)
            
        else:
            return "Sorry, I can't understand."
    
    def ask_is_pescatarian(self, inp: str, cfg) -> str:
        inp = inp.lower()
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        
        pattern = r'\bis\b.+?pescatarian'
        pescatarian = True
        non_pescatarian = []
        if bool(re.search(pattern, inp)):
            recipe = recipe_handler[-1].recipe
            for ingredient in recipe.ingredients:
                for type in ingredient.types:
                    if type == "meat_and_poultry":
                        pescatarian = False
                        non_pescatarian.append(ingredient.name)
            if pescatarian:
                return "This recipe is pescatarian."
            else:
                return "This recipe is not pescatarian. It contains " + ", ".join(non_pescatarian)
        else:
            return "Sorry, I can't understand."
    
    def transform_to_keto(self, inp: str, cfg) -> str:
        inp = inp.lower()
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        ori_recipe = recipe_handler[-1].ori_recipe
        recipe = recipe_handler[-1].recipe
        
        pattern = r'\b(transform|make)\b.+?keto'
        if bool(re.search(pattern, inp)):
            for i in range(len(recipe.ingredients)):
                ingredient = recipe.ingredients[i]
                for type in ingredient.types:
                    if type == "carbs":
                        # transform
                        recipe.ingredients[i].name = random.choice(INGREDIENTS["keto_carb_substitute"])
                        recipe.ingredients[i].types = ["keto_carb_substitute"]
                    if type == "sweeteners":
                        # transform
                        recipe.ingredients[i].name = random.choice(INGREDIENTS["keto_sweetener"])
                        recipe.ingredients[i].types = ["keto_sweetener"]

            return f"I've made the recipe keto for you. Here are the ingredients of the keto version of **{recipe.title}:**\n\n* [x] " + "\n\n* [x] ".join(map(str, recipe.ingredients))
        else:
            return "Sorry, I can't understand."
    
    def transform_to_pescatarian(self, inp: str, cfg) -> str:
        inp = inp.lower()
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        ori_recipe = recipe_handler[-1].ori_recipe
        recipe = recipe_handler[-1].recipe
        
        pattern = r'\b(transform|make)\b.+?pescatarian'
        if bool(re.search(pattern, inp)):
            for i in range(len(recipe.ingredients)):
                ingredient = recipe.ingredients[i]
                for type in ingredient.types:
                    if type == "meat_and_poultry":
                        # transform
                        recipe.ingredients[i].name = random.choice(INGREDIENTS["seafood"])
                        recipe.ingredients[i].types = ["seafood"]

            return f"I've made the recipe pescatarian for you. Here are the ingredients of the pescatarian version of **{recipe.title}:**\n\n* [x] " + "\n\n* [x] ".join(map(str, recipe.ingredients))
        else:
            return "Sorry, I can't understand."
        
    def transform_to_kosher(self, inp: str, cfg) -> str:
        inp = inp.lower()
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        ori_recipe = recipe_handler[-1].ori_recipe
        recipe = recipe_handler[-1].recipe
        
        pattern = r'\b(transform|make)\b.+?kosher'
        
        if bool(re.search(pattern, inp)):
            ing_types = []
            for i in range(len(recipe.ingredients)):
                ingredient = recipe.ingredients[i]
                for type in ingredient.types:
                    ing_types.append(type)
                    if type == "meat_and_poultry" or type == "seafood":
                        found = False
                        for item in INGREDIENTS["kosher_meat"]:
                            if item in ingredient.name:
                                found = True
                                break
                        if not found:
                            # transform
                            recipe.ingredients[i].name = random.choice(INGREDIENTS["kosher_meat"])
                            recipe.ingredients[i].types = ["kosher_meat"]
                        recipe.ingredients[i].descriptor = None
                        recipe.ingredients[i].prep = None
                
                    if (type == "milk_and_dairy" or type == "cheese") and ("meat_and_poultry" in ing_types):
                        # transform
                        if type == "milk_and_dairy":
                            recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_milk"])
                            recipe.ingredients[i].types = ["kosher_dairy"]
                        elif type == "cheese":
                            recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_cheese"])
                            recipe.ingredients[i].types = ["kosher_dairy"]
                            
                    elif (type == "meat_and_poultry") and ("milk_and_dairy" in ing_types or "cheese" in ing_types):
                        recipe.ingredients[i].name = random.choice(INGREDIENTS["pareve_proteins"])
                        recipe.ingredients[i].types = ["pareve_proteins"]
            
            return f"I've made the recipe Kosher for you. Here are the ingredients of the Kosher version of **{recipe.title}:**\n\n* [x] " + "\n\n* [x] ".join(map(str, recipe.ingredients))
        
        else:
            return "Sorry, I can't understand."
    
    
    def transform_to_vegetarian_vegan(self, inp: str, cfg) -> str:
        inp = inp.lower()
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        ori_recipe = recipe_handler[-1].ori_recipe
        recipe = recipe_handler[-1].recipe
        
        pattern = r'\b(transform|make)\b.+?vegetarian'
        if bool(re.search(pattern, inp)):
            for i in range(len(recipe.ingredients)):
                ingredient = recipe.ingredients[i]
                for type in ingredient.types:
                    if type == "meat_and_poultry" or type == "seafood":
                        # transform
                        recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_protein"])
                        recipe.ingredients[i].types = ["vegan_protein"]
                        recipe.ingredients[i].descriptor = None
                        recipe.ingredients[i].prep = None
            
            return f"I've made the recipe vegetarian for you. Here are the ingredients of the vegetarian version of **{recipe.title}:**\n\n* [x] " + "\n\n* [x] ".join(map(str, recipe.ingredients))
        
        pattern = r'\b(transform|make)\b.+?vegan'
        if bool(re.search(pattern, inp)):
            for i in range(len(recipe.ingredients)):
                ingredient = recipe.ingredients[i]
                for type in ingredient.types:
                    if type == "meat_and_poultry" or type == "seafood":
                        # transform
                        recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_protein"])
                        recipe.ingredients[i].types = ["vegan_protein"]
                    elif type == "milk_and_dairy":
                        if "milk" in ingredient.name:
                            recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_milk"])
                            recipe.ingredients[i].types = ["vegan_milk"]
                        elif "yogurt" in ingredient.name:
                            recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_yogurt"])
                            recipe.ingredients[i].types = ["vegan_yogurt"]
                        elif "butter" in ingredient.name:
                            recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_butter"])
                            recipe.ingredients[i].types = ["vegan_butter"]
                        elif "cream" in ingredient.name:
                            recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_cream"])
                            recipe.ingredients[i].types = ["vegan_cream"]
                        else:
                            recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_milk"])
                            recipe.ingredients[i].types = ["vegan_milk"]
                    elif type == "eggs":
                        recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_eggs"])
                        recipe.ingredients[i].types = ["vegan_eggs"]
                    elif type == "cheese":
                        recipe.ingredients[i].name = random.choice(INGREDIENTS["vegan_cheese"])
                        recipe.ingredients[i].types = ["vegan_cheese"]
            
            return f"I've made the recipe vegan for you. Here are the ingredients of the vegan version of **{recipe.title}:**\n\n* [x] " + "\n\n* [x] ".join(map(str, recipe.ingredients))
        else:
            return "Sorry, I can't understand."
        
        
    def match(self, inp: str, cfg) -> int:
        # handler = [handler for handler in cfg['handler'] if handler.type() == "get_ingredient"]
        if "Sorry" not in self.ask_is_vegetarian_vegan(inp, cfg):
            return 1
        elif "Sorry" not in self.ask_is_kosher(inp, cfg):
            return 1
        elif "Sorry" not in self.ask_is_pescatarian(inp, cfg):
            return 1
        elif "Sorry" not in self.transform_to_keto(inp, cfg):
            return 1
        elif "Sorry" not in self.transform_to_pescatarian(inp, cfg):
            return 1
        elif "Sorry" not in self.transform_to_kosher(inp, cfg):
            return 1
        elif "Sorry" not in self.transform_to_vegetarian_vegan(inp, cfg):
            return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        cfg['handler'].append(self)
        
        ans = self.ask_is_vegetarian_vegan(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.ask_is_kosher(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.ask_is_pescatarian(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.transform_to_keto(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.transform_to_pescatarian(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.transform_to_kosher(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.transform_to_vegetarian_vegan(inp, cfg)
        if "Sorry" not in ans:
            return ans
        return "Sorry, I can't understand."
    
       
