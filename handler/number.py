from handler.base import BaseHandler


class NumberHandler(BaseHandler):
    def __init__(self):
        pass

    @staticmethod
    def type() -> str:
        return "number"

    def match(self, inp: str, cfg) -> int:
        text = inp.lower().strip()
        if 1 <= len(text) <= 3 and text[0].isdigit() and int(text[0]) in range(1, 5):
            return 100
        return 0

    def handle(self, inp: str, cfg) -> str:
        handler = [handler for handler in cfg['handler'] if handler.type() == "get_recipe"]
        if not handler:
            return "Please specify a recipe first."
        op = int(inp.lower().strip()[0])
        if op == 1:
            return cfg['get_ingredient'].handle(inp, cfg)
        elif op == 2:
            return cfg['get_step'].handle(inp, cfg)
        elif op == 3:
            return str(cfg['get_recipe'].recipe)
        elif op == 4:
            cfg['handler'] = []
            for name, handler in cfg.items():
                if issubclass(type(handler), BaseHandler):
                    handler.clear()
            return "Recipe cleared."
        return "Invalid input."


