# CS 337, Fall 2023, Project 2+3
## Group 9
### Eric Chen, Xukun Liu, Zafir Ansari

## Installation and Steup
Get the required packages through requirements.txt. 

## Demo
https://clipchamp.com/watch/o0lGQW5ezWr

## Run without GUI(Recommended)
run python main.py

## Run with GUI
Please download source code of our GUI from , If you are using windows, go target\release and run steam.exe. Next run server.py in this repo then you can start chat. 

This GUI can only run on windows, if you have any questions about this GUI you can send email to xukunliu2025@u.northwestern.edu.

## Main Features
This recipe parser takes URLs from allrecipes.com, delish.com, and bonappetit.com, parses the recipes and provides the user with an interactive chatbot. We have done relatively little testing for bonappetit.com, so results for this website may be worse than for the other two. 

For parsing, we used a mixture of string matching, regex, and navigating through dependency trees, and parts of speech. Please see step.py, substep.py, and ingredient.py for details. 

For the convenience of grading, there is the option to see the full parse, including all the variables we extracted from the steps. To see this, choose option 3 in the menu. Furthermore, there are still some features of the parser that we were unable to write handlers for. For example, we extracted the position of all of the ingredients within a step, and the steps that involve a particular ingredient. 

All of the required features were implemented and tested. For the types of questions it can answer, refer to the assignment document or the demo video. 

## Bonus
- [x] 1: A desktop GUI application written in React and Rust.
- [x] 2: Enable Text-to-Speech (TTS) in the GUI application.
- [x] 3: All the Option parts mentioned in the project description.
- [x] 4: Transformation: Chinese, Indian, Vegetarian, Vegan, Pescatarian, and Kosher.
