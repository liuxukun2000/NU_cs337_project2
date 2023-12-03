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
        if 'how' in inp.lower():
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
            return f"No worries. I found a Wikipedia page for you: https://en.wikipedia.org/wiki/{text}"

