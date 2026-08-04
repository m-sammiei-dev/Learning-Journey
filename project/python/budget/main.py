def create_spend_chart(categories):
    spent = []

    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    percentages = []
    for value in spent:
        percent = 0
        if total_spent != 0:
            percent = int((value / total_spent) * 100)
        percentages.append((percent // 10) * 10)

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += str(level).rjust(3) + "|"
        for percent in percentages:
            if percent >= level:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart
