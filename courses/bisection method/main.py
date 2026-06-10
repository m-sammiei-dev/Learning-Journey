import matplotlib.pyplot as plt

def square_root_bisection(square_target, nth_root, tolerance=1e-7, max_iterations=100):
    guesses = []
    errors = []  
    
    if square_target < 0 and nth_root % 2 == 0:
        raise ValueError('Root of negative is not defined for even powers in real numbers')
    
    if square_target == 1:
        return 1
    elif square_target == 0:
        return 0
    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for i in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid ** nth_root
            
            guesses.append(mid)
            
            errors.append(abs(square_mid - square_target))

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            elif square_mid < square_target:
                low = mid
            else:
                high = mid
        if root is None:
            print(f'Failed to find root within {max_iterations} iterations')
        else:
            print(f'The {nth_root}th root of {square_target} is approximately {root}')
        
        return root, errors
def plot_convergence(errors, target, n):
    plt.figure(figsize=(10, 6))
    plt.plot(errors, marker='o', color='red', linestyle='-', label='Error Value')
    
    plt.yscale('log')
    plt.grid(True, which="both", ls="-", alpha=0.5) 
    
    plt.title(f'Convergence Analysis: Finding {n}th root of {target}')
    plt.xlabel('Iteration Number')
    plt.ylabel('Error (Log Scale)')
    plt.legend()
    plt.savefig('convergence_plot.png') 
    print("The symbol has been successfully saved.")
    plt.show()

N = 27
root_power = 3
result, error_history = square_root_bisection(N, root_power)

if error_history:
    plot_convergence(error_history, N, root_power)