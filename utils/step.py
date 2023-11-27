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

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def to_dict(self):
        return {"name": self.name, "description": self.description, "ingredients": self.ingredients, "equipment": self.equipment, "instructions": self.instructions}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def to_yaml(self):
        return yaml.dump(self.to_dict(), indent=4)

    def to_xml(self):
        return dicttoxml(self.to_dict(), custom_root="step", attr_type=False).decode("utf-8")

    def to_csv(self):
        return ",".join([self.name, self.description, self.ingredients, self.equipment, self.instructions])

    def to_tsv(self):
        return "\t".join([self.name, self.description, self.ingredients, self.equipment, self.instructions])