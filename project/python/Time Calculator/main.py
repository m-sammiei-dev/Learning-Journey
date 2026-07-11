from time_calculator import add_time


def main():
    while True:
        print("\nWelcome to the time calculator program.")
        print("1. Start program")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            try:
                start = input("Enter start time: ").strip()
                duration = input("Enter duration: ").strip()
                day_of_week = input("Enter day of week (optional): ").strip() or None

                result = add_time(start, duration, day_of_week)
                print(f"\nResult: {result['result']}")

            except Exception as error:
                print(f"Error: {error}")

        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
