import itertools
import math
import matplotlib.pyplot as plt

# Graph of all color patterns of a word and the info to probability ratio for the word

x = ["🟩", "🟨", "⬜"]

permu = [p for p in itertools.product(x, repeat=5)]


wordFile = open("valid-wordle-words.txt", "r")
words = wordFile.read().splitlines()

class wordSet:
    def __init__(self, permut, probab):
        permWord = ""
        for i in permut:
            permWord = permWord + i
        self.colorWord = permWord
        self.info = math.log((1/probab), 2)
        self.probab = probab

    def __repr__(self):
        return '{' + self.colorWord + ', ' + str(self.probab) + ', ' + str(self.info) + '}'



letters = input("What is the word: ")

wordClassList = []

colorGraph = []
probGraph = []
infoGraph = []

for perm in permu:
    
    colors = perm
    pos = 0
    prob = 0
    info = 0

    for word in words:

        guess = letters # W_a__
        x = 0
        y = True

        final = ""

        for letter in guess:
            if letter == "_":
                final = final + "_"

            elif colors[x] == "🟩":
                if letter != word[x]:
                    y = False

            elif colors[x] == "🟨":
                if letter not in word or letter == word[x]:
                    y = False

            elif colors[x] == "⬜":
                if letter in word:
                    y = False
            else:
                print("something went wrong")
                y = False

            x += 1
        
        if y == True:
                pos += 1
                

    # print("POSSILITIES: " + str(pos))

    total = len(words)
    prob = pos/total

    # print("PROBABILITY: " + str(prob))

    if prob != 0:
        wordClass = wordSet(perm, prob)
        wordClassList.append(wordClass)

wordClassList.sort(key=lambda z: z.probab)

for obj in wordClassList:
    colorGraph.append(obj.colorWord)
    probGraph.append(obj.probab)
    infoGraph.append(obj.info)


plt.plot(infoGraph, probGraph)
plt.title('Info Vs Probability')
plt.xlabel('Info')
plt.ylabel('Probability')
plt.show()

plt.bar(colorGraph, probGraph)
plt.title('Combination Vs Probability')
plt.xlabel('Combination')
plt.ylabel('Probability')
plt.show()

    # print("INFORMATION: " + str(info))
