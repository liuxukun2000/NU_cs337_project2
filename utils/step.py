import re
from nltk import pos_tag, word_tokenize
import spacy
from ontologies import *
from typing import Dict
from ingredient import RecipeIngredient
from spacy.matcher import Matcher
from substep import RecipeSubstep

nlp = spacy.load('en_core_web_sm')


class RecipeStep():
    def __init__(self, text, step_number, substeps: list[RecipeSubstep]):
        self.text = text
        self.step_number = step_number
        self.substeps = substeps
        

    def __str__(self):
        return f"Step: {self.name}\nDescription: {self.description}\nIngredients: {self.ingredients}\nEquipment: {self.equipment}\nInstructions: {self.instructions}"

    def __repr__(self):
        return f"Step: {self.name}\nDescription: {self.description}\nIngredients: {self.ingredients}\nEquipment: {self.equipment}\nInstructions: {self.instructions}"

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description and self.ingredients == other.ingredients and self.equipment == other.equipment and self.instructions == other.instructions

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.name, self.description, self.ingredients, self.equipment, self.instructions))
    
    @staticmethod
    def from_string(step: str, ingredients: Dict[str, RecipeIngredient], step_number: int):
        step = RecipeStep.preprocess(step)
        step.step.strip()
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
                    substeps.append(RecipeSubstep(doc, ingredients, step_number))
                else:
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
        if doc[0].pos_ == "VERB" and doc[0].dep_ == "ROOT" and doc[0].tag_ == "VB":
            return True
        elif doc[0].dep_ == "prep":
            for token in doc:
                if token.pos_ == "VERB" and doc[0].dep_ == "ROOT" and doc[0].tag_ == "VB":
                    return True
        return False
    
        
def split_string_by_multiple_delimiters(string, delimiters):
    # Create a regex pattern with the delimiters
    pattern = '|'.join(map(re.escape, delimiters))

    # Split the string using the created pattern
    return re.split(pattern, string)
