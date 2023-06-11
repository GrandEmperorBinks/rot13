import json
output = []     #create output list for use later on

def ROT13():    #define the encoding/deconding function
    alphabet = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']     #list of encodable/decodable characters - the alphabet
    messageList = []
    newMessage = ''
    message = input('Enter text to be encoded/decoded (enter x to end program): ')      #prompt the user for input

    for character in message:   #convert the input (the message variable) to a list (the messageList) variable
        messageList.append(character.lower())

    for letter in messageList:  #iterate through messageList
        if letter in alphabet:  #if the letter is in our alphabet list, replace it with the character 13 positions away and add that new character to a string
            index = alphabet.index(letter)
            index = index + 13
            if index > 26:      #ensure that it loops back to the start of the aplhabet list if the index is higher than available
                index = index - 26
            newMessage = newMessage + alphabet[index]
        else:                   #if the character isn't encodeable/decodeable, add it without encoding to the string
            newMessage = newMessage + letter

    return newMessage           #return the new message newMessage

file = open('data.txt', 'w')    #open the file data.txt


while True:                     #forever repeat
    text = ROT13()              #run the function and save the output as text
    if text == 'k':             #if the text is 'k' (encoded version of 'x'), break out of infinite loop (ending program)
        break
    else:                       #else add message to a list of encoded/decoded messages
        output.append(text)

json.dump(output, file, indent = 2)     #write list of messages to the file in JSON format
file.close()
