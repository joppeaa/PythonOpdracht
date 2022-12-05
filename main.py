#alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encryptText():
    textInputConfirmed = "N"
    keyInputConfirmed = "N"
    while textInputConfirmed.lower() != "y":
        inputText = input('Please enter the the text to be encrypted: ')
        print("Text to be encrypted: ", inputText)
        textInputConfirmed = input('Please check the entered text, Continue? y/n: ')
    
    while keyInputConfirmed.lower() != "y":
        key = input('Please enter the encryption key: ')
        print("Selected key: ", key)
        keyInputConfirmed = input('Please check the entered key, Continue? y/n: ')
    
        
    for i in range(len(inputText)):
        char = inputText[i]
        charLocation = ord(char)
        print(chr(charLocation), "ord: ", charLocation)

def selectionHandler():                                                                         #Starting function to choose the selected 
    chosenOption = 0
    while chosenOption not in [1,2,3]:
        print("Option 1: Encrypt readable text with key")
        print("Option 2: Decrypt text with key K")
        print("Option 3: Find the key K")

        chosenOption = int(input("Please enter the value of the desired option, 1-3: "))

    return chosenOption





#Main code start

option = selectionHandler()
if option == 1:
    encryptText()


