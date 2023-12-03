
PRIMARY_COOKING_ACTIONS = ['bake', 'steam', 'grill', 'roast', 'boil', 'fry', 'sear', 'baste', 'broil', 'poach', 'freeze', 'cure', 'saute', 'cook']

SECONDARY_COOKING_ACTIONS = ['pour', 'toast','topped','combine','chop', 'grate', 'serve','cut', 'shake', 'mince', 'stir', 'mix', 'crush', 'squeeze', 'beat', 'blend', 'caramelize', 'dice', 'dust',
                             'glaze', 'knead', 'pare', 'shred', 'toss', 'whip', 'sprinkle', 'grease', 'arrange', 'microwave', 'coat', 'turn', 'turning','preheat', "drizzle", "sprinkle", 'flip', 'melt',
                             'broil', 'marinate', 'brushing', 'slice', 'season', 'garnish','whisk', 'heat', 'drain', 'stirring', 'add', "remove", "return", "move", "place", "lay", "put"]

TEMPERATURE = ['degrees', 'degree', 'fahrenheit', 'celsius', 'f', 'c',"heat", "lukewarm", "warm", "hot", "boiling", "cool", "cold", "freezing", "room temperature", "room temp"]

COOKING_MEASUREMENTS = [
    'bunch', 'bunches', 'clove', 'cloves', 'coffeespoon', 'coffeespoons', 'cup', 'cups',
    'dash', 'dashes', 'dessertspoon', 'dessertspoons', 'drop', 'drops', 'fluid dram', 'fluid drams',
    'fluid ounce', 'fluid ounces', 'gallon', 'gallons', 'gill', 'gills', 'handful', 'handfuls',
    'ounce', 'ounces', 'piece', 'pieces', 'pinch', 'pinches', 'pint', 'pints', 'pound', 'pounds',
    'quart', 'quarts', 'saltspoon', 'saltspoons', 'slice', 'slices', 'smidgen', 'smidgens',
    'stalk', 'stalks', 'stick', 'sticks', 'tablespoon', 'tablespoons', 'teacup', 'teacups',
    'teaspoon', 'teaspoons', 'wineglass', 'wineglasses'
]

COOKING_TOOLS = ['aluminum foil', 'adjustable measuring cup', 'aluminum sheet pan', 'apple corer', 
'apple cutter', 'baking dish', 'baking parchment', 'balloon whisk', 'baster', 'beanpot', 
'biscuit cutter', 'biscuit press', 'blender', 'bottle opener', 'bowl', 'bread bin', 
'bread knife', 'broiler rack', 'broiler tray', 'browning tray', 'butter curler', 'cake and pie server', 
'can opener', 'cast-iron Dutch oven', 'cast-iron griddle', 'ceramic baking dish', 'ceramic saucepan', 
'cheese knife', 'cheesecloth', 'chefs knife', 'cherry pitter', 'chinoise', 'chip pan', 
'chopping/cutting board', 'citrus juicer', 'cleaver', 'clingfilm', 'colander', 'cookie sheet', 
'cooking pot', 'corkscrew', 'crepe pan', 'cutting board', 'cylinder', 'dish', 'double boiler', 
'doufeu', 'dough scraper', 'dutch oven', 'egg poacher', 'egg separator', 'egg slicer', 'egg timer', 
'electric pressure cooker', 'fillet knife', 'fish scaler', 'fish slice', 'flour sifter', 'food mill', 
'food processor', 'food scraper', 'food thermometer', 'fork', 'fryer', 'frying pan', 'funnel', 
'garlic press', 'glass food storage containers', 'grapefruit knife', 'grate', 'grater', 'gravy strainer', 
'griddle', 'grinder', 'hand mixer', 'immersion blender', 'instant-read thermometer', 'karahi', 'kettle', 
'kitchen foil', 'kitchen scales', 'kitchen shears/scissors', 'kitchen tool organizer', 'knife', 
'knife sharpening/honing rod', 'ladle', 'lame', 'lemon reamer', 'lemon squeezer', 'loaf pan', 'mandoline', 
'manual rotary grater', 'masher', 'mated colander pot', 'measuring cup', 'measuring jug', 'measuring spoon', 
'meat thermometer', 'melon baller', 'microwave', 'mixing bowl', 'mortar and pestle', 'muffin pan', 
'nonstick frying pan', 'nut milk bag', 'nutcracker', 'nutmeg grater', 'oven', 'oven glove', 'ovenproof dish', 
'pan', 'paring knife', 'pasta fork', 'pasta strainer', 'pastry bush', 'pastry wheel', 'peeler', 'pepper mill', 
'pizza cutter', 'plastic containers', 'plastic wrap', 'plastic zipper bags', 'pot', 'pot-holder', 'potato ricer', 
'pressure cooker', 'ramekin', 'roasting pan', 'roasting rack', 'roasting tin', 'rolling pin', 'salt shaker', 
'saucepan', 'saucepansauciersaute pan', 'saute pan', 'serrated knife', 'shallow glass dish', 'sharp knife', 
'sharpening steel', 'sieve', 'silicone pastry brush', 'silicone spatula', 'silicone tongs', 'skillet', 
'slotted spoon', 'slow cooker', 'souffle dish', 'spatula', 'spider', 'spiralizer', 'splayed saute pan', 
'spoon', 'springform pan', 'stainless steel baking sheet', 'stainless steel colander', 'stainless steel cooking spoon', 
'stainless steel frying pan', 'stainless steel spatula', 'steamer', 'stirring spoon', 'stockpot', 
'stovetop pressure cooker', 'strainer', 'tajine', 'tea infuser', 'tea towels', 'tenderizer', 'thermometer', 
'tin opener', 'tongs', 'tube panwok', 'vegetable knife', 'vegetable peeler', 'whisk', 'wonder pot', 
'wooden spoon', 'zester']

