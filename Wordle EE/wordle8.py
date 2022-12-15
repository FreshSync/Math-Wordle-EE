from email import iterators
import itertools
import math
import statistics
import pandas as pd
from tqdm import tqdm

# Information, probability and entropy of every single word in google sheets
# With loading bar


x = ["🟩", "🟨", "⬜"]

permu = [p for p in itertools.product(x, repeat=5)]

allWordInfo = []


wordFile = open("valid-wordle-words.txt", "r")
words = wordFile.read().splitlines()
 

class wordSet:
    def __init__(self, permut, probab):
        permWord = ""
        for sq in permut:
            permWord = permWord + sq
        self.colorWord = permWord
        self.info = math.log((1/probab), 2)
        self.probab = probab

    def __repr__(self):
        return '{' + str(self.colorWord) + "," + str(self.probab) + ', ' + str(self.info) + '}'

class wordDataSet:
    def __init__(self, wordD, probD, infoD, colorD, entropyD):
        self.wordData = wordD
        self.probData = probD
        self.infoData = infoD
        self.colorData = colorD
        self.entropyData = entropyD

    def __repr__(self):
        return '{' + str(self.wordData) + "," + str(self.probData) + ', ' + str(self.infoData) + "," + str(self.colorData) + str(self.entropyData) + '}'


for i in tqdm (range(len(words)), desc="Loading...", ascii=False, ncols=75):

    letters = words[i]

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

    xyz = 0
    entropy = 0

    meanProb = statistics.mean(probGraph)
    meanInfo = statistics.mean(infoGraph)
    for eProb in probGraph:
        entropy += eProb * infoGraph[xyz]
        xyz += 1
    probColor = colorGraph[-1]

    wordInfo = wordDataSet(letters, meanProb, meanInfo, probColor, entropy)
    allWordInfo.append(wordInfo)


allWordInfo.sort(key=lambda w: w.probData)

allWordData = []
allProbData = []
allInfoData = []
allColorData = []
allEntropyData = []

for element in allWordInfo:
    allWordData.append(element.wordData)
    allProbData.append(element.probData)
    allInfoData.append(element.infoData)
    allColorData.append(element.colorData)
    allEntropyData.append(element.entropyData)

outPath = "G:/My Drive/Wordle_All_Math3.xlsx"

df = pd.DataFrame({"Word": allWordData, "Mean Probability": allProbData, "Mean Information": allInfoData, "Most Probable Color": allColorData, "Entropy": allEntropyData})

writer = pd.ExcelWriter(outPath, engine="xlsxwriter")

df.to_excel(writer, sheet_name="All Words", index=False)

writer.save()

print("Finished")