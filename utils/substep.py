import re
import spacy
from ontologies import *
from typing import Dict
from ingredient import RecipeIngredient
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')

class RecipeSubstep():
    def __init__(self, doc, recipe_ingredients, actions, parent_step_number):
        self.text = doc.text
        self.parent_step_number = parent_step_number
        self.primary_actions = actions['primary']
        self.secondary_actions = actions['secondary']
        self.misc_actions = actions['misc']
        
        # All of these are lists. There is processing to be done in handler to handle multiple values.
        self.ingredients = self.get_ingredients(doc, recipe_ingredients)
        self.tools = self.get_tools(doc)
        self.duration, self.end_condition = self.get_duration(doc)
        self.temperature = self.get_temperature(doc)
        
        self.additional_info = None
    
    def add_additional_info(self, info):
        self.additional_info = info
    
    def get_temperature(self, doc: spacy.tokens.doc.Doc):
        temperature = []
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
                        
                        for action in reversed(self.secondary_actions):
                            if "heat" in action[0]:
                                self.secondary_actions.remove(action)
                    
                    elif temp_word == "degrees":
                        if start > 0 and doc[start-1].pos_ == "NUM":
                            temp = doc[start-1].text + " degrees"
                    else: 
                        temp = temp_word
                    
                    if temp: 
                        temperature.append((temp,start))
        
        return temperature
    
    def get_tools(self, doc: spacy.tokens.doc.Doc):
        tools = []
        matcher = PhraseMatcher(nlp.vocab)
        patterns = [nlp.make_doc(tool) for tool in COOKING_TOOLS]
        matcher.add("tools", patterns)
        
        for match_id, start, end in matcher(doc):
            span = doc[start:end]
            tools.append((span.text,start))
        
        return tools
    
    def get_duration(self, doc: spacy.tokens.doc.Doc):
        duration = []
        end_condition = []
        for ent in doc.ents:
            if ent.label_ == "TIME":
                duration.append((ent.text,ent.start))
    
        # Handle the "until" keyword
        for part in doc.text.split(','):
            doc = nlp(part)
            matcher = Matcher(nlp.vocab)
            pattern = [{"LOWER": 'until'}]
            matcher.add("until", [pattern])
            
            for match_id, start, end in matcher(doc):
                end_cond = ''
                if doc[start].dep_ == "mark":
                    head = doc[start].head
                    for item in head.subtree:
                        end_cond += item.text + ' '
                    end_condition.append((end_cond.strip(),start))
                    
                elif doc[start].dep_ == "prep" or doc[start].dep_ == "ROOT":
                    for item in doc[start].subtree:
                        end_cond += item.text + ' '
                    end_condition.append((end_cond.strip(),start))
                    
        return duration, end_condition
    
    def get_ingredients(self, doc: spacy.tokens.doc.Doc, ingredients: Dict[str, RecipeIngredient]):
        # String match the ingredients
        patterns = [nlp.make_doc(ing) for ing in ingredients.keys()]
        matcher = PhraseMatcher(nlp.vocab)
        matcher.add("ingredients", patterns)
        matches = matcher(doc)
        
        step_ingredients = []
        
        for match_id, start, end in matches:
            span = doc[start:end]
            ingredients[span.text].add_step(self.parent_step_number)
            step_ingredients.append((ingredients[span.text].name,start))
            
        # do a second pass
        for token in doc: 
            for ing in ingredients.keys():
                if token.text in ing and token.text not in [item[0] for item in step_ingredients]:
                    step_ingredients.append((ingredients[ing].name,token.i))
                    ingredients[ing].add_step(self.parent_step_number)
                    
        return step_ingredients
    
    @staticmethod
    def get_actions(doc: spacy.tokens.doc.Doc):
        # find actions through a combination of string matching and dependency parsing
        primary_actions = []
        secondary_actions = []
        misc_actions = []
        
        # match the cooking actions
        matcher = PhraseMatcher(nlp.vocab)
        primary_patterns = [nlp.make_doc(method) for method in PRIMARY_COOKING_ACTIONS]
        matcher.add("primary_methods", primary_patterns)
        secondary_patterns = [nlp.make_doc(method) for method in SECONDARY_COOKING_ACTIONS]
        matcher.add("secondary_methods", secondary_patterns)
        
        for match_id, start, end in matcher(doc):
            span = doc[start:end]
            if nlp.vocab.strings[match_id] == "primary_methods":
                primary_actions.append((span.text,start))
            elif nlp.vocab.strings[match_id] == "secondary_methods":
                secondary_actions.append((span.text,start))
        
        # find the misc actions
        if len(primary_actions) == 0 and len(secondary_actions) == 0:
            for token in doc:
                if token.dep_ == "ROOT" and token.pos_ == "VERB" and token.pos_ == "VB":
                    misc_actions.append((token.text, token.i))
                    
        return primary_actions, secondary_actions, misc_actions
    

    