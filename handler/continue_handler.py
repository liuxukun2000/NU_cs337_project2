from handler.base import BaseHandler


class ContinueHandler(BaseHandler):

    def __init__(self):
        pass

    @staticmethod
    def type() -> str:
        return "continue"

    def match(self, inp: str, cfg) -> int:
        if len(cfg['handler']) and cfg['handler'][-1].type() == "get_step": # TODO: add more handlers
            if inp.lower().strip().startswith("continue"):
                return 1
            if inp.lower().strip().startswith("next"):
                return 1
            if inp.lower().strip().startswith("go"):
                return 1
        return 0

    def handle(self, inp: str, cfg) -> str:
        handler = cfg['handler'][-1]
        if handler.type() == "get_step":
            return handler.handle(inp, cfg)
        return "Sorry, I don't understand."