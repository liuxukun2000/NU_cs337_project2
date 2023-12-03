import re

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
                return 2
        if ("show" in inp.lower() or 'give' in inp.lower()) and "step" in inp.lower():
            return 2
        if "step" in inp.lower():
            return 1
        return 0

    def get_step_num(self, inp: str):
        if "first" in inp.lower() or "1st" in inp.lower():
            return 1
        if "second" in inp.lower() or "2nd" in inp.lower():
            return 2
        if "third" in inp.lower() or "3rd" in inp.lower():
            return 3
        if "fourth" in inp.lower() or "4th" in inp.lower():
            return 4
        if "fifth" in inp.lower() or "5th" in inp.lower():
            return 5
        if "sixth" in inp.lower() or "6th" in inp.lower():
            return 6
        if "seventh" in inp.lower() or "7th" in inp.lower():
            return 7
        if "eighth" in inp.lower() or "8th" in inp.lower():
            return 8
        if "ninth" in inp.lower() or "9th" in inp.lower():
            return 9
        if "tenth" in inp.lower() or "10th" in inp.lower():
            return 10
        if "last" in inp.lower():
            return 100
        if "go back" in inp.lower():
            return self.step - 1
        if "go forward" in inp.lower():
            return self.step + 1
        if "next" in inp.lower():
            return self.step + 1
        if "previous" in inp.lower():
            return self.step - 1
        if "current" in inp.lower():
            return self.step
        return -1

    def handle(self, inp: str, cfg) -> str:
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        recipe = recipe_handler[-1].recipe
        if self.title != recipe.title:
            self.title = recipe.title
            self.step = 0
        user_step = self.get_step_num(inp)
        if user_step == -1:
            self.step += 1
        else:
            self.step = user_step
        cfg['handler'].append(self)
        if self.step > len(recipe.steps):
            return f"Sorry, there is no more step."
        if self.step < 1:
            return f"Sorry, there is no step before this."
        return f"Sure. Here is the **Step {self.step}:**\n\n{recipe.steps[self.step - 1]}"


    def clear(self):
        self.title = ""
        self.step = 0