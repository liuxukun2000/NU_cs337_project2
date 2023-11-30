import re
from nltk import pos_tag, word_tokenize
import spacy
from utils.ontologies import *

nlp = spacy.load('en_core_web_sm')

class RecipeIngredient:
    def __init__(self, name, quantity, unit, prep, descriptor, types, alt=None):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.prep = prep
        self.descriptor = descriptor
        self.types = types
        self.alt = alt

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"

    def __repr__(self):
        return f"{self.quantity} {self.unit} {self.name}"
    
    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity and self.unit == other.unit
    
    def __hash__(self):
        return hash((self.name, self.quantity, self.unit))
    
    @staticmethod
    def from_string(ing) -> "RecipeIngredient":
        ing = RecipeIngredient.preprocess(ing)
        
        unit = None
        name = None
        quantity = None
        prep = None
        descriptor = None
        
        # Split by comma
        ing = ing.split(',')[0]
        
        # Handle alternatives
        if 'or' in ing:
            ing = ing.split('or')[0]
            alt = RecipeIngredient.from_string(ing.split('or')[1])
        
        second = None
        if len(ing.split(','))> 1:
            second = ing.split(',')[1]

        # Find the quantity and unit of the ingredient from ing
        doc = nlp(ing)
        
        if doc[0].pos_ == 'NUM':
            quantity = doc[0].text
            if doc[1].text in COOKING_MEASUREMENTS:
                unit = doc[1].text
            else: 
                unit = None
        else:
            quantity = None
            unit = None
        
        name = ''
        descriptor = ''
        prep = ''
        types = []
        # Find the name of the ingredient from ing, as well as any preprocessing and descriptors in the first part of the ingredient
        for token in doc:
            if (token.dep_ in ['nsubj', 'dobj', 'ROOT']) and (token.pos_ in ['NOUN', 'PROPN']) and (token.text not in COOKING_MEASUREMENTS):
                for child in token.children:
                    if (child not in COOKING_MEASUREMENTS) and (child.dep_ == 'compound'):
                        name += child.text + ' '
                    elif (child not in COOKING_MEASUREMENTS) and (child.dep_ == 'amod'):
                        descriptor += child.text + ' '
            
                name += token.text
            elif token.dep == 'ROOT' and token.pos_ == 'VERB':
                prep += token.text
                # check for conjunctions
                for child in token.children:
                    if child.dep_ == 'conj' or child.dep_ == 'cc':
                        prep += child.text + ' '
                
                prep = prep.strip()
                
        # Handle the second part of the ingredient
        if second:
            if second.split(" ")[0] != "or" and second.split(" ")[0] != "plus":
                prep += ' ' + second
                prep = prep.strip()
    
        # Find the type of the ingredient
        
                
        
    @staticmethod
    def expand_units(ing):
        # Expand units to their full names
        ing = ing.replace('tsp.', 'teaspoon')
        ing = ing.replace('tbsp.', 'tablespoon')
        ing = ing.replace('oz.', 'ounce')
        ing = ing.replace('lb.', 'pound')
        ing = ing.replace('c.', 'cup')
        ing = ing.replace('pt.', 'pint')
        ing = ing.replace('qt.', 'quart')
        ing = ing.replace('gal.', 'gallon')
        return ing
    
    @staticmethod
    def fraction_to_decimal(fraction):
        unicode_fractions = {
            '½': 0.5, '⅓': 1/3, '⅔': 2/3, '¼': 0.25, '¾': 0.75,
            '⅕': 0.2, '⅖': 0.4, '⅗': 0.6, '⅘': 0.8, '⅙': 1/6, 
            '⅚': 5/6, '⅛': 0.125, '⅜': 0.375, '⅝': 0.625, '⅞': 0.875
        }
        if fraction in unicode_fractions:
            return unicode_fractions[fraction]

        if '/' in fraction:
            numerator, denominator = fraction.split('/')
            return float(numerator) / float(denominator)

        return 0

    @staticmethod
    def replace_quantity_with_decimal(ingredient):
        # Updated pattern to match whole number with optional fraction, standalone fraction, or standalone whole number
        quantity_pattern = r'((\d+\s*)(\d+/\d+|[\u00BC-\u00BE\u2150-\u215E]))|((\d+/\d+|[\u00BC-\u00BE\u2150-\u215E]))|(\d+)'

        def replace_match(match):
            # Extract the whole number and fraction parts
            whole_number = match.group(6) or match.group(2)
            fraction = match.group(3) or match.group(5) 

            decimal_whole_number = int(whole_number) if whole_number else 0
            decimal_fraction = RecipeIngredient.fraction_to_decimal(fraction) if fraction else 0

            total_quantity = decimal_whole_number + decimal_fraction
            return str(total_quantity)

        # Replace the quantity with the decimal sum
        return re.sub(quantity_pattern, replace_match, ingredient, 1)
    
    @staticmethod
    def preprocess(ing):
        ing = ing.strip()
        
        # Expand units to their full names
        ing = RecipeIngredient.expand_units(ing)
        
        # Remove extra spaces
        ing = re.sub(r'\s+', ' ', ing)
        
        ing = RecipeIngredient.replace_quantity_with_decimal(ing)
        
        return ing
        
        
    