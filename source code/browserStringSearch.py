import webbrowser
import os


input_word = input("Enter the word you want to search: ")
url = "https://www.google.com/search?q=define+ENTER_WORD_HERE"
url = url.replace("ENTER_WORD_HERE", input_word)

# Open the URL in the default web browser
webbrowser.open(url)

# Alternatively, you can open the URL in a new Chrome window using the following line
# os.system('google-chrome {}'.format(url))

print("Searching for the meaning of Python on Google...")