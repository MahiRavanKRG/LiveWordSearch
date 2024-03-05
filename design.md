# "Every line of code and every train of thought contributes to software design"

#### Problem: 
I want to know the meaning of the word that I am seeing/typing on monkey type.

#### Digest: 
It is hard to differentiate between words I know and words I don't know. So, let's make a program that listens to the keyboard and searches all the typed works. A simple program, just run it using the cmd line and it will keep showing me the words that I am typing.

## Plan to solve the problem
1. Learn to listen to a word from the keyboard
2. Search on the internet for whatever you get
3. From my current understanding you can now use the Chrome tab to search for a specific "string" using code. 
4. Now, shift from Chrome to pure CMD line interface, you should type a word and your code should reply with the word's meaning. Use the internet for now, for the future this can be made offline for all major meanings, I imagine having one dictionary can make this app offline.
5. Now, our logic is ready, if your app can listen to the keyboard live and reply with a word meaning every spacebar then your prototype is ready, finish it into a proper product, and then put it onto the internet.

## Updates 

This branch purpose has been completed up until now. Working logic has been completed and currently working on the **GUI-Branch**. 

## Design

I don't have to cover Design in detail as only app1.py is the complete application, it has been refined from RefinedBasicLogicWithoutInternet.py and has everything it needs to run. Other files are just testing files that I learned from and made tests on. 
> Yet I am writing some lines on each file.

##### app1.py
This is the functional component of the current branch. This is derived from the file RefinedBasicLogicWithoutInternet.py
> has the current logic made into a deployable piece of code.

##### basicLogic.py
This is the first and implements the functionality of searching the word on internet.
> was used as the proof of concept for the Idea, 
> Implements the logic of how to use python to solve the problem stated

##### design.md
THIS FILE
> Provides detailed information about 
> 1. this branch
> 2. its status
> 3. design desicions 
> 4. file structure 
> 5. thought process of me :)

##### dictionary.py
This file is for learning about PIdictionary and its uses

##### README.md
Provides information about this branch and its status at a glance

##### RefinedBasicLogicWithoutInternet.py
This file is derived from "basicLogic.py" file and implements the thought-process/algorithm on offline-ish manner it uses pictionoary python package to make the whole solution local and independent of internet.
> This changes certain lines of code to make the word search offline.