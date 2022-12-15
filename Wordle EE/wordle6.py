import itertools
import math
import matplotlib.pyplot as plt
import statistics

# Information and probability for every single word, but in python


x = ["🟩", "🟨", "⬜"]

permu = [p for p in itertools.product(x, repeat=5)]

allWordInfo = []


wordFile = open("valid-wordle-words.txt", "r")
words = wordFile.read().splitlines()

allWordFile = open("test-words.txt", "r")
allWords = allWordFile.read().splitlines()

class wordSet:
    def __init__(self, permut, probab):
        permWord = ""
        for i in permut:
            permWord = permWord + i
        self.colorWord = permWord
        self.info = math.log((1/probab), 2)
        self.probab = probab

    def __repr__(self):
        return '{' + str(self.colorWord) + "," + str(self.probab) + ', ' + str(self.info) + '}'

class wordDataSet:
    def __init__(self, wordD, probD, infoD, colorD):
        self.wordData = wordD
        self.probData = probD
        self.infoData = infoD
        self.colorData = colorD

    def __repr__(self):
        return '{' + str(self.wordData) + "," + str(self.probData) + ', ' + str(self.infoData) + "," + str(self.colorData) + '}'


for eachWord in allWords:

    letters = eachWord

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

    m = 0

        # print("INFORMATION: " + str(info))

    meanProb = statistics.mean(probGraph)
    meanInfo = statistics.mean(infoGraph)
    probColor = colorGraph[-1]

    wordInfo = wordDataSet(letters, meanProb, meanInfo, probColor)
    allWordInfo.append(wordInfo)

allWordInfo.sort(key=lambda w: w.probData)

print(allWordInfo)

