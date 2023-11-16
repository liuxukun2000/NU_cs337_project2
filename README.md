# NU_cs337_project2
## Project description
The goals of Project 2 are to design and build a system that (i) parses online recipes into a useful data representation and (ii) features a (basic) conversational interface for user interaction.

Here's an illustrative user story comprising a set of user utterances and examples of suitable bot responses:

**USER STORY**

User: Walk me through a recipe from AllRecipes.com.

Bot: Sure. Please specify a URL.

User: https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/Links to an external site.

Bot: Alright. So let's start working with "Classic and Simple Meat Lasagna." What do you want to do?

[1] Go over ingredients list 

[2] Go over recipe steps.

User: 2.

Bot: The 1st step is: Preheat oven to 350 degrees F (175 degrees C).

User: How do I preheat the oven?

Bot: No worries. I found a reference for you: https://www.youtube.com/results?search_query=how+to+preheat+ovenLinks to an external site.

User: Thanks!

Bot: Should I continue to the 2nd step?

User: Show me the ingredients list.

Bot: Here are the ingredients for "Classic and Simple Meat Lasagna":

12 whole wheat lasagna noodles

1 pound lean ground beef

(...)

1 1/2 25 ounce jars tomato-basil pasta sauce

2 cups mozzarella cheese, shredded

User: (...)

</USER STORY>

## Parsing goals
Your group should build features to handle these goals related to parsing:

Accept the URL of a recipe from some recipe website, and programmatically fetch the page.
Some recipe-related websites to consider: seriouseats.comLinks to an external site., allrecipes.comLinks to an external site., epicurious.comLinks to an external site., bonappetit.comLinks to an external site., delish.comLinks to an external site., foodnetwork.comLinks to an external site., …
Your transformer should be able to handle any recipe from your chosen website – if you want to go above and beyond, build out a solution that can take inputs from multiple different websites! 
2. Parse it into the recipe data representation your group designs. Your parser should be able to recognize:

  Ingredients 
  Ingredient name
  Quantity
  Measurement (cup, teaspoon, pinch, etc.)
  (optional) Descriptor (e.g. fresh, extra-virgin)
  (optional) Preparation (e.g. finely chopped)
  Tools – pans, graters, whisks, etc.
  Methods 
Primary cooking method (e.g. sauté, broil, boil, poach, etc.)
(optional) Other cooking methods used (e.g. chop, grate, stir, shake, mince, crush, squeeze, etc.)
Steps – parse the directions into a series of steps that each consist of ingredients, tools, methods, and times


## Question answering goals
[WARNING FOR THIS NON-FINAL VERSION -- this list might get tweaked in the final version, but it's a good starting point regardless!]

Here are the types of user utterances that your conversational interface should support:

Recipe retrieval and display (see example above, including "Show me the ingredients list")
Navigation utterances ("Go back one step", "Go to the next step", "Repeat please", "Take me to the 1st step", "Take me to the n-th step")
Asking about the parameters of the current step ("How much of <ingredient> do I need?", "What temperature?", "How long do I <specific technique>?", "When is it done?")
Simple "what is" questions ("What is a <tool being mentioned>?")
Specific "how to" questions ("How do I <specific technique>?")
Vague "how to" questions ("How do I do that?" – use conversation history to infer what “that” refers to)
The typical solution for this project runs via terminal/console (i.e. using input in python) and that's perfectly fine. However, there's a number of extra credit opportunities available if you deploy your conversational interface in more advanced ways (more details in the “interface extra credit” section at the end of this document).

Some tips/guidelines about handling these different utterance types:

Some of these utterance types (type 2 [“go back one step”, “go to the next step”, “repeat please”] and type 6) rely on parts of the conversation history. So, make sure to store any useful conversation-related information.

 

Answering questions from types 4/5/6 requires external knowledge. Strategy for type 4 (simple “what is”) and type 5 (specific “how to”): since these have no conversation-related ambiguities to resolve, your response strategy is straightforward to implement. You should return either a Google or Youtube URL related to the user’s question (no logic required here, you can pick whichever you prefer). To build these URLs, replace the spaces in the user’s question (e.g. “how to preheat oven”) with +’s. Examples for both websites:

https://www.google.com/search?q=how+to+preheat+ovenLinks to an external site.
https://www.youtube.com/results?search_query=how+to+preheat+ovenLinks to an external site.
Type 6 (vague “how to”) is similar, but it first requires us to figure out what component from past utterances is being referenced. 

High-level project details
Your transformations should work on any given recipe from the website(s) you choose. Make sure to test using a wide variety of recipes. Some recipes will be harder than others to transform, and we will use a range of recipe complexity when grading.

Note that some of the things listed in the “parsing goals” section are designated as optional. A group that does a truly fantastic job on all of the steps listed above, but omits the optional items, will probably be in the running for an B+ to B. Optional items will bolster your grade, although doing all of the optional items and a lousy job on the core items is not recommended.

There are two deliverables for this assignment. First, you should submit a link to your group’s github repo for the project. Second, all groups must include a short video (maximum of 10 minutes) that outlines the features you developed for the project (did you tackle any optional features?) and includes demonstrations of your system on at least two recipes. 

Code-specific details
All code must be in Python 3. You can use any Python package or Python NLP toolkit, with one caveat. There are some python packages that would obviate most of the recipe parsing work for this project (e.g. python-allrecipes) – you are not allowed to use any package like this.
Please use the Python standard for imports described here: https://www.python.org/dev/peps/pep-0008/#imports (Links to an external site.)Links to an external site.
You must use a publicly accessible repository such as Github, and commit code regularly. When pair programming, note in the commit message those who were present and involved. We use these logs to verify complaints about AWOL teammates, and to avoid penalizing the entire group for one student’s violation of academic integrity. We don’t look at the commits unless there’s something really wrong with the code, or there’s a complaint.
If you use a DB, it must be Mongo DB, and you must provide the code you used to populate your database.
Your code must be runnable by the TAs. Thus, your repository must include a readme.txt file that lists the version of the programming language you used, and all dependencies. Any modules that are not part of the standard install of your programming language should be included in this list, along with information on the code repository from which it can be downloaded (e.g. for python, pip or easy_install). If you used code that you instead put in a file in your project’s working directory, then a copy of that file should be provided along with the code you wrote; the readme and/or comments in such files should clearly state that the code was not written by your team.
A note on plagiarism: GIT repos from this and previous years are accessible, being public. If you are tempted to look at them, be advised that the code in these repos is not necessarily of great quality. You wouldn’t want to copy from a past group who got a poor grade. Also note that it's easy to identify any copying from a past repo (plagiarism detectors are really good), and this would greatly affect your grade. 

Interface extra credit
For extra credit, you can improve the conversational interface in any of these three ways:

Implement your conversational interface with Rasa. Difficulty level: medium.
Connect your deployment to Facebook Messenger or Slack. Difficulty level: medium-to-hard.
Connect your deployment to Google Assistant or Amazon Alexa. Difficulty level: hard. 