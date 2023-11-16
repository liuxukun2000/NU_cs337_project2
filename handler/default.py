from handler.base import BaseHandler


class DefaultHandler(BaseHandler):
    def __init__(self):
        self.handler = None

    @staticmethod
    def type() -> str:
        return "default"

    def match(self, inp: str, cfg) -> int:
        return 0

    def handle(self, inp: str, cfg) -> str:
        if not len(cfg['handler']):
            return "Sorry, I don't understand."
        if cfg['handler'][-1].type() == "search":
            handler = [handler for handler in cfg['handler'] if handler.type() == "get_step"]
            if handler:
                self.handler = handler[-1]
                cfg['handler'].append(self)
                return f"Should I continue to the **{self.handler.step + 1}nd Step** of **{self.handler.title}**?"
        return "Sorry, I don't understand."