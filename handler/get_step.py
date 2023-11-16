from handler.base import BaseHandler


class GetStepHandler(BaseHandler):
    def __init__(self):
        self.title = ""
        self.step = 0

    @staticmethod
    def type() -> str:
        return "get_step"

    def match(self, inp: str, cfg) -> int:
        if len(cfg['handler']) and cfg['handler'][-1].type() == "get_recipe":
            if inp.lower().strip().startswith("2"):
                return 1
        if ("show" in inp.lower() or 'give' in inp.lower()) and "step" in inp.lower():
            return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        recipe = recipe_handler[-1].recipe
        if self.title != recipe.title:
            self.title = recipe.title
            self.step = 0
        self.step += 1
        cfg['handler'].append(self)
        if self.step > len(recipe.steps):
            return f"Sorry, there is no more step."
        return f"Sure. Here is the **Step {self.step}:**\n\n{recipe.steps[self.step - 1]}"
    ## TODO: get nth step

    def clear(self):
        self.title = ""
        self.step = 0