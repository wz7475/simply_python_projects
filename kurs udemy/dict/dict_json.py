import json
data = json.load(open("dict\\data.json"))

from difflib import get_close_matches


def search_word(word):
    try:
        try:
            definition = data[word.lower()]
        except KeyError:
            try:
                definition = data[word.title()]
            except KeyError:
                definition = data[word.upper()]
        counter = 1
        if len(definition) >= 2:
            for i in definition:
                print(str(counter), "-", i)
                counter += 1
        else:
            for i in definition:
                print(i)
    except KeyError:
        suggestion = get_close_matches(word, data)
        print("You've entered non-existing in dictionary word, try again.")
        print("Did you mean: {}".format(suggestion))



while(True):
    phrase = input("Enter an english word: ")
    search_word(phrase)

