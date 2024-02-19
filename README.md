## LiveWordSearch - Logic Branch
### This branch focuses on the Logic used in this project only.

This project is quiet simple, whenever running this project will listen to your current keyboard inputs, whenever your spacebar whatever sequece of words you have typed will be considered one word and will be searched on the internet.

Thought Process
1. Listen to the keyboard keys pressed
2. Make the inputs into a word
3. Search the defination of this word
> this can be done in multiple ways
> 1. use google ➡️ basicLogic.py
>> This is hard as I am confused on how to extract precise data from the search, but bare minimum has been achieved.
> 2. offline search ➡️ basicLogicWithoutInternet.py
>> The problem faced here if different I have used PyDictionary as word dictionay, a different model/library might generate better redsults.
4. Relay the answer back to the Graphical Unit for the user
> Currently uses command line as the GUI

### Result
This has been successfully converted into a command-line Interface like application, that works 100% offline. However, its full of bugs and barely reliable. This works so Currently I should focus on GUI