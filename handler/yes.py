from handler.base import BaseHandler


class YesHandler(BaseHandler):
    def __init__(self):
        pass

    @staticmethod
    def type() -> str:
        return "yes"

    def match(self, inp: str, cfg) -> int:
        if len(cfg['handler']) and cfg['handler'][-1].type() == "default":
            if inp.lower().strip().startswith("yes"):
                return 1
            if inp.lower().strip().startswith("sure"):
                return 1
            if inp.lower().strip().startswith("ok"):
                return 1
            if inp.lower().strip().startswith("y"):
                return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        handler = cfg['handler'][-1]
        if handler.type() == "default":
            return handler.handler.handle(inp, cfg)
        return "Sorry, I don't understand."