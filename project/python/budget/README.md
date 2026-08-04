# Budget App

A simple Python budgeting tool built around a `Category` class that tracks deposits and withdrawals for different spending categories (e.g. Food, Clothing, Entertainment), plus a helper function that renders a bar chart of spending by category.

## How it works

### `Category` class
Each `Category` instance represents a budget category (like "Food" or "Entertainment") and keeps an internal `ledger` — a list of dictionaries, each with an `"amount"` and a `"description"`. Typical methods on this class (not shown in the snippet above, but assumed to exist) include:

- `deposit(amount, description)` — adds a positive entry to the ledger
- `withdraw(amount, description)` — adds a negative entry if there are sufficient funds, returns `True`/`False`
- `get_balance()` — returns the current balance (sum of the ledger)
- `transfer(amount, other_category)` — withdraws from one category and deposits into another
- `check_funds(amount)` — checks if a withdrawal/transfer is affordable
- `__str__` — pretty-prints the category as a formatted ledger table

### `create_spend_chart(categories)`
This function takes a list of `Category` objects and builds a text-based bar chart showing what percentage of total spending came from each category. Here's the logic step by step:

1. **Calculate spending per category**
   For each category, sum up the absolute value of every negative ledger entry (withdrawals). Deposits are ignored since the chart only cares about money spent.

2. **Calculate percentages**
   Each category's spend is divided by the total spend across all categories to get a percentage. This is then rounded *down* to the nearest multiple of 10 (e.g. 47% becomes 40%), since the chart can only display bars in 10% increments.

3. **Draw the chart**
   The chart is built from the top (100%) down to 0%, in steps of 10. For each row:
   - Print the level label (right-aligned, 3 characters wide) followed by `|`
   - For each category, print `" o "` if that category's percentage is greater than or equal to the current level, otherwise print three blank spaces
   
   This creates the visual effect of vertical bars rising from 0% to each category's percentage.

4. **Draw the horizontal axis**
   A line of dashes is drawn under the bars, wide enough to span all categories.

5. **Draw the category names vertically**
   Since category names can be longer than the bar width, they're printed **one letter per row**, underneath the axis line, so the names read top-to-bottom instead of left-to-right. The loop runs for as many rows as the longest category name requires, padding shorter names with blank space once their letters run out.

### Example output

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Usage example

```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(105.55, "groceries")

clothing = Category("Clothing")
clothing.deposit(500, "initial deposit")
clothing.withdraw(50, "shirt")

print(create_spend_chart([food, clothing]))
```

## Notes / possible extensions

- Percentages are always rounded down to the nearest 10, so bars may not visually sum to exactly 100%.
- If `total_spent` is 0 (no withdrawals anywhere), every category's percentage safely defaults to 0 instead of raising a division error.
- The chart width automatically scales with the number of categories passed in.