import re
from copy import deepcopy
from typing import List

from handler.base import BaseHandler
from handler.select_web import SelectWebHandler


def find_url(inp: str) -> List[str]:
    regex = r'https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z0-9/-]+'
    return re.findall(regex, inp)


class GetRecipeHandler(BaseHandler):
    def __init__(self):
        self.recipe = None
        self.ori_recipe = None
        self.url = None

    @staticmethod
    def type() -> str:
        return "get_recipe"

    def match(self, inp: str, cfg) -> int:
        if not find_url(inp):
            return 0
        return 3

    def handle(self, inp: str, cfg) -> str:
        if SelectWebHandler().handle(inp, cfg).startswith("Sorry"):
            return "It seems that I don't support this website. Please try another one."
        select_handler = [handler for handler in cfg['handler'] if handler.type() == "select_web"]
        if not select_handler:
            return "It seems that I don't support this website. Please try another one."
        select_handler = cfg['handler'][-1]
        spider = select_handler.spider
        url = find_url(inp)
        if len(url) > 1:
            return "Sorry, I don't support multiple URLs."
        self.url = url[0]
        try:
            self.recipe = spider.get(self.url)
            self.ori_recipe = deepcopy(self.recipe)
        except Exception as e:
            return f"Sorry, I cannot get this recipe."
        cfg['handler'].append(self)
        return f"Alright. So let's start working with **{self.recipe.title}**.\nWhat do you want to do?" \
            + "\n\n[1]. **Get the ingredients.**\n\n[2]. **Get the steps.**\n\n[3]. **Get the whole recipe.**\n\n[4]. **Start over.**"

    def clear(self):
        self.recipe = None


