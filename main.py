alphabet = ["a", "b", "c", "d",	"e", "f", "g", "h",	"i", "j", "k", "l",	"m", "n", "o", "p",	"q", "r", "s", "t", "u", "v", "w", "x",	"y", "z",]

def encryptText(textToEncrypt):
    for i in range(len(textToEncrypt)):
        char = textToEncrypt[i]


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

print(len(inputText))
encryptText(inputText)
