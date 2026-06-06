
def vigenere(message, key):
    result_message = ""
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in message.lower():
        # Append non-alphabetic characters (like spaces, numbers, or symbols) to the message without encrypting them
        check_is_alphabet = 0
        for i in alphabet:
            if char == i:
                check_is_alphabet += 1
                
        if check_is_alphabet != 1:
         result_message += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            result_message += alphabet[new_index]
    return result_message
while True:
    print("\nChoose an option:")
    print("1. Encrypt the massege")
    print("2. Exit")
    
    choice = input("\nEnter your Choice (1/2):")
    if choice == '1':
        text = input("Enter the message: ")
        key = input("Enter the secret key: ")
        result = vigenere(text, key)
        print("\nResult:" ,result)

    elif choice == '2':
        print("Goodbye!")
        break
    else:
        print("invalid choice. please try again...")