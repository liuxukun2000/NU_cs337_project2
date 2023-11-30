import re
from nltk import pos_tag, word_tokenize
import spacy
from ontologies import *
from typing import Dict
from ingredient import RecipeIngredient
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

class RecipeStep():
    def __init__(self, text, substeps, ingredients, tools, methods, duration, substep: bool = False):
        self.text = text
        self.substeps = substeps
        self.tools = tools
        self.methods = methods
        self.ingredients = ingredients
        self.duration = duration
        self.substep = substep

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
    def from_string(step, ingredients: Dict[str, RecipeIngredient]):
        step = RecipeStep.preprocess(step)
        step.step.strip()
        step = RecipeStep.expand_degrees(step)
        step = step.lower()
        doc = nlp(step)
        
        sentence_indices = []
        for sent in doc.sents:
            sentence_indices.append((sent.start, sent.end))
        
        # Get parameters by string matchin methods
        text = step.strip()
        substeps = text.split('.')
        for substep in substeps:
            substep = substep.strip()
            if substep == '':
                substeps.remove(substep) 
        
        # Get temperature, also store information about which substep it corresponds to
        temperature = {}
        for temp_word in TEMPERATURE:
            matcher = Matcher(nlp.vocab)
            if len(temp_word.split(' ')) > 1:
                pattern = [{'LOWER': temp_word.split(' ')[0]}, {"IS_PUNCT": True}, {'LOWER': temp_word.split(' ')[1]}]
            else:
                pattern = [{'LOWER': temp_word}]
            matcher.add(temp_word,[pattern])
            matches = matcher(doc)
            
            temp = None
            if len(matches) > 0:
                for match_id, start, end in matches:
                    span = doc[start:end]
                    if temp_word == "heat":
                        if start > 0 and doc[start-1].dep_ == "amod":
                            temp = doc[start-1].text + " heat"
                            if start > 2 and doc[start-2].text == "to" and doc[start-3].text == "low" or doc[start-3].text == "medium" or doc[start-3].text == "high":
                                temp = doc[start-3:end].text
                    
                    elif temp_word == "degrees":
                        if start > 0 and doc[start-1].pos_ == "NUM":
                            temp = doc[start-1].text + " degrees"
                    else: 
                        temp = temp_word
                    
                    if temp: 
                        temperature[temp] = RecipeStep.map_to_substep(start, end, sentence_indices)
                            
        # Get cooking methods
        methods = {}
        matcher = Matcher(nlp.vocab)
        patterns = [nlp.make_doc(method) for method in PRIMARY_COOKING_METHODS+SECONDARY_COOKING_METHODS]
        matcher.add("methods", patterns)
        
        for match_id, start, end in matcher(doc):
            span = doc[start:end]
            methods[span.text] = RecipeStep.map_to_substep(start, end, sentence_indices)

        # Get tools
        tools = {}
        matcher = Matcher(nlp.vocab)
        patterns = [nlp.make_doc(tool) for tool in COOKING_TOOLS]
        matcher.add("tools", patterns)
        
        for match_id, start, end in matcher(doc):
            span = doc[start:end]
            tools[span.text] = RecipeStep.map_to_substep(start, end, sentence_indices)

        # Get time - use doc.ents for this
        duration = {}
        for ent in doc.ents:
            if ent.label_ == "TIME":
                duration[ent.text] = RecipeStep.map_to_substep(ent.start, ent.end, sentence_indices)
        
        # Get ingredients - dictionary of ingredient object to substep and quantity used in current step
        ingredients = {}
        
        
        
        return RecipeStep(text, substeps, ingredients, tools, methods, duration)
    
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
    
    