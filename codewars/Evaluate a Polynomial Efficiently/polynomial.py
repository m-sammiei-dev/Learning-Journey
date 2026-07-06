def evaluate(coefficients, x):
    result = 0
    for coefficient in coefficients:
       result = (result * x) + coefficient
    return result    
    
    
    

x = 3
c = [2, 1, 5]
print(evaluate(c, x))
    