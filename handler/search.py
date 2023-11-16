from handler.base import BaseHandler


class SearchHandler(BaseHandler):
    def __init__(self):
        pass

    @staticmethod
    def type() -> str:
        return "search"

    def match(self, inp: str, cfg) -> int:
        text = inp.lower().strip()
        if text.startswith("how") or text.startswith("what"):
            return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        pos = inp.lower().find(" i ")
        text = inp.lower().strip()
        if pos == -1:
            pos = inp.lower().find(" to ")
            if pos != -1:
                text = inp[pos + 4:].strip()
        else:
            text = inp[pos + 3:].strip()
        if pos == -1:
            return "Sorry, I don't understand."
        cfg['handler'].append(self)
        text = ''.join([i for i in text if i.isalpha() or i == ' '])
        text = text.replace(" ", "+")
        return f"No worries. I found a reference for you: https://www.youtube.com/results?search_query={text}"