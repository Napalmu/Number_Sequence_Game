from random import choice
from math import floor, ceil
from threading import Timer

level = 1.0

def startGame():

    incrLevel = 1
    
    while True:
        currentStr = getStr(floor(level), incrLevel)

        print("\n")
        print(currentStr)
        print("\n")

        timeout = 5
        t = Timer(timeout, gameOver)

        t.start()
        prompt = "Time: %d seconds \n" % timeout
        userInput = input(prompt)
        t.cancel() 

        checkAnsw(userInput, currentStr)

def checkAnsw(userInput, currentStr):
    global level
    if userInput == currentStr:
        level += 0.5
    
def gameOver():
    global level
    print("\nGame over, your score: "+ str(ceil(level)+1))
    input()
    quit()

def getStr(level, incrLevel):
    num = "1234567890"
    newNum = ""
    for i in range(0, level+incrLevel):
        newNum += choice(num)
    return newNum
