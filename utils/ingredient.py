class RecipeIngredient():
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"

    def __repr__(self):
        return f"{self.quantity} {self.unit} {self.name}"
    
    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity and self.unit == other.unit
    
    def __hash__(self):
        return hash((self.name, self.quantity, self.unit))
    
    