#Author: Joppe Aarnoutse, Floris Wondergem, and Joël David
#Supervisor: H.Yu
#Course: Intelligent Control: CU04448

import pprint

pp = pprint.PrettyPrinter(sort_dicts=False)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
previouslyEncryptedText = ''

def encryptText():
    print("Encrypting option selected")

    while True:
        try:
            inputText = input('Please enter the the text to be encrypted: ')                                            #Receiving the original text to be encrypted, keep looping until valid text is entered
            for i in range(len(inputText)):                                                                             #Getting the length of the input-text and looping over each character in this range
                char = inputText[i].lower()
                if char not in alphabet:
                    raise TypeError("Only character from alphabet allowed")
            break
        except:
            print("Please enter text with valid characters included in the normal alphabet range")
    
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
    #print("EncryptedText: ", encryptedText)
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

        while True:
            inputText = input('Please enter the the text to be decrypted: ')                                            #Receiving the text to be decrypted
            badCharacterDetected = False                
            for i in range(len(inputText)):                                                                             
                char = inputText[i].lower()
                if char not in alphabet:
                    badCharacterDetected = True
                
            if badCharacterDetected == False:
                break
            else:
                print("Please enter text with valid characters included in the normal alphabet range")
    
    while True: 
        try:                                                                                                       
            key = int(input('Please enter the decryption key: '))                                                       #Receiving the decryption key
            break
        except:
            print("***Please enter a integer value***")
    print("Decrypting..........")
    decryptedText = shiftText((-1*key), inputText)
    #print("DecryptedText: ", decryptedText)
    print(inputText)
    print("↓" * len(inputText))
    print(decryptedText)

    input("\nPress enter to return to the selection menu → ")
    print("\n"*3)
            
def shiftText(key, inputText):                                                                                          #Function to shift the text in the alphabet in order to de- or encrypt the text
    newCharLocationAfterCorrection = 0
    newAlphabet = []
    #newkey = 0
    
    if key > len(alphabet):
        newkey = (key % len(alphabet))
        
    elif key < (-len(alphabet)):
        newkey = (-(abs(key) % len(alphabet)))
    else:
        newkey = key

    #print("Newkey: ",newkey)

    for i in range(len(inputText)):                                                                                     #Getting the length of the input-text and looping over each character in this range
        char = inputText[i].lower()
        #print(alphabet.index(char))

        newCharLocation = int(alphabet.index(char) + newkey)                                                            #Appying the key-offset to the characters
        
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
        newAlphabet.insert(i, (alphabet[newCharLocationAfterCorrection]))                                               #Filling a list with the new characters
        
    #print(newAlphabet)
    encryptedText = "".join(newAlphabet)                                                                                #Combining the previous list into a single string  
    
    #print("Final encrypted text: ", encryptedText)

    return(encryptedText)

    
def findKey():
    
    keyResults = {}
     
    for i in range(1, len(alphabet)):                                                                                   #Generating nested dictionary to store tried keys and their results
        keyResults[f'key{i}'] = {}
        for j in alphabet: 
            keyResults[f'key{i}'][f'{j}count'] = 0
               
    letterFrequency = {
        "a" : 8.2, "b" : 1.5, "c" : 2.8, "d" : 4.3,
        "e" : 13, "f" : 2.2, "g" : 2, "h" : 6.1,
        "i" : 7, "j" : 0.15, "k" : 0.77, "l" : 4,
        "m" : 2.4, "n" : 6.7, "o" : 7.5, "p" : 1.9,
        "q" : 0.095, "r" : 6, "s" : 6.3, "t" : 9.1,
        "u" : 2.8, "v" : 0.98, "w" : 2.4, "x" : 0.15,
        "y" : 2, "z" : 0.074
    }
    
    print(letterFrequency["z"])
    
    print("Finding key option selected")
    print("Gathering probability of possible keys....")
    
    while True:
        try:
            inputText = input('Please enter the the text to be decrypted: ')                                            #Receiving the original text to be decrypted, keep looping until valid text is entered
            for i in range(len(inputText)):                                                                             #Getting the length of the input-text and looping over each character in this range
                char = inputText[i].lower()
                if char not in alphabet:
                    raise TypeError("Only character from alphabet allowed")
            break
        except:
            print("Please enter text with valid characters included in the normal alphabet range")

    inputTextLength = len(inputText.replace(" ", ""))
    print(inputTextLength)

    for i in range(1, len(alphabet)):
        keyResults[f'key{i}'] = {}
        inputText = shiftText(1, inputText)
        keyResults[f'key{i}']['result'] = inputText

        for j in alphabet: 
            keyResults[f'key{i}'][f'{j}count'] = inputText.count(j)
       

    
    



    pp.pprint(keyResults)

    quit()

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

