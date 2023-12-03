import re
from copy import deepcopy
from nltk import pos_tag, word_tokenize
import spacy
from utils.ontologies import *
from typing import Dict
from utils.ingredient import RecipeIngredient
from spacy.matcher import Matcher
from utils.substep import RecipeSubstep

nlp = spacy.load('en_core_web_sm')


class RecipeStep:
    def __init__(self, text, step_number, substeps: list[RecipeSubstep]):
        self.text = text
        self.step_number = step_number
        self.substeps = substeps


    @property
    def processed_text(self):
        text = deepcopy(self.text)

        for substep in self.substeps:
            if substep.primary_actions is not None:
                for action in substep.primary_actions:
                    if f"**{action[0]}**" in text:
                        continue
                    text = text.replace(action[0], f'**{action[0]}**')
            if substep.secondary_actions is not None:
                for action in substep.secondary_actions:
                    if f"**{action[0]}**" in text:
                        continue
                    text = text.replace(action[0], f'**{action[0]}**')

            if substep.tools is not None:
                for tool in substep.tools:
                    if f"**{tool[0]}**" in text:
                        continue
                    text = text.replace(tool[0], f'**{tool[0]}**')
                    
            # Hopefully takes care of changing the names after transformations

            if len(substep.ingredients) > 0:
                for ing in substep.ingredients:
                    if f"**{ing[0]}**" in text:
                        continue
                    text = text.replace(ing[0], f'**{ing[0]}**')
        text = text.replace("****", "**")
        return text
        

    def __str__(self):
        return self.processed_text
    
    @staticmethod
    def from_string(step: str, ingredients: list[RecipeIngredient], step_number: int):
        step =  step.strip()
        step = RecipeStep.expand_degrees(step)
        step = step.lower()
        
        #doc = nlp(step)
        substeps = []

        # Get parameters by string matchin methods
        text = step.strip()
        sentences = split_string_by_multiple_delimiters(text,['.', '?', '!', ';'])
        for sent in sentences:
            sent = sent.strip()
            if sent == '':
                continue
            for part in sent.split("then"):
                part = part.strip()
                doc = nlp(sent)
                isStep = RecipeStep.isStep(doc)
                if isStep:
                    primary_actions, secondary_actions, misc_actions = RecipeSubstep.get_actions(doc)
                    actions = {'primary': primary_actions, 'secondary': secondary_actions, 'misc': misc_actions}
                
                    substeps.append(RecipeSubstep(doc, ingredients, actions, step_number))
                else:
                    if len(substeps) > 0:
                        substeps[-1].add_additional_info(part)
                    continue                
       
        return RecipeStep(text, step_number, substeps)
        
    @staticmethod
    def expand_degrees(text):
        text = text.replace('°', ' degrees ')
        text = text.replace('º', ' degrees ')
        text = text.replace('°C', ' degrees celsius ')
        text = text.replace('ºC', ' degrees celsius ')
        text = text.replace('°F', ' degrees fahrenheit ')
        text = text.replace('ºF', ' degrees fahrenheit ')
        text = text.strip()
        return text
    
    @staticmethod
    def map_to_substep(start, end, sentence_indices):
        for i in range(len(sentence_indices)):
            if start >= sentence_indices[i][0] and end <= sentence_indices[i][1]:
                return i
        return None
    
    @staticmethod
    def isStep(doc):
        if doc[0].pos_ == "VERB" and (doc[0].dep_ == "ROOT" or doc[0].dep_ == "nsubj") and doc[0].tag_ == "VB":
            return True
        elif doc[0].dep_ == "prep":
            for token in doc:
                if token.pos_ == "VERB" and token.dep_ == "ROOT" and (token.tag_ == "VB" or token.tag_ == "VBP"):
                    return True
        elif doc[0].text in PRIMARY_COOKING_ACTIONS or doc[0].text in SECONDARY_COOKING_ACTIONS:
            return True
        
        return False
    
        
def split_string_by_multiple_delimiters(string, delimiters):
    # Create a regex pattern with the delimiters
    pattern = '|'.join(map(re.escape, delimiters))

    # Split the string using the created pattern
    return re.split(pattern, string)

if __name__ == "__main__":
    
    # Initialize ingredients
    ingredient_strs = ["Cooking spray, for pan","1 1/2 lb. baby mushrooms", "2 tbsp. butter", "2 cloves garlic, minced", "1/4 c. breadcrumbs", "Kosher salt", "Freshly ground black pepper", "1/4 c. freshly grated Parmesan, plus more for topping",
                       "4 oz. cream cheese, softened", "2 tbsp. freshly chopped parsley, plus more for garnish", "1 tbsp. freshly chopped thyme"]
    
    ingredients = {}
    for ing in ingredient_strs:
        ingredient = RecipeIngredient.from_string(ing)
        ingredients[ingredient.name] = ingredient
    
    step = RecipeStep.from_string("Preheat oven to 400°. Grease a baking sheet with cooking spray. Remove stems from mushrooms and finely chop stems. Place mushroom caps on baking sheet.", ingredients, 1)
    step2 = RecipeStep.from_string("In a medium skillet over medium heat, melt butter. Add chopped mushrooms stems and cook until most of the moisture is out, 5 minutes. Add garlic and cook until fragrant, 1 minute then add breadcrumbs and let toast slightly, 3 minutes. Season with salt and pepper. Remove from heat and let cool slightly.", ingredients, 2)
    step3 = RecipeStep.from_string("In a large bowl mix together mushroom stem mixture, Parmesan, cream cheese, parsley, and thyme. Season with salt and pepper. Fill mushroom caps with filling and sprinkle with more Parmesan.", ingredients, 3)
    step4 = RecipeStep.from_string("Bake until mushrooms are tender and filling is golden, 20 minutes.", ingredients, 4)
    step5 = RecipeStep.from_string("Garnish with parsley and serve.", ingredients, 5)
    print(step)