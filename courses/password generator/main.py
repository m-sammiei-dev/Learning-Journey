import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """Generate a random password that satisfies the minimum character constraints."""
    if length < 1:
        raise ValueError('length must be at least 1')
    if any(value < 0 for value in [nums, special_chars, uppercase, lowercase]):
        raise ValueError('constraints cannot be negative')
    if nums + special_chars + uppercase + lowercase > length:
        raise ValueError('constraints cannot be greater than password length')
    # Define the possible characters for the password
    digits = string.digits
    letters = string.ascii_letters
    symbols = string.punctuation
    escaped_symbols = re.escape(symbols)
    # Define all characters
    all_characters = digits + letters + symbols
    
    # Generate password
    while True:
        password = ''
        for _ in range(length):
            password += secrets.choice(all_characters)
    
        constraints = [
            (nums, r'\d'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]'),
            (special_chars, fr'[{escaped_symbols}]')
        ]     

        if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints):
            break
        
    return password

def main():
    while True:
        print('\nWelcome to password generator')
    
        print('1. Create New Password')
        print('2. Exit')
        choice = input('\nplease enter your choice: ')
        if choice == '1':
            try:
                count = int(input('How many passwords do you want? '))
                if count < 1:
                    raise ValueError('count must be at least 1')
                length = int(input('Please enter the length of each password: '))
                nums = int(input('How many numbers do you want in each password at least? '))
                lowercase = int(input('How many lowercase letters do you want in each password at least? '))
                uppercase = int(input('How many uppercase letters do you want in each password at least? '))
                symbols_count = int(input('How many symbols do you want in each password at least? '))                   
                passwords = set()
                while len(passwords) < count:
                    single_password = generate_password(
                        length=length, 
                        nums=nums, 
                        lowercase=lowercase, 
                        uppercase=uppercase, 
                        special_chars=symbols_count
                    )
                    passwords.add(single_password)                    
                    print('\nGenerated passwords:')    
                for index, pwd in enumerate(passwords, start=1):
                    print(f'{index}. {pwd}')                       
            except ValueError as error:
                print(f'Error: {error}')
        elif choice == '2':
            print('Goodbye!')
            break
        else:
            print('Please enter a valid choice')

        
if __name__ == '__main__':        
    main()