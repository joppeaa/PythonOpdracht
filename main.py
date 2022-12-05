alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def encryptText():
    textInputConfirmed = "N"
    keyInputConfirmed = "N"
    newAlphabet = []
    newText = ""

    while textInputConfirmed.lower() != "y":
        inputText = input('Please enter the the text to be encrypted: ')
        print("Text to be encrypted: ", inputText)
        textInputConfirmed = "y"
    
    while keyInputConfirmed.lower() != "y":
        key = int(input('Please enter the encryption key: '))
        print("Selected key: ", key)
        keyInputConfirmed = "y"
    
    

    for i in range(len(inputText)):
        char = inputText[i]
        print(alphabet.index(char))

        newCharLocation = int(alphabet.index(char) + key)
        if newCharLocation > len(alphabet):
            newCharLocation = newCharLocation - len(alphabet)
        print(newCharLocation)
        print(alphabet[newCharLocation])
        newAlphabet.insert(i, newCharLocation)
        
    for i in range(len(newAlphabet)):
        print(newAlphabet[i])
   

def selectionHandler():                                                                         #Starting function to select the desired option
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


