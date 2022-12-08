alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
previouslyEncryptedText = ''

def encryptText():
    print("Encrypting option selected")

    while True:
        try:
            inputText = input('Please enter the the text to be encrypted: ')                            #Receiving the original text to be encrypted, keep looping until valid text is entered
            for i in range(len(inputText)):                                                             #Getting the length of the input-text and looping over each character in this range
                char = inputText[i].lower()
                if char not in alphabet:
                    raise TypeError("Only character from alphabet allowed")
            break
        except:
            print("Please enter text with valid characters included in the normal alphabet range")
    
    while True:                                                                                         #Receiving the encryption key/offset, keep looping untill int value is entered
        try:
            key = int(input('Please enter the encryption key: '))                                   
            break
        except:
            print("Please enter a integer value")
    encryptedText = shiftText(key, inputText)
    print("EncryptedText: ", encryptedText)
    print("Moving back to the selection menu")

def decryptText():
    print("Decrypting option selected")
    print("Printing from decrypt: ", previouslyEncryptedText)
    if previouslyEncryptedText:
        while True:
            usePreviouslyEncryptedText = input("Previously encrypted text detected, would you like to import this? y/n ")
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
            inputText = input('Please enter the the text to be decrypted: ')                            #Receiving the original text to be encrypted, keep looping until valid text is entered
            badCharacterDetected = False
            for i in range(len(inputText)):                                                             #Getting the length of the input-text and looping over each character in this range
                char = inputText[i].lower()
                if char not in alphabet:
                    badCharacterDetected = True
                
            if badCharacterDetected == False:
                break
            else:
                print("Please enter text with valid characters included in the normal alphabet range")
    
    while True:                                                                                         #Receiving the encryption key/offset, keep looping untill int value is entered
        try:
            key = int(input('Please enter the encryption key: '))                                   
            break
        except:
            print("Please enter a integer value")
    decryptedText = shiftText((-1*key), inputText)
    print("DecryptedText: ", decryptedText)
            
def shiftText(key, inputText):
    newAlphabet = []
    for i in range(len(inputText)):                                                             #Getting the length of the input-text and looping over each character in this range
        char = inputText[i].lower()
        print(alphabet.index(char))

        newCharLocation = int(alphabet.index(char) + key)                                       #Appying the key-offset to the characters
        
        print("lengthAlphabet: ", len(alphabet))
        print("NewCharLocation: ", newCharLocation)

        if newCharLocation > (len(alphabet) - 1):
            newCharLocation = newCharLocation - len(alphabet)
        elif newCharLocation < 0:
            newCharLocation = ((len(alphabet) - 1) + newCharLocation)
        
        print(newCharLocation)
        print(alphabet[newCharLocation])
        newAlphabet.insert(i, (alphabet[newCharLocation]))                                      #Filling a list with the new characters
        
    #print(newAlphabet)
    encryptedText = "".join(newAlphabet)                                                              #Combining the previous list into a single string  
    
    print("Final encrypted text: ", encryptedText)
    print(inputText)
    print("↓" * len(inputText))
    print(encryptedText)
    global previouslyEncryptedText
    previouslyEncryptedText = encryptedText
    return(encryptedText)

    
def findKey():
    print("Finding key option selected")

def customCipher():
    print("Custom substituion cipher option selected")


def selectionHandler():                                                                         #Starting function to select the desired option
    chosenOption = 0
    print('\033[1m' + '\nWelcome to the caesar cipher solver by: Joppe Aarnoutse, Floris Wondergem, and Joël David')   
    print('\033[0m')
    while chosenOption not in [1,2,3,4]:
        
        print("Option 1: Encrypt readable text with key K")
        print("Option 2: Decrypt text with key K")
        print("Option 3: Find the key K")
        print("Option 4: Encrypt with custom substitution cipher")

        chosenOption = int(input("\nPlease enter the value of the desired option, 1-4: "))
        if chosenOption not in [1,2,3,4]:
            print("\n***Input not valid!, please choose one of the availible options***")
    return chosenOption


#Main code start
while True:
    print("Printing from global prevencryptedtext: ", previouslyEncryptedText)
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

