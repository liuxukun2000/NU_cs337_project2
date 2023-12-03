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
        if ("time" in inp or "long" in inp or 'end' in inp or 'duration' in inp) and handler:
            recipe = handler[-1].recipe
            step = step[-1].step - 1
            steps = recipe.steps[step]
            durations, conditions = [], []
            num = 0
            for sub in steps.substeps:
                if sub.duration:
                    durations.append(sub.duration[0][0])
                    num += 1
                else:
                    durations.append(None)
                if sub.end_condition:
                    conditions.append(sub.end_condition[0][0])
                    num += 1
                else:
                    conditions.append(None)
            ans = []
            if not num:
                return "I can't find time in this step."
            else:
                for t, c in zip(durations, conditions):
                    if t and c:
                        ans.append(f"{t} or {c}")
                    if not t and not c:
                        continue
                    ans.append(t or c)
                if len(ans) == 1:
                    return f"Time of this step is: {ans[0]}."
                else:
                    return f"There are many sub-steps in this step. Time of these sub-steps are:\n\n\n\n" + '\n\n'.join(ans[:-1]) + "and \n\n" + ans[-1]
        else:
            return "Sorry, I can't find time in this step."

    def ask_temperature(self, inp: str, cfg) -> str:
        inp = inp.lower()
        handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        step = [handler for handler in cfg['handler'] if handler.type() == "get_step"]
        if ("temperature" in inp or "heat" in inp or 'hot' in inp) and handler:
            recipe = handler[-1].recipe
            step = step[-1].step - 1
            steps = recipe.steps[step]
            for sub in steps.substeps:
                if sub.temperature:
                    return f"Temperature of this step is: {sub.temperature[0][0]}."
            return "I can't find temperature in this step."
        else:
            return "Sorry, I can't find temperature in this step."

    def ask_time_sp(self, inp: str, cfg):
        inp = inp.lower()
        handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        step = [handler for handler in cfg['handler'] if handler.type() == "get_step"]
        regex = re.compile(r'how (many|much) (minutes|minute|mins|min|m|time|hour|hours) to ([\w\s]+)')
        ans = regex.search(inp)
        if ans and handler:
            ans = ans.group(3)
            anss = []
            recipe = handler[-1].recipe
            step = step[-1].step - 1
            steps = recipe.steps[step]
            for sub in steps.substeps:
                if sub.primary_actions:
                    for i in sub.primary_actions:
                        if i[0] in ans:
                            if sub.duration:
                                anss.append(sub)
            print(anss)
            ans = ans.split()
            res = None
            for i in anss:
                if res:
                    break
                for j in ans:
                    if j in i.text:
                        res = i.duration[0][0]
                        break
            if res:
                return f"Time of this step is: {res}."
            return "I can't find time in this step."
        else:
            return "Sorry, I can't find time in this step."

    def ask_actions(self, inp: str, cfg) -> str:
        inp = inp.lower()
        handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        step = [handler for handler in cfg['handler'] if handler.type() == "get_step"]
        if ("action" in inp or " do " in inp or 'step' in inp) and handler:
            recipe = handler[-1].recipe
            step = step[-1].step - 1
            steps = recipe.steps[step]
            ans = []
            for sub in steps.substeps:
                ans.extend(sub.primary_actions)
                ans.extend(sub.secondary_actions)
                ans.extend(sub.misc_actions)
            ans = [i[0] for i in ans]
            return f"Actions of this step are:\n\n" + "\n\n".join(map(str, ans))
        else:
            return "Sorry, I can't find actions in this step."
    def match(self, inp: str, cfg) -> int:
        if "Sorry" not in self.ask_ingredients(inp, cfg):
            return 1
        elif "Sorry" not in self.ask_tool(inp, cfg):
            return 1
        elif "Sorry" not in self.ask_time_sp(inp, cfg):
            return 1
        elif "Sorry" not in self.ask_time(inp, cfg):
            return 1
        elif "Sorry" not in self.ask_temperature(inp, cfg):
            return 1
        elif "Sorry" not in self.ask_actions(inp, cfg):
            return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        recipe_handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not recipe_handler:
            return "Please specify a recipe first."
        cfg['handler'].append(self)
        ans = self.ask_time_sp(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.ask_ingredients(inp, cfg)
        if "Sorry" not in ans :
            return ans
        ans = self.ask_tool(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.ask_time(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.ask_temperature(inp, cfg)
        if "Sorry" not in ans:
            return ans
        ans = self.ask_actions(inp, cfg)
        if "Sorry" not in ans:
            return ans
        return "Sorry, I don't understand."
