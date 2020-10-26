import json
from difflib import get_close_matches

data = json.load(open("data.json", "r+"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no ")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            word_not_found(word)
        else:
            return("You have entered wrong input please enter just y or n ")
    else:
        word_not_found(word)
def word_not_found(word):
    qs = input("Can you help me find the meaning? Type y for Yes: ")
    if(qs == 'y'):
        meaning = input("Please enter the meaning of "+word+" here: ")
        temp_dict = {word:meaning}
        with open("data.json", "r+") as file:
            data = json.load(file)
            data.update(temp_dict)
            file.seek(0)
            json.dump(data, file)
        print("Dictionary updated! Thank you for your contribution")
more = 'y'
while(more == 'y'):
    word = input("Enter the word you want to search: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    elif output == None:
        pass
    else:
        print(output)
    more = input("Do you want to continue? type y for Yes: ")
