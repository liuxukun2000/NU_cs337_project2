import re

from handler.base import BaseHandler
from spider.allrecipes import AllrecipesSpider


class SelectWebHandler(BaseHandler):
    def __init__(self):
        spiders = [AllrecipesSpider]
        self.spider = None
        self.spiders = {spider.name(): spider for spider in spiders}

    @staticmethod
    def type() -> str:
        return "select_web"

    def match(self, inp: str, _cfg) -> int:
        ans = [
            i for i, j in self.spiders.items() if i in inp.lower()
        ]
        return int('from ' in inp.lower()) + int(ans != [])


    def handle(self, inp: str, cfg) -> str:
        ans = [
            i for i, j in self.spiders.items() if i in inp.lower()
        ]
        if not ans:
            return "Sorry, I don't support this website."
        if len(ans) > 1:
            return "Sorry, I don't support multiple websites."
        cfg['handler'].append(self)
        self.spider = self.spiders[ans[0]]
        return f"Sure. I will use {ans[0]}. Please specify a URL."