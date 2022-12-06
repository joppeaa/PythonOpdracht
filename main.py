alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
 
def encryptText():
    
    print("Encrypting option selected")
    newAlphabet = []
    
    inputText = input('Please enter the the text to be encrypted: ')                            #Receiving the original text to be encrypted
    print("Text to be encrypted: ", inputText)
    
    key = int(input('Please enter the encryption key: '))                                       #Receiving the encryption key/offset
    print("Selected key: ", key)
          
    for i in range(len(inputText)):                                                             #Getting the length of the input-text and looping over each character in this range
        char = inputText[i]
        #print(alphabet.index(char))

        newCharLocation = int(alphabet.index(char) + key)                                       #Appying the key-offset to the characters
        if newCharLocation > len(alphabet):
            newCharLocation = newCharLocation - len(alphabet)
        elif newCharLocation < 0:
            newCharLocation = (len(alphabet) + newCharLocation)
        
        #print(newCharLocation)
        #print(alphabet[newCharLocation])
        newAlphabet.insert(i, (alphabet[newCharLocation]))                                      #Filling a list with the new characters
        
    print(newAlphabet)
    newText = "".join(newAlphabet)                                                              #Combining the previous list into a single string  
    
    print("Final encrypted text: ", newText)
    print("Moving back to the selection menu")
 
def decryptText():
    print("Decrypting option selected")
    

def findKey():
    print("Finding key option selected")


def selectionHandler():                                                                         #Starting function to select the desired option
    chosenOption = 0
    print('\033[1m' + '\nWelcome to the caesar cipher solver by: Joppe Aarnoutse, Floris Wondergem, and Joël David')   
    print('\033[0m')
    while chosenOption not in [1,2,3]:
        
        print("Option 1: Encrypt readable text with key K")
        print("Option 2: Decrypt text with key K")
        print("Option 3: Find the key K")

        chosenOption = int(input("\nPlease enter the value of the desired option, 1-3: "))
        if chosenOption not in [1,2,3]:
            print("\n***Input not valid!, please choose one of the availible options***")
    return chosenOption


#Main code start
while True:
    option = selectionHandler()
    if option == 1:
        encryptText()
    elif option ==2:
        decryptText()
    elif option ==3:
        findKey()
    else:
        print("Option selection failed, please try again.")

