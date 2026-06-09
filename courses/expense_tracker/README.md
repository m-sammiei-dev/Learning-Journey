# 💰 Advanced Expense Tracker (Python)

This is a functional CLI-based Expense Tracker developed as part of my Python learning journey. It started with the foundational logic from **freeCodeCamp** and was significantly enhanced with custom features and improved data handling.

## 🚀 Key Enhancements (Beyond the Tutorial)
Unlike the basic version, this version includes:
- **Expense Removal:** Added a system to remove specific expenses using unique IDs (index-based).
- **Financial Analytics:** Implemented a percentage-based reporting system to see how much each category contributes to total spending.
- **Improved Data Management:** Used `list()` conversion for Filter objects to ensure data persistence during multiple operations.
- **Modular Code:** Refined function naming and structure for better readability and PEP 8 compliance.

## 🧠 Logic & Technical Overview
The project demonstrates the use of several advanced Python concepts:
- **Lambda Functions:** Used for concise, on-the-fly logic within higher-order functions.
- **Map & Filter:** Leveraged for efficient data transformation and extraction without using explicit for-loops for every calculation.
- **List & Dictionary Compositions:** Data is structured as a list of dictionaries to simulate a real-world JSON-like database.
- **Error Handling (Logic):** Includes checks for "Division by Zero" when calculating percentages of an empty list.

## 🛠 Features
1. **Add Expense:** Record amount and category.
2. **Remove Expense:** Delete records by their sequence number.
3. **List All:** Display a formatted list of all entries.
4. **Total Balance:** Calculate the sum of all expenses.
5. **Categorized View:** Filter expenses by a specific category.
6. **Analytics:** View the percentage of total spending for any chosen category.

## 💻 How to Run
1. Clone the repository:
```bash
   git clone https://github.com/m-sammiei-dev/expense-tracker.git
 
