from handler.continue_handler import ContinueHandler
from handler.get_ingredient import GetIngredientHandler
from handler.get_recipe import GetRecipeHandler
from handler.get_step import GetStepHandler
from handler.search import SearchHandler
from handler.select_web import SelectWebHandler
from handler.default import DefaultHandler
from handler.yes import YesHandler


class HandlerManager:
    def __init__(self):
        self.handlers = [
            SelectWebHandler(),
            GetRecipeHandler(),
            GetIngredientHandler(),
            GetStepHandler(),
            ContinueHandler(),
            SearchHandler(),
            YesHandler(),
        ]
        self.default_handler = DefaultHandler()
        self.cfg = dict(handler=[])

    def handle(self, inp: str) -> str:
        max_score = 0
        handler = None
        for h in self.handlers:
            score = h.match(inp, self.cfg)
            # print(h.type(), score)
            if score >= max_score and score > 0:
                max_score = score
                handler = h
        if handler is None:
            return self.default_handler.handle(inp, self.cfg)
        return handler.handle(inp, self.cfg)

    def run(self):
        print("Hi, I am a recipe bot. I can help you with recipes.")
        while True:
            inp = input(">>> ")
            if inp.lower() == "exit":
                print("Bye!")
                break
            print(self.handle(inp))

    def stream(self, inp: str):
        ans = self.handle(inp).split(' ')
        for i in ans:
            yield i


