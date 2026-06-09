def convert_to_snake_case(camel_or_pascal_string):
    coverted_to_snake_case = ['_' + char.lower() if char.isupper() else char for char in camel_or_pascal_string]
    return ''.join(coverted_to_snake_case).strip('_')

def auto_detection(input_string):
    if input_string.islower():
        return 1
    return 0

def reverse_from_snake_case(input_string, option):
    words = input_string.split('_')
    
    if option == '1': 
        return words[0] + ''.join(word.title() for word in words[1:])
    
    elif option == '2':
        return ''.join(word.title() for word in words)
    
    return input_string

    
def main():
    while True:
        print('\nWelcome To Convert Or Reverse Snake_Case App')
        
        print('\n1. Covert To Snake_case')
        print('2. Reverse From Snake_case')
        print('3. Exit')
        choice = input('\nPlease Enter Your Choice (1/2):')
        if choice == '1':
            input_string = input('\nPlease Enter Your String:' )
            if auto_detection(input_string):
                print('\nALREADY SNAKE CASE!')
            else:
                print(f'This Is Your Snake_case String: {convert_to_snake_case(input_string)}')
        
        elif choice == '2':
            input_string = input('\nPlease Enter Your String:' )
            option = input ('\nIf You Want CamelCase Choose (1) And For PascalCase Choose (2): ') 
            print(f'This Is Your Snake_case String: {reverse_from_snake_case(input_string, option)}')
        elif choice == '3':
            print('goodbye')
            break
        else:
            print('\nINVALIDE CHOICE !!!')


main()