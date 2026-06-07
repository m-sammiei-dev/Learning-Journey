🛡️ Advanced Luhn Algorithm Card Validator

A professional Python-based CLI tool that validates credit card numbers using the Luhn Algorithm (also known as the "mod 10" algorithm). This project demonstrates string manipulation, data validation, and logic implementation in Python.

🚀 Features





Luhn Validation: Accurately checks if a card number is mathematically valid.



Card Type Identification: Automatically detects major card providers:





🟦 Visa (Starts with 4)



🟥 MasterCard (Starts with 51-55)



🟩 American Express (Starts with 34 or 37)



Input Cleaning: Handles spaces and hyphens (-) automatically using str.maketrans.



Interactive CLI: A user-friendly loop that allows multiple validations in one session.

🧠 How the Luhn Algorithm Works





Reverse the card number.



Sum the digits in the odd positions (1st, 3rd, 5th, etc.).



For digits in even positions, multiply by 2.





If the result is greater than 9, add the digits of the result (for example, 12 becomes 1 + 2 = 3).



Add all results together.



If the total ends in 0, meaning ( \text{Total} % 10 = 0 ), the card is valid.

🛠️ Technologies Used





Language: Python 3.x



Concepts: Slicing, Dictionary Mapping, String Translation, Loops, and Error Handling.

📋 How to Run





Clone the repository:

git clone https://github.com/YourUsername/Learning-Journey.git




Navigate to the directory:

cd courses/luhn_algorithm




Run the script:

python main.py


📂 Project Structure

Learning-Journey/
├── courses/
│   └── luhn_algorithm/
│       └── main.py          # Core logic and CLI
├── README.md                # Project documentation
└── .gitignore               # Ignoring .venv and cache




Developed by a Junior Developer during the Learning Journey.