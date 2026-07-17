from sudoku_solver import solve_sudoku


def get_board():
    board = []
    print("Enter 9 rows of the Sudoku puzzle.")
    print("Use spaces between numbers and 0 for empty cells.")

    for i in range(9):
        raw = input(f"Row {i + 1}: ").split()

        if len(raw) != 9:
            raise ValueError("Each row must contain exactly 9 numbers.")

        try:
            row = [int(num) for num in raw]
        except ValueError:
            raise ValueError("Each row must contain only integers.")

        board.append(row)

    return board


def main():
    try:
        board = get_board()
        solved = solve_sudoku(board)
        print("\nSolved puzzle:")
        print(solved)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
