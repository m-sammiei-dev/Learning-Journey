def arithmetic_arranger(problems,show_answer = False):
    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for problem in problems:
            first_operand, operator, second_operand = problem.split(' ')
            if operator not in ['+', '-']:
                return "Error: Operator must be '+' or '-'."
            elif not first_operand.isdigit() or not second_operand.isdigit():
                 return 'Error: Numbers must only contain digits.'
            if len(first_operand) > 4 or len(second_operand) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            
            
            width = max(len(first_operand),len(second_operand)) + 2
            
            
            top_line.append(first_operand.rjust(width))
            bottom_line.append(operator + second_operand.rjust(width - 1))
            dash_line.append('-' * width)
            if operator == '+':
                result = str(int(first_operand) + int(second_operand))    
            else:
                result = str(int(first_operand) - int(second_operand)) 
            answer_line.append(result.rjust(width))
                   
        arranger_problems = ("    ".join(top_line) + "\n" + "    ".join(bottom_line) + "\n" + "    ".join(dash_line))
        if show_answer:
            arranger_problems += "\n" + "    ".join(answer_line)
    return arranger_problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answer= True )}')    