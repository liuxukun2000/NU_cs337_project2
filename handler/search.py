from handler.base import BaseHandler


class SearchHandler(BaseHandler):
    def __init__(self):
        self.ask_that = False
        self.keywords = ""

    @staticmethod
    def type() -> str:
        return "search"

    def match(self, inp: str, cfg) -> int:
        text = inp.lower().strip()
        if self.ask_that:
            return 100
        if "how" in text and "that" in text:
            return 3
        if text.startswith("how") or text.startswith("what"):
            return 1

        return 0

    def handle(self, inp: str, cfg) -> str:
        if self.ask_that or ('how' in inp.lower() and 'that' in inp.lower()):
            if cfg['handler'] and cfg['handler'][-1].type() == "search":
                ans = f"https://en.wikipedia.org/wiki/{self.keywords}"
                return f"No worries. I found a Wikipedia page for you: {ans}"
            handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
            step = [handler for handler in cfg['handler'] if handler.type() == "get_step"]
            ans = []
            if handler:
                recipe = handler[-1].recipe
                step = step[-1].step - 1 if step else 0
                step = recipe.steps[step]
                for i in step.substeps:
                    ans.extend(i.primary_actions)
                if not ans:
                    for i in step.substeps:
                        ans.extend(i.secondary_actions)
                if not ans:
                    return "Sorry, I can't find actions in this step."
                if len(ans) > 1 and not self.ask_that:
                    self.ask_that = True
                    return "I found multiple actions in this step. Please specify one:\n\n" + "\n\n".join([i[0] for i in ans])
                if self.ask_that:
                    for i in ans:
                        if i[0] in inp or inp in i[0]:
                            ans = i
                            break
                    self.ask_that = False
                while isinstance(ans, tuple) or isinstance(ans, list):
                    ans = ans[0]
                ans = f"https://en.wikipedia.org/wiki/{ans}"
                return f"No worries. I found a Wikipedia page for you: {ans}"
            else:
                return "Please specify a recipe first."
        elif 'how' in inp.lower():
            pos = inp.lower().find(" i ")
            text = inp.lower().strip()
            if pos == -1:
                pos = inp.lower().find(" to ")
                if pos != -1:
                    text = inp[pos + 4:].strip()
            else:
                pos += 3
                text = inp[pos:].strip()
            if pos == -1:
                return "Sorry, I don't understand."
            cfg['handler'].append(self)
            text = ''.join([i for i in text if i.isalpha() or i == ' '])
            text = text.replace(" ", "+")
            self.keywords = text
            return f"No worries. I found a YouTube video for you: https://www.youtube.com/results?search_query={text}"
        else:
            pos = inp.lower().find("is a")
            if pos == -1:
                pos = inp.lower().find("is an")
                if pos != -1:
                    pos += 5
            if pos == -1:
                pos = inp.lower().find("is the")
                if pos != -1:
                    pos += 6
            if pos == -1:
                pos = inp.lower().find("is")
                if pos != -1:
                    pos += 2
            if pos == -1:
                pos = inp.lower().find("are")
                if pos != -1:
                    pos += 3
            if pos == -1:
                return "Sorry, I don't understand."
            cfg['handler'].append(self)
            text = inp[pos:].strip()
            text = ''.join([i for i in text if i.isalpha() or i == ' '])
            text = text.replace(" ", "+")
            self.keywords = text
            return f"No worries. I found a Wikipedia page for you: https://en.wikipedia.org/wiki/{text}"

