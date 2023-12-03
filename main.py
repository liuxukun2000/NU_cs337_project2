from handler.manager import HandlerManager
from scrapper.allrecipes import AllrecipesSpider
from scrapper.delish import DelishSpider
from utils.ingredient import RecipeIngredient

if __name__ == "__main__":
    # HandlerManager().run()
    x = DelishSpider.get("https://www.delish.com/holiday-recipes/thanksgiving/a29178578/how-to-dry-brine-turkey-recipe/")
    for i in x.steps:
        print(i)