def verify_card_number(card_number):
    reversed_card_number = card_number[::-1]
    odd_digits = reversed_card_number[::2]
    even_digits = reversed_card_number[1::2]
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            sum_of_even_digits += number // 10 + number % 10
        else:
            sum_of_even_digits += number 
    total = sum_of_even_digits + sum_of_odd_digits
    return total % 10 == 0
def get_card_type(card_number):
    if int(card_number[0]) == 4:
        return 'Visa' 
    elif int(card_number[0:2]) == 51 or int(card_number[0:2]) == 55:
        return 'MasterCard'
    elif int(card_number[0:2]) == 34 or int(card_number[0:2]) == 37:
        return 'American Express'
    else:
        return 'Unknowm Provider'          
def main():
    
    while True:
        print('Advance Luhn Card Validator')
        user_input = input('Enter card number to validate (or type exit to quit):')
    
        if user_input.lower() == 'exit':
            print('Goodbye')
            break
    
        card_translation = str.maketrans({'-': '', ' ': ''})
        translated_card_number = user_input.translate(card_translation)
        continue
        if not translated_card_number.isdigit():
            print('Please enter numbers')
        if verify_card_number(translated_card_number):
            card_type = get_card_type(translated_card_number)
            print(f'VALID! Type: {card_type}')
        else:
            print('UNVALID!')
        

main()       
           
