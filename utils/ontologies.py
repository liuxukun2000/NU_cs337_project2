
PRIMARY_COOKING_METHODS = ['bake', 'steam', 'grill', 'roast', 'boil', 'fry', 'barbeque', 'baste', 'broil', 'poach', 'freeze', 'cure', 'saute', 'cook']

SECONDARY_COOKING_METHODS = ['pour', 'toast','topped','combine','chop', 'grate', 'serve','cut', 'shake', 'mince', 'stir', 'mix', 'crush', 'squeeze', 'beat', 'blend', 'caramelize', 'dice', 'dust',
                             'glaze', 'knead', 'pare', 'shred', 'toss', 'whip', 'sprinkle', 'grease', 'arrange', 'microwave', 'coat', 'turning','preheat', 
                             'broil', 'marinate', 'brushing', 'slice', 'season', 'whisk', 'heat', 'drain', 'stirring']


COOKING_MEASUREMENTS = [
    "bunch",
    "cloves",
    "coffeespoon",
    "cup",
    "dash",
    "dessertspoon",
    "drop",
    "fluid dram",
    "fluid ounce",
    "gallon",
    "gill",
    "handful",
    "ounce",
    "piece",
    "pinch",
    "pint",
    "pound",
    "quart",
    "saltspoon",
    "slice",
    "smidgen",
    "stalk",
    "stick",
    "tablespoon",
    "teacup",
    "teaspoon",
    "wineglass"
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
    "eggs_and_dairy":
        ["eggs", "milk", "butter", "cheese", "yogurt", "cream", "sour cream", "buttermilk", 
    "cottage cheese", "cream cheese", "ghee", "kefir", "ricotta", "whey", "skim milk", 
    "whole milk", "condensed milk", "evaporated milk", "powdered milk", "egg whites", 
    "egg yolks", "hard-boiled eggs", "scrambled eggs", "omelette", "feta", "mozzarella", 
    "parmesan", "cheddar", "swiss cheese", "blue cheese", "brie", "camembert", "gouda", 
    "goat cheese", "monterey jack", "colby", "provolone", "asiago", "mascarpone", "paneer",
    "halloumi", "stilton", "quark", "manchego", "edam", "emmental", "gorgonzola", 
    "havarti", "pecorino", "roquefort", "taleggio", "vacherin"
    ],
        
    "meat_and_poultry":
        [
        "eggs", "milk", "butter", "cheese", "yogurt", "cream", "sour cream", "buttermilk", 
        "cottage cheese", "cream cheese", "ghee", "kefir", "ricotta", "whey", "skim milk", 
        "whole milk", "condensed milk", "evaporated milk", "powdered milk", "egg whites", 
        "egg yolks", "hard-boiled eggs", "scrambled eggs", "omelette", "feta", "mozzarella", 
        "parmesan", "cheddar", "swiss cheese", "blue cheese", "brie", "camembert", "gouda", 
        "goat cheese", "monterey jack", "colby", "provolone", "asiago", "mascarpone", "paneer",
        "halloumi", "stilton", "quark", "manchego", "edam", "emmental", "gorgonzola", 
        "havarti", "pecorino", "roquefort", "taleggio", "vacherin"
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
        
    "nuts and seeds":
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
    
    "herbs and spices": [
        
    ]
}


# some cooking methods and tool names were derived from this source: https://github.com/amitadate/EECS-337-NLP-Project-02/blob/master/Final_Submission/PreProcessing/extracter_list.py