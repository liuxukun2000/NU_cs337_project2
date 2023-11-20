from handler.continue_handler import ContinueHandler
from handler.get_ingredient import GetIngredientHandler
from handler.get_recipe import GetRecipeHandler
from handler.get_step import GetStepHandler
from handler.number import NumberHandler
from handler.repeat import RepeatHandler
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
            RepeatHandler(),
            NumberHandler(),
        ]
        self.default_handler = DefaultHandler()
        self.cfg = dict(handler=[])
        self.history = []
        for i in self.handlers:
            self.cfg[i.type()] = i

    def handle(self, inp: str) -> str:
        max_score = 0
        handler = None
        self.cfg['history'] = self.history
        for h in self.handlers:
            score = h.match(inp, self.cfg)
            # print(h.type(), score)
            if score >= max_score and score > 0:
                max_score = score
                handler = h
        if handler is None:
            self.history.append(self.default_handler.handle(inp, self.cfg))
        else:
            self.history.append(handler.handle(inp, self.cfg))
        return self.history[-1]

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


