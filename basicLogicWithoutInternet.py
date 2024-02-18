import webbrowser
import keyboard
import PyDictionary

# for some reason I cannot declare variables, I have to make them in the defination of the function
def on_key_release(event, input_string=[]):  # the event is used to handle the key press event, input_string is used to store the input characters as a list
    if event.name == "space": # as per the pllaned functionality, space will trigger search
        passing_string = ''.join(input_string) # joining the list of characters to form a string
        input_string.clear() # clearing the list for the next input
        print(f"The input sting is {passing_string} \nLooking on PyDictionary...") # CMD evidence of the input string
        dictionary = PyDictionary.PyDictionary()
        print(dictionary.meaning(passing_string)['Noun'])
    elif event.name in ["esc", "alt", "ctrl", "shift", "enter", "tab", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]: # keeps the input_string unpolluted
        pass

    else:    
        input_string += str(event.name) # adding the input character to the list
        print(f"Key {event.name} released") # CMD evidence of the key press



while True:
    keyboard.on_release(on_key_release) # calling the function whenever a key is released
    keyboard.wait("esc") # esc to exit the program
    
    exit(0)