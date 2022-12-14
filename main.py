#Author: Joppe Aarnoutse, Floris Wondergem, and Joël David
#Supervisor: H.Yu
#Course: Intelligent Control: CU04448

import pprint
from copy import deepcopy

pp = pprint.PrettyPrinter(sort_dicts=False)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
previouslyEncryptedText = ''


def getInputText(messageToDisplay):
    
    while True:
        try:
            inputText = input(messageToDisplay)
            if not inputText:
                raise TypeError("Please enter valid text")
            else:
                return inputText
        except TypeError as e:
            print(e)


def encryptText():
    
    print("Encrypting option selected")
    inputText = getInputText("Please enter the text to be encrypted: ")
    
            
    while True:                                                                                                         
        try:
            key = int(input('Please enter the encryption key: '))                                                       #Receiving the encryption key/offset, keep looping untill int value is entered
            break
        except:
            print("Please enter a integer value")
    print("Encrypting..........")
    encryptedText = shiftText(key, inputText)                                                                           #Calling shiftText function to encrypt the text
    global previouslyEncryptedText                      
    previouslyEncryptedText = encryptedText                                                                             #Storing encrypted text in global variable in order to use it in the decryption option
    
    print(inputText)
    print("↓" * len(inputText))
    print(encryptedText)
    input("\nPress enter to return to the selection menu → ")
    print("\n"*3)

def decryptText():
    print("Decrypting option selected")
    
    if previouslyEncryptedText:                                                                                         #Checking if the is encrypted text stored in the global variable
        print("Previously encrypted text:", previouslyEncryptedText)
        while True:
            usePreviouslyEncryptedText = input("Previously encrypted text detected, would you like to import this? y/n ")   #Checking if user wants to use previously encrypted text
            if usePreviouslyEncryptedText.lower() in ["y","n"]:                                         
                break
            else:
                print("Please enter y or n to continue")
        if usePreviouslyEncryptedText.lower() == "y":
            inputText = previouslyEncryptedText
            userInputRequired = False
        else:
            userInputRequired = True
    else:
        userInputRequired = True

    if userInputRequired:

        getInputText("Please enter te text to be decrypted: ")
    
    while True: 
        try:                                                                                                       
            key = int(input('Please enter the decryption key: '))                                                       #Receiving the decryption key
            break
        except:
            print("***Please enter a integer value***")
    print("Decrypting..........")
    decryptedText = shiftText((-1*key), inputText)
    
    print(inputText)
    print("↓" * len(inputText))
    print(decryptedText)

    input("\nPress enter to return to the selection menu → ")
    print("\n"*3)
            
def shiftText(key, inputText):                                                                                          #Function to shift the text in the alphabet in order to de- or encrypt the text
    newCharLocationAfterCorrection = 0
    newAlphabet = []
      
    if key > len(alphabet):
        newkey = (key % len(alphabet))
        
    elif key < (-len(alphabet)):
        newkey = (-(abs(key) % len(alphabet)))
    else:
        newkey = key



    for i in range(len(inputText)):                                                                                     #Getting the length of the input-text and looping over each character in this range
        char = inputText[i].lower()
      
        if char in alphabet:
            newCharLocation = int(alphabet.index(char) + newkey)
              #print("lengthAlphabet: ", len(alphabet))
            #print("NewCharLocation: ", newCharLocation)
        
            if newCharLocation > (len(alphabet) - 1):                                                                       #Handling for when the index reaches the edges of the list
                newCharLocationAfterCorrection = newCharLocation - len(alphabet)
            elif newCharLocation < 0:
                newCharLocationAfterCorrection = (len(alphabet) + newCharLocation)
            else:
                newCharLocationAfterCorrection = newCharLocation
        
            #print("newCharLocAfterCorrection: ", newCharLocationAfterCorrection)
            #print(alphabet[newCharLocationAfterCorrection])
            newAlphabet.insert(i, (alphabet[newCharLocationAfterCorrection]))  
            
            
                                                                        #Appying the key-offset to the characters
        else:
             newAlphabet.insert(i, char)
        
                                                   #Filling a list with the new characters
        
    encryptedText = "".join(newAlphabet)                                                                                #Combining the previous list into a single string  
    
    return(encryptedText)

    
