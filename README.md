## LiveWordSearch - Graphics Branch
### This branch focuses on the Graphics used in this project only.

This project is quiet simple, whenever running this project will listen to your current keyboard inputs, whenever your spacebar whatever sequece of words you have typed will be considered one word and will be searched on the internet.

Thought-Process/Algorithm
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
5. Job of graphics part starts Exclusively from here, The data needs to be represented in a way that doesnot distrub the main focus of Monkey type which is typing
> I think converting it into a crome extention will suffice my work for now, the answers can be shown at the belly of typing screen. Out of the way but near the focus, in a 'Drak Mode' manner, black background without border and white low contrast text. Box just big enough for a couple of lines to be read.

## Contents
This branch is rather Empty, as We don't need all the files here only the ones that I need to make the GUI better.

### Result
Currently Exploreing to make the UI richer by giving it a more useful make over.
This has been successfully converted into a command-line Interface like application, that works 100% offline. However, its full of bugs and barely reliable. This works so Currently I should focus on GUI [GUI-BRANCH].