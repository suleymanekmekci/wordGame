import random
import sys
import time

if len(sys.argv) < 3:
    print("You must write two arguments for this program")
else:
    wordFileName, letterFileName = sys.argv[1],sys.argv[2]

    with open(wordFileName,"r",encoding="utf-8") as wordsFile:
        myWordDict = {}
        
        for line in wordsFile:
            wordDictKeys = line.split(":")[0]
            wordDictValueList = []
            for wordDictValue in line.split(":")[1].strip("\n").split(","):
                
                if "I" in wordDictValue:
                    wordDictKeys = wordDictKeys.replace("I","ı").lower()
                    wordDictValue = wordDictValue.replace("I","ı").lower()
                    wordDictValueList.append(wordDictValue)
                    myWordDict[wordDictKeys] = wordDictValueList
                    
                else:
                    wordDictKeys = wordDictKeys.lower()
                    wordDictValue = wordDictValue.lower()
                    wordDictValue = wordDictValue.replace("i̇","i")
                    wordDictValueList.append(wordDictValue)
                    myWordDict[wordDictKeys] = wordDictValueList
                    
                
    
    with open(letterFileName,"r",encoding="utf-8") as lettersFile:
        myLetterDict = {}
        for line in lettersFile:
            letterDictKeys = line.split(":")[0]
            if letterDictKeys == "I":
                letterDictKeys = letterDictKeys.lower().replace("i","ı")
            elif letterDictKeys == "İ":
                
                letterDictKeys = letterDictKeys.lower().replace("i̇","i")
            else:

                letterDictKeys = letterDictKeys.lower()
            
            
            letterDictValues = int(line.split(":")[1].strip("\n"))
            myLetterDict[letterDictKeys] = letterDictValues
    
    
    def findTheValue(userValue,word):
        global pointForWords
        
        pointForWords = 0
        
        if userValue in myWordDict[word] and dictionaryForKnownWords[userValue] != 1:
            
            dictionaryForKnownWords[userValue] = 1

            ##point calculation
            for letter in userValue:
                eachPoint = myLetterDict[letter]
                pointForWords += eachPoint
            pointForWords *= len(userValue)     
        
        elif len(userValue) < 3:
            print("Please guess words for these letters with minimum three letters")
            
        elif userValue in myWordDict[word] and dictionaryForKnownWords[userValue] == 1:
            print("This word is guessed before")
            
        elif userValue not in myWordDict[word]:
            print("your guessed word is not a valid word")
            
        
        
    remainTime = 30
    totalPointsForAll = 0
    for word in myWordDict:
        print("Shuffled letters are:  {}  Please guess words for these letters with minimum three letters".format(word))
        dictionaryForKnownWords = {}
        
        start = time.time()
        
        totalPointsForWord = 0
        guessedWordString = ""
        for values in myWordDict[word]:
            dictionaryForKnownWords[values] = 0
        
        while True:
            
            guessedWord = input("Guessed word: ")
            if "I" in guessedWord:
                guessedWord = guessedWord.lower().replace("i","ı")
            elif "İ" in guessedWord:
                guessedWord = guessedWord.lower().replace("i̇","i")
            else:
                guessedWord = guessedWord.lower()
            
            
            
            
            if guessedWord:
                if 30 - int(time.time() - start) <=0:
                    guessedWordString = guessedWordString.strip("-")
                    print("You have 0 time")
                    print("Score for  {}  is  {}  points and guessed words: {}".format(word,totalPointsForWord,guessedWordString))
                    break
                else:
                    if len(guessedWord) >2 and guessedWord not in guessedWordString and guessedWord in myWordDict[word]:
                        guessedWordString += guessedWord + "-"
                    findTheValue(guessedWord,word)
                    totalPointsForWord += pointForWords
                    remainTime = 30  - int(time.time() - start)
                    print("You have  {}  time".format(remainTime))
                
            
            #check if finish
            if 0 in dictionaryForKnownWords.values():
                pass
            else:
                break

        totalPointsForAll += totalPointsForWord
    print("Total score is {} points".format(totalPointsForAll))
