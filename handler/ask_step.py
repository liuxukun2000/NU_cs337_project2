import re

from handler.base import BaseHandler


class AskStepsHandler(BaseHandler):
    def __init__(self):
        self.number = -1

    @staticmethod
    def type() -> str:
        return "ask_step"

    def ask_ingredients(self, inp: str, cfg) -> str:
        inp = inp.lower()
        handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        step = [handler for handler in cfg['handler'] if handler.type() == "get_step"]
        if "ingredient" in inp and handler:
            recipe = handler[-1].recipe
            step = step[-1].step - 1
            steps = recipe.steps[step]
            ans = []
            for sub_step in steps.substeps:
                ans.extend(sub_step.ingredients)
            ans = [i[0] for i in ans]
            return f"You need :\n\n" + "\n\n".join(map(str, ans)) + "\n\nfor this step."
        else:
            return "Sorry, I can't find ingredients in this step."

    def ask_tool(self, inp: str, cfg) -> str:
        inp = inp.lower()
        handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        step = [handler for handler in cfg['handler'] if handler.type() == "get_step"]
        if "tool" in inp and handler:
            recipe = handler[-1].recipe
            step = step[-1].step - 1
            steps = recipe.steps[step]
            ans = []
            for sub_step in steps.substeps:
                ans.extend(sub_step.tools)
            ans = [i[0] for i in ans]
            return f"You need :\n\n" + "\n\n".join(map(str, ans)) + "\n\nfor this step."
        else:
            return "Sorry, I can't find tools in this step."

    def ask_time(self, inp: str, cfg) -> str:
        inp = inp.lower()
        handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        step = [handler for handler in cfg['handler'] if handler.type() == "get_step"]
        if ("time" in inp or "long" in inp) and handler:
            recipe = handler[-1].recipe
            step = step[-1].step - 1
            steps = recipe.steps[step]
            for sub in steps.substeps:
                if sub.duration:
                    return f"This step takes {sub.duration} time."
            return "I can't find time in this step."
        else:
            return "Sorry, I can't find time in this step."
    def match(self, inp: str, cfg) -> int:
        if "Sorry" not in self.ask_ingredients(inp, cfg):
            return 1
        elif "Sorry" not in self.ask_tool(inp, cfg):
            return 1
        elif "Sorry" not in self.ask_time(inp, cfg):
            return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        ans = self.ask_ingredients(inp, cfg)
        cfg['handler'].append(self)
        if "Sorry" not in ans :
            return ans
        ans = self.ask_tool(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.ask_time(inp, cfg)
        if "Sorry" not in ans:
            return ans
        return "Sorry, I don't understand."
