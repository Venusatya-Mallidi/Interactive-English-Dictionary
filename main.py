import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Do you mean %s instead? type Y for yes N for no: ")
        if yn == 'Y':
            close_match = get_close_matches(word, data.keys())
            if close_match:
                return data[close_match[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."
    
user_input = input("Enter the word: ")

output = translate(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)