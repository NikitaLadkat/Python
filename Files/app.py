import json


data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        print("No word found...")



word = input("Enter the word : ")

print(translate(word))
