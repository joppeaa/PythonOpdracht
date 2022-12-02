textInputConfirmed = "N"
keyInputConfirmed = "N"

while textInputConfirmed.lower() != "y":
    inputText = input('Please enter the the text to be encrypted: ')
    print("Text to be encrypted: ", inputText)
    textInputConfirmed = input('Please check the entered text, Continue? y/n: ')
    
while textInputConfirmed.lower() != "y":
    textInputConfirmed == "y" or "Y" or "YES" or "Yes" or "yes":
    key = input('Please enter the encryption key: ')
    print("Selected key: ", key)
    keyInputConfirmed = input('Please check the entered key, Continue? y/n: ')

