class RecipeStep():
    def __init__(self, name, description, ingredients, equipment, instructions):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.equipment = equipment
        self.instructions = instructions

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