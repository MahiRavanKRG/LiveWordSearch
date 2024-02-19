import PyDictionary

# Create an instance of PyDictionary
dictionary = PyDictionary.PyDictionary()
# Get the meaning of a word
word = "erotic"

def get_meaning(word):
    meaning = dictionary.meaning(word)
    return meaning['Noun']

print(get_meaning(word))