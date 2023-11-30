from handler.manager import HandlerManager
from scrapper.allrecipes import AllrecipesSpider
from utils.ingredient import RecipeIngredient

if __name__ == "__main__":
    # HandlerManager().run()
    x = AllrecipesSpider.get("https://www.allrecipes.com/recipe/230904/hearty-barley-turkey-soup/")
    for i in x.ingredients:
        print(i)
        print(RecipeIngredient.from_string(i))