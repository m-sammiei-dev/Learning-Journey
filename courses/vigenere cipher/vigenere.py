def vigenere(message, key, direction=1):
    result_message = ""
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for char in message.lower():
        # Append non-alphabetic characters (like spaces, numbers, or symbols) 
        # to the message without encrypting/decrypting them
        if char not in alphabet:
            result_message += char
        else:
            # Find the right key character based on the current index
            key_char = key[key_index % len(key)]
            key_index += 1
            
            # Define the offset and calculate the new character index
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + (offset * direction)) % len(alphabet)
            result_message += alphabet[new_index]
            
    return result_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1) 

while True:
    print("\n--- Vigenère Cipher Menu ---")
    print("1. Encrypt a message")
    print("2. Decrypt a message")  
    print("3. Exit")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        text = input("Enter the message to encrypt: ")
        key = input("Enter the secret key: ")
        result = encrypt(text, key)
        print(f'Encrypted message: {result}')
        
    elif choice == '2':
        text_decrypt = input("Enter the message to decrypt: ")
        key_decrypt = input("Enter the secret key: ")
        result = decrypt(text_decrypt, key_decrypt)
        print(f'Decrypted message: {result}')
        
    elif choice == '3':
        print('Exiting the program... Goodbye, Master!')
        break
    else:
        print("Invalid choice. Please try again.")
