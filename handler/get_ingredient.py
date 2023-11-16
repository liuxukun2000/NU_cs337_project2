from handler.base import BaseHandler


class GetIngredientHandler(BaseHandler):
    def __init__(self):
        pass

    @staticmethod
    def type() -> str:
        return "get_ingredient"

    def match(self, inp: str, cfg) -> int:
        if len(cfg['handler']) and cfg['handler'][-1].type() == "get_recipe":
            if inp.lower().strip().startswith("1"):
                return 1
        if ("show" in inp.lower() or 'give' in inp.lower()) and "ingredient" in inp.lower():
            return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        recipe = recipe_handler[-1].recipe
        cfg['handler'].append(self)
        return f"Here are the ingredients of: {recipe.title}\n" + "\n".join(recipe.ingredients)
