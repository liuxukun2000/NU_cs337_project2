import re

from handler.base import BaseHandler


class AmountHandler(BaseHandler):
    def __init__(self):
        self.number = -1

    @staticmethod
    def type() -> str:
        return "amount"

    def _get_number(self, inp: str) -> int:
        regex = r"\d+"
        ans = re.findall(regex, inp)
        return sum([int(x) for x in ans]) // len(ans) if len(ans) else -1
    def match(self, inp: str, cfg) -> int:
        handler = [handler for handler in cfg['handler'] if handler.type() == "get_ingredient"]
        # if len(cfg['handler']) and cfg['handler'][-1].type() == "get_ingredient":
        if handler:
            if ("people" in inp.lower() or 'person' in inp.lower()) and ("serving" in inp.lower() or self._get_number(inp) != -1):
                return 1
        if len(cfg['handler']) and cfg['handler'][-1].type() == "amount":
            if self._get_number(inp) != -1:
                return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        recipe = recipe_handler[-1].recipe
        ori_recipe = recipe_handler[-1].ori_recipe
        cfg['handler'].append(self)
        number = self._get_number(inp)
        self.number = number
        if number == -1:
            return "Please specify the number of servings."
        for i in range(len(recipe.ingredients)):
            ingredient = recipe.ingredients[i]
            if ingredient.quantity is not None:
                ingredient.quantity = float(ori_recipe.ingredients[i].quantity) * number / recipe.servings
                ingredient.quantity = round(ingredient.quantity, 1)
        for i in range(len(recipe.steps)):
            step = recipe.steps[i]
            for substep in step.substeps:
                if len(substep.quantity) > 0:
                    for j in range(substep.quantity):
                        substep.quantity[j] = float(ori_recipe.steps[i].substeps[j].quantity) * number / recipe.servings
                        substep.quantity[j] = round(substep.quantity[j], 1)
        return f"Here are the ingredients of: **{recipe.title}:**\n\n* [x] " + "\n\n* [x] ".join(map(str, recipe.ingredients))
