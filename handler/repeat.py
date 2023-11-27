from handler.base import BaseHandler


class RepeatHandler(BaseHandler):
    def __init__(self):
        pass

    @staticmethod
    def type() -> str:
        return "repeat"

    def match(self, inp: str, cfg) -> int:
        text = inp.lower().strip()
        if text.startswith("repeat"):
            return 2
        if "repeat" in text:
            return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        if len(cfg['history']) == 0:
            return "Sorry, I can't repeat anything."
        return cfg['history'][-1]


