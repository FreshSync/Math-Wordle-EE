import math

# Code to find all possible words with the input of a secific word and color pattern
# All set of words is limited compared to wordle.py


wordFile = open("new-words.txt", "r")
words = wordFile.read().splitlines()

pos = 0

letters = ""
colors = ""

count = 1

while count <= 5:
    letter = input("What is your " + str(count) + "th letter: ")
    color = input("What color is the " + str(count) +"st letter: ")
    letters = letters + letter
    colors = colors + color
    count += 1

for word in words:

    guess = letters # W_a__
    x = 0
    y = True

    final = ""

    for letter in guess:
        if letter == "_":
            final = final + "_"

        elif colors[x] == "g":
            if letter != word[x]:
                y = False

        elif colors[x] == "y":
            if letter not in word or letter == word[x]:
                y = False

        elif colors[x] == "b":
            if letter in word:
                y = False
        else:
            print("something went wrong")
            y = False

        x += 1
    
    if y == True:
            pos += 1
            print(word)

print("POSSILITIES: " + str(pos))

total = len(words)
prob = pos/total

print("PROBABILITY: " + str(prob))

info = math.log((1/prob), 2)

print("INFORMATION: " + str(info))