def findKey():
    
    # alphabetWithoutSpace = deepcopy(alphabet)
    # alphabetWithoutSpace.pop(26)
    # print(alphabetWithoutSpace)

    keyResults = {}
     
    for i in range(1, len(alphabet)):                                                                                   #Generating nested dictionary to store tried keys and their results
        keyResults[f'key{i}'] = {}
        keyResults[f'key{i}']['percentageError'] = ''
        for j in alphabet: 
            keyResults[f'key{i}'][f'{j}count'] = 0
                           
    letterFrequency = {                                                                                                 #List of nominal letter frequency in the english language, wikipedia.
        "a" : 8.2, "b" : 1.5, "c" : 2.8, "d" : 4.3,
        "e" : 13, "f" : 2.2, "g" : 2, "h" : 6.1,
        "i" : 7, "j" : 0.15, "k" : 0.77, "l" : 4,
        "m" : 2.4, "n" : 6.7, "o" : 7.5, "p" : 1.9,
        "q" : 0.095, "r" : 6, "s" : 6.3, "t" : 9.1,
        "u" : 2.8, "v" : 0.98, "w" : 2.4, "x" : 0.15,
        "y" : 2, "z" : 0.074
    }
    
    #print(letterFrequency["z"])
    
    print("Finding key option selected")
    
    #print(alphabet)
    
    inputText = getInputText("Please enter the encrypted text to be hacked: ")

    inputTextLength = len(inputText.replace(" ", ""))
    print(inputTextLength)

    for i in reversed(range(1, len(alphabet))):                                                                                   #looping over every possible key
        keyResults[f'key{i}'] = {}
        inputText = shiftText(1, inputText)
        keyResults[f'key{i}']['result'] = inputText
        percentageError = 0
        
        for j in alphabet: 
            keyResults[f'key{i}'][f'{j}count'] = inputText.count(j)
            percentageError = percentageError + ((((keyResults[f'key{i}'][f'{j}count'] / inputTextLength)*100) - letterFrequency[j]) / letterFrequency[j])
            
        keyResults[f'key{i}']['percentageError'] = (percentageError)

    #pp.pprint(keyResults)
        
    sortedKeyResults = sorted(keyResults.items(), key=joppeSort, reverse=True)

    top1Results = sortedKeyResults.pop()  
    top2Results = sortedKeyResults.pop()
    top3Results = sortedKeyResults.pop()
    top4Results = sortedKeyResults.pop()
    
    print("\nFinal solution: ")
    print("     Top1: ", top1Results[0], ",\tresult:", top1Results[1]["result"])
    
    print("\nIf the solution is not correct, the text length may have been too short to represent the nominal english text letter frequency")
    print("Three most probable alternative solutions:")
    
    print("     Top2: ", top2Results[0], ",\tresult:", top2Results[1]["result"])
    print("     Top3: ", top3Results[0], ",\tresult:", top3Results[1]["result"])
    print("     Top4: ", top4Results[0], ",\tresult:", top4Results[1]["result"])
    
    quit()

def joppeSort(item):
    return item[1]['percentageError']


def customCipher():
    print("Custom substituion cipher option selected")
    print("ha")

def selectionHandler():                                                                                                 #Starting function to select the desired option
    print('\033[1m' + '\nWelcome to the caesar cipher solver by: Joppe Aarnoutse, Floris Wondergem, and Joël David')   
    print('\033[0m')

    while True:
        try:
            print("     Option 1: Encrypt readable text with key K")                                                    #Displaying options to user
            print("     Option 2: Decrypt text with key K")
            print("     Option 3: Find the key K")
            print("     Option 4: Encrypt with custom substitution cipher")
            chosenOption = int(input("\nPlease enter the value of the desired option, 1-4: "))
            if chosenOption in [1,2,3,4]:
                break
        except:
                print("***invalid input***")     

    return chosenOption

#Main code start
while True:                                                                                                             #Main loop
    option = selectionHandler()
    if option == 1:
        encryptText()
    elif option == 2:
        decryptText()
    elif option == 3:
        findKey()
    elif option == 4:
        customCipher()
    else:
        print("Option selection failed, please try again.")

