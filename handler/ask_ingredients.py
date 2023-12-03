import re

from handler.base import BaseHandler


class AskIngredientsHandler(BaseHandler):
    def __init__(self):
        self.number = -1

    @staticmethod
    def type() -> str:
        return "ask_ingredients"

    def _get_name(self, inp: str) -> str:
        inp = inp.lower()
        regex = r"how (many|much) ([\w\s]+)"
        ans = re.search(regex, inp)
        if ans:
            return ans.group(2).replace(" do", "").replace(" i", "").replace("need", "")
        else:
            return inp.replace(" do", "").replace(" i", "").replace("need", "")
    def match(self, inp: str, cfg) -> int:
        handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        regex = r"how (many|much) "
        if len(handler) and re.findall(regex, inp.lower()):
            return 2
        return 0

    def handle(self, inp: str, cfg) -> str:
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        recipe = recipe_handler[-1].recipe

        cfg['handler'].append(self)
        name = self._get_name(inp)
        print(name)
        ans = [ingredient for ingredient in recipe.ingredients if ingredient.name in name]
        if not ans:
            for i in name.split():
                ans += [ingredient for ingredient in recipe.ingredients if i in ingredient.name]

        return f"You need :\n\n" + "\n\n".join(map(str, ans)) + "\n\nfor this recipe."
