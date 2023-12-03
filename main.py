from handler.manager import HandlerManager
from scrapper.allrecipes import AllrecipesSpider
from scrapper.delish import DelishSpider
from utils.ingredient import RecipeIngredient

if __name__ == "__main__":
    # HandlerManager().run()
    x = DelishSpider.get("https://www.delish.com/cooking/recipe-ideas/a20089643/easy-stuffed-mushroom-recipe/")
    print(x)
    # for i in x.steps:
    #     print(i)