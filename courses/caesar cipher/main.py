text = 'Hello zarld!'
shift = 3
def ceasar(message, key):
    alphabet = 'abcdefghijklnopqrstuvwxyz'
    ceasar_result = ''
    for char in message.lower():
        if char == " ":
            ceasar_result += " "
        else:    
            index = (alphabet.find(char) + key) % len(alphabet)
            ceasar_result += alphabet[index]
    print('text:',message, 'ceasar_result:',ceasar_result)
    
    
ceasar('salam', 13)