INGREDIENTS = {
    "eggs":
        [ "eggs", "egg", "whole eggs", "egg whites", "egg yolks", "liquid egg product", "dried egg whites",
    "dried egg yolks", "dried whole eggs", "frozen egg whites", "frozen egg yolks", 
    "scrambled egg mix", "egg powder", "egg substitutes"
    ],
        
    "milk_and_dairy":
        [
            "milk", "yogurt", "cream", "butter", "sour cream", "buttermilk", "ice cream", 
        "kefir", "heavy cream", "half and half", "whipped cream", "condensed milk", 
        "evaporated milk", "powdered milk", "clotted cream", "crème fraîche", "ghee"
        ],
        
    "cheese": 
        [
            "cheese", "american cheese", "asiago cheese", "blue cheese", "brocconcini", "brie cheese",
            "burrata cheese", "butterkäse", "cabrales", "camembert cheese", "cheddar cheese",
            "colby cheese", "cotija cheese", "cottage cheese", "cream cheese", "danish blue (danablu)",
            "edam", "emmental", "feta cheese", "fontina cheese", "goat cheese",
            "gorgonzola", "gouda", "grana padano", "gruyere", "halloumi",
            "havarti cheese", "hrudka", "jarlsberg", "manchego cheese", "mascarpone",
            "monterey jack", "mozzarella", "muenster cheese", "neufchâtel", "paneer",
            "parmesan", "parmigiano reggiano", "pecorino romano", "pepper jack", "processed cheese",
            "provolone cheese", "quark", "queso blanco", "queso fresco", "raclette",
            "ricotta cheese", "romano", "roquefort", "sakura", "sirene",
            "stilton", "string cheese", "swiss"
        ],
        
    "meat_and_poultry":
        [ 
        "beef", "pork", "chicken", "turkey", "lamb", "duck", "goose", "veal", 
        "rabbit", "quail", "pigeon", "venison", "buffalo", "boar", "bacon", 
        "ham", "sausage", "brisket", "rib", "steak", "ground beef", "ground pork", 
        "ground turkey", "ground chicken", "chicken breast", "chicken thighs", "chicken wings", 
        "chicken drumsticks", "pork chops", "pork loin", "pork belly", "lamb chops", 
        "lamb shank", "rack of lamb", "corned beef", "pastrami", "prosciutto", "salami", 
        "pepperoni", "chorizo", "biltong", "jerky", "hot dog", "frankfurter", "meatloaf", 
        "meatballs", "liver", "kidney", "heart", "tongue", "tripe", "oxtail"
    ],
        
    "seafood":
        [
            "salmon", "tuna", "trout", "mackerel", "sardines", "anchovies", "herring", "cod", 
            "haddock", "halibut", "flounder", "sole", "tilapia", "catfish", "bass", "carp", 
            "mahimahi", "swordfish", "shark", "eel", "pollock", "grouper", "red snapper", "barramundi", 
            "lobster", "crab", "shrimp", "prawns", "oysters", "clams", "mussels", "scallops", 
            "squid", "octopus", "cuttlefish", "jellyfish", "sea urchin", "caviar", "roe", 
            "crayfish", "langoustine", "periwinkle", "abalone", "conch", "sea cucumber", "king crab", 
            "snow crab", "soft shell crab", "blue crab", "dungeness crab", "rock shrimp", "bay scallops", 
            "sea scallops", "cockles", "geoduck", "razor clams", "welk"
        ],
        
    "kosher_meat":
        [
                'beef', 'chicken', 'turkey', 'lamb', 'duck', 'goose', 'veal',
                'quail', 'pigeon', 'venison', 'buffalo', 'sausage', 'brisket',
                'rib', 'steak', 'ground beef', 'ground pork', 'ground turkey',
                'ground chicken', 'chicken breast', 'chicken thighs', 'chicken wings',
                'chicken drumsticks', 'lamb chops', 'lamb shank', 'rack of lamb',
                'corned beef', 'pastrami', 'prosciutto', 'salami', 'pepperoni',
                'chorizo', 'biltong', 'jerky', 'hot dog', 'frankfurter', 'meatloaf',
                'meatballs', 'liver', 'kidney', 'heart', 'tongue', 'tripe', 'oxtail',
                'salmon', 'tuna', 'trout', 'mackerel', 'sardines', 'anchovies', 'herring',
                'cod', 'haddock', 'halibut', 'flounder', 'sole', 'tilapia', 'catfish',
                'bass', 'carp', 'mahimahi', 'pollock', 'grouper', 'red snapper', 'barramundi',
                'caviar', 'roe'
        ],
        
    "nuts_and_seeds":
        [
            "almonds", "cashews", "pistachios", "walnuts", "pecans", "macadamia nuts", "pine nuts", 
            "peanuts", "hazelnuts", "chestnuts", "sesame seeds", "pumpkin seeds", "sunflower seeds", 
            "flax seeds", "chia seeds", "poppy seeds", "hemp seeds", "nut butter", "tahini", "nutella"
        ],
    
    "fruits":
        [
            "apple", "apricot", "avocado", "banana", "blackberry", "blueberry", "boysenberry", 
            "cherry", "coconut", "cranberry", "date", "dragonfruit", "durian", "fig", "gooseberry", 
            "grape", "grapefruit", "guava", "honeydew", "jackfruit", "kiwi", "kumquat", "lemon", 
            "lime", "lychee", "mango", "melon", "cantaloupe", "honeydew", "watermelon", "nectarine", 
            "orange", "clementine", "mandarin", "tangerine", "papaya", "passion fruit", "peach", 
            "pear", "persimmon", "pineapple", "plantain", "plum", "pluot", "pomegranate", "pomelo", 
            "prickly pear", "quince", "raspberry", "star fruit", "strawberry"
        ],
        
    "vegetables": [
        "carrot", "potato", "tomato", "onion", "garlic", "broccoli", "cauliflower", "spinach", 
        "lettuce", "cucumber", "bell pepper", "mushroom", "zucchini", "squash", "pumpkin", "eggplant",
        "corn", "green beans", "peas", "asparagus", "leek", "celery", "beetroot", "radish", 
        "sweet potato", "turnip", "parsnip", "yam", "kale", "cabbage", "brussels sprouts", "artichoke", 
        "bok choy", "arugula", "watercress", "endive", "chard", "collard greens", "okra", "rutabaga", 
        "fennel", "shallot", "scallion", "chili pepper", "jalapeno", "habanero", "poblano", "anaheim pepper",
        "butternut squash", "acorn squash", "kohlrabi", "daikon", "horseradish", "bamboo shoots", "rhubarb", 
        "ginger", "turmeric", "jicama", "water chestnut", "hearts of palm", "sunchoke", "rapini", "radicchio"
    ],
    
    "herbs_and_spices": [
        "basil", "oregano", "thyme", "rosemary", "sage", "parsley", "cilantro", "dill", 
        "mint", "chives", "tarragon", "bay leaves", "lemongrass", "coriander", "cumin", 
        "paprika", "turmeric", "saffron", "fennel", "cinnamon", "star anise", "cloves", 
        "nutmeg", "allspice", "cardamom", "ginger", "garlic", "garlic powder", "onion powder", 
        "chili powder", "cayenne pepper", "black pepper", "white pepper", "red pepper flakes", 
        "mustard seeds", "fenugreek", "sumac", "za'atar", "harissa", "garam masala", "curry powder", 
        "anise", "caraway seeds", "juniper berries", "marjoram", "asafoetida", "lavender", 
        "kaffir lime leaves", "vanilla", "masala", "berbere", "ras el hanout", "ajwain", 
        "bayberry", "chervil", "lovage", "sichuan pepper", "tamarind", "wasabi", "horseradish", 
        "mace", "annatto", "arrowroot", "galangal", "grains of paradise", "lemon balm", 
        "lemon verbena", "licorice root", "savory", "spearmint", "valerian", "verbena", 
        "wintergreen", "green onion", "five-spice powder", "hoisin sauce", "soy sauce", 
        "fish sauce", "oyster sauce", "Thai basil", "holy basil", "dried shrimp", "palm sugar",
        "kaffir lime", "galangal", "Thai chilies"
    ],
    
    "sauces": [
        "ketchup", "mustard", "mayonnaise", "barbecue sauce", "hot sauce", "soy sauce", 
        "teriyaki sauce", "sriracha", "hollandaise", "béarnaise", "alfredo sauce", "marinara sauce",
        "pesto", "tartar sauce", "chimichurri", "aioli", "hoisin sauce", "fish sauce", "oyster sauce", 
        "salsa", "guacamole", "tzatziki", "ranch dressing", "caesar dressing", "vinaigrette", 
        "bolognese sauce", "carbonara sauce", "buffalo sauce", "worcestershire sauce", "ponzu sauce", 
        "thai peanut sauce", "mole sauce", "sambal", "harissa", "chutney", "curry sauce", 
        "satay sauce", "gravy", "demi-glace", "bechamel sauce", "veloute sauce", "espelette pepper sauce", 
        "romesco sauce", "gremolata", "remoulade", "szechuan sauce", "duck sauce", "sweet and sour sauce", 
        "plum sauce", "tahini sauce", "tzatziki", "kimchi", "gochujang", "xo sauce", "vinegar"
    ],
    
    "carbs": [
        "rice", "quinoa", "bread", "flour", "pasta", "noodles", "couscous", "barley", 
        "oats", "corn", "cornmeal", "polenta", "potatoes", "sweet potatoes", "yams", 
        "beans", "lentils", "chickpeas", "peas", "tortillas", "bagels", "pita bread", 
        "rye bread", "sourdough bread", "whole wheat bread", "muffins", "pancakes", 
        "waffles", "crackers", "biscuits", "croissants", "granola", "muesli", "buckwheat", 
        "bulgur", "farro", "millet", "amaranth", "soba noodles", "udon noodles", "ramen", 
        "rice noodles", "spaghetti", "macaroni", "fettuccine", "penne", "lasagna", "gnocchi", 
        "dumplings", "popcorn", "pretzels", "tapioca", "rice cakes", "matzo", "cornbread", 
        "scones", "baguette", "ciabatta", "naan", "focaccia", "pizza dough", "rye", "teff", 
        "tagliatelle", "linguine", "rigatoni", "orzo", "vermicelli", "angel hair", "pappardelle", 
        "rotini", "ziti", "cavatappi", "tortellini", "ravioli", "cannelloni", "farfalle"
    ],
    
    "oils": [
        "vegetable oil", "olive oil", "coconut oil", "sesame oil", "canola oil", "peanut oil", 
        "sunflower oil", "corn oil", "grapeseed oil", "avocado oil", "walnut oil", "almond oil", 
        "hazelnut oil", "palm oil", "soybean oil", "flaxseed oil", "pumpkin seed oil", "safflower oil", 
        "truffle oil", "rice bran oil", "cottonseed oil", "mustard oil", "macadamia oil", "pistachio oil"
    ],
    
    "sweeteners": [
        "sugar", "honey", "maple syrup", "agave nectar", "molasses", "corn syrup", "coconut sugar", 
        "brown sugar", "confectioners sugar", "stevia", "sucralose", "aspartame", "saccharin", 
        "sucrose", "sorbitol", "xylitol", "erythritol", "monk fruit", "date sugar", "barley malt syrup", 
        "brown rice syrup", "cane sugar", "caramel", "carob syrup", "evaporated cane juice", "fructose", 
        "fruit juice concentrate", "glucose", "high fructose corn syrup", "invert sugar", "lactose", 
        "maltodextrin", "maltose", "mannitol", "refiner's syrup", "treacle", "turbinado sugar"
    ],
    
    "vegan_protein": [
        "tofu", "tempeh", "seitan", "portabello mushroom"
    ],
    
    "vegan_egg": ["flaxseed", "chia seed", "applesauce", "mashed banana", "silken tofu",
        "vinegar and baking soda", "aquafaba", "commercial egg replacers",
        "vegan yogurt or buttermilk", "arrowroot powder", "nut butter"
    ],
    
    "vegan_milk": [
        "almond milk", "soy milk", "oat milk", "coconut milk", "rice milk", "cashew milk", "hemp milk"
    ],
    
    "vegan_yogurt": [
        "soy yogurt", "coconut yogurt", "almond yogurt", "cashew yogurt"
    ],
    
    "vegan_cream": [
        "coconut cream", "cashew cream", "soy cream"
    ],
    
    "vegan_cheese": [
        "nutritional yeast", "vegan cheese", "vegan parmesan", "vegan mozzarella", "vegan cheddar"
    ],
    
    "vegan_butter": [
        "vegan butter", "vegan margarine", "coconut oil"
    ],
    
    "pareve_proteins": [
    "tofu", "tempeh", "seitan", "lentils", "chickpeas", "beans", "quinoa", 
    "nuts", "seeds", "edamame", "peas", "textured vegetable protein", "soy protein", 
    "mushrooms", "eggplant", "green beans", "almonds", "walnuts", "cashews", 
    "sunflower seeds", "pumpkin seeds", "hemp seeds", "chia seeds", "flaxseeds", 
    "spirulina", "nutritional yeast", "soy nuts", "soy milk", "almond milk", 
    "rice milk", "hemp milk", "oat milk", "pea protein",
    "salmon", "tuna", "trout", "cod", "haddock", "halibut", "flounder", "tilapia",
    "carp", "mackerel", "snapper", "sardines", "bass"
    ], 
    
    "south_asian_spices": [
        "cumin seeds", "coriander seeds", "turmeric", "garam masala", "cardamom pods", 
        "cinnamon sticks", "cloves", "mustard seeds", "fenugreek seeds", "asafoetida (hing)", 
        "black pepper", "green cardamom", "black cardamom", "nutmeg", "mace", 
        "bay leaves", "saffron", "fennel seeds", "star anise", "red chili powder", 
        "kashmiri chili powder", "amchur (dried mango powder)", "tamarind", "ajwain (carom seeds)", 
        "pomegranate seeds (anardana)", "kalonji (nigella seeds)", "sichuan pepper", "curry leaves", 
        "kaffir lime leaves", "dried red chilies", "white pepper", "black salt (kala namak)", 
        "chaat masala", "kasuri methi (dried fenugreek leaves)"
    ],
    
    "south_asian_sauces": [
        "tamarind chutney", "mint chutney", "coriander chutney", "raita", "tomato chutney", 
        "coconut chutney", "mango chutney", "yogurt sauce", "korma sauce", "masala sauce", 
        "vindaloo sauce", "rogan josh sauce", "tikka masala sauce", "makhani sauce", "kadai sauce", 
        "saag sauce", "dal makhani sauce", "achari sauce", "biryani sauce", "goan curry sauce",
        "pickle (achar)", "ghee", "curry paste"
    ],
    
    "south_asian_protein": [
        "chicken", "mutton", "lamb", "ilish", "rohu", "bhakura", "shrimp", "lentils", "chickpeas", "paneer", "yogurt", "tofu"
    ],
    
    "south_asian_vegetable": [
        "potato", "onion", "garlic", "ginger", "tomato", "cauliflower", "eggplant (brinjal)",
        "spinach", "okra (bhindi)", "cabbage", "peas", "carrot", "bell pepper (capsicum)",
        "green beans", "bitter gourd (karela)", "bottle gourd (lauki)", "ridge gourd (turai)",
        "pumpkin", "fenugreek leaves (methi)", "radish", "cucumber", "beetroot",
        "turnip", "sweet potato", "chilli pepper", "mustard greens (sarson)", "amla", "yam",
        "taro root (arbi)", "plantain", "ivy gourd (tindora)", "cluster beans (gavar)", "colocasia leaves"
        ], 
    
    "south_asian_carb": [
        "basmati rice", "roti", "naan", "chapati", "paratha", "puri", "dosa", "idli", "upma", "poha", "sevai", "biryani", "pulao"
    ],
    
    "south_asian_dairy": [
        "ghee", "yogurt", "paneer"
    ],
    
    "keto_carb_substitute:":[
        "almond flour", "cauliflower rice", "zucchini noodles"
    ],
    
    "keto_sweetener": [
        "stevia", "erythritol", "xylitol"
    ],
    
    "chinese_carb":[
        "jasmine rice", "rice noodle roll", "ho fun", "noodles", "vermicelli", "egg noodles", "wonton wrappers", "dumpling wrappers", "bao"
    ],
    
    "chinese_spices": [
        "five-spice powder", "star anise", "sichuan peppercorns", "cinnamon", "cloves", 
    "fennel seeds", "ginger", "garlic", "green onion", "dried chili peppers", "black pepper", 
    "white pepper", "cumin", "coriander", "cardamom", "turmeric", "nutmeg", 
    "bay leaves", "sesame seeds", "dried orange peel", "fenugreek", "anise", 
    "licorice root", "galangal", "lemongrass", "black cardamom", "red yeast rice", "star anise",
    ], 
    
    "chinese_sauce":[
        "soy sauce", "hoisin sauce", "oyster sauce", "fish sauce", "sesame oil", 
    "rice vinegar", "black vinegar", "chili oil", "chili sauce", "bean paste", 
    "doubanjiang (spicy bean paste)", "tianmianjiang (sweet bean sauce)", "plum sauce", 
    "sweet and sour sauce", "xo sauce", "light soy sauce", "dark soy sauce", 
    "shaoxing wine", "rice wine", "fermented black bean sauce", "chinese mustard", 
    "szechuan sauce", "garlic sauce", "ginger sauce"
    ], 
    
    "chinese_vegetable": [
        "bok choy", "napa cabbage", "chinese broccoli (gai lan)", "chinese eggplant", 
    "chinese spinach", "snow peas", "water chestnuts", "bamboo shoots", "lotus root", 
    "bean sprouts", "mung bean sprouts", "shiitake mushrooms", "wood ear mushrooms", 
    "enoki mushrooms", "bitter melon", "daikon radish", "chinese long beans", 
    "chinese chives", "garlic scapes", "chinese mustard greens", "yu choy", 
    "baby bok choy", "taro", "edamame", "ginger", "garlic", "green onion (scallion)", 
    "chinese yam", "jicama", "water spinach", "pea shoots", "chinese okra (silk gourd)", 
    "radish", "tomato", "cucumber", "bell pepper", "hot peppers", "zucchini"
    ]
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}


# some cooking methods and tool names were derived from this source: https://github.com/amitadate/EECS-337-NLP-Project-02/blob/master/Final_Submission/PreProcessing/extracter_list.py