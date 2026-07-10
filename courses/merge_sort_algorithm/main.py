import time
from merge_sort import merge_sort

def main():
    while True:
        print("\nWelcome to the merge sort program.")
        print("1. Start program")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            try:
                user_input = input("Enter numbers separated by spaces: ").split()
                numbers = [int(num) for num in user_input]

                order = input("Enter sorting order (asc/desc): ").strip().lower()
                if order not in ["asc", "desc"]:
                    print("Invalid order. Please enter 'asc' or 'desc'.")
                    continue

                reverse = order == "desc"
                original_numbers = numbers.copy()
                stats = {"comparisons": 0}

                start_time = time.perf_counter()
                merge_sort(numbers, reverse=reverse, stats=stats)
                end_time = time.perf_counter()

                execution_time = end_time - start_time

                print("\nUnsorted array:", original_numbers)
                print("Sorted array:", numbers)
                print("Order:", order)
                print("Comparisons:", stats["comparisons"])
                print(f"Execution time: {execution_time:.6f} seconds")

            except ValueError:
                print("Invalid input. Please enter integers only.")

        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
