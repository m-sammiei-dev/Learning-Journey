class Board:
    """Represent a Sudoku board and solve it with backtracking."""

    def __init__(self, board):
        self._validate_board(board)
        self.board = board

    def _validate_board(self, board):
        if len(board) != 9:
            raise ValueError("Board must have 9 rows.")

        for row in board:
            if len(row) != 9:
                raise ValueError("Each row must have 9 columns.")

            for num in row:
                if not isinstance(num, int) or num < 0 or num > 9:
                    raise ValueError("Board values must be integers from 0 to 9.")

        for row in board:
            nums = [num for num in row if num != 0]
            if len(nums) != len(set(nums)):
                raise ValueError("Board has duplicate numbers in a row.")

        for col in range(9):
            nums = [board[row][col] for row in range(9) if board[row][col] != 0]
            if len(nums) != len(set(nums)):
                raise ValueError("Board has duplicate numbers in a column.")

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                nums = []

                for row in range(row_start, row_start + 3):
                    for col in range(col_start, col_start + 3):
                        num = board[row][col]
                        if num != 0:
                            nums.append(num)

                if len(nums) != len(set(nums)):
                    raise ValueError("Board has duplicate numbers in a 3x3 square.")

    def __str__(self):
        lines = []
        border = "+-------+-------+-------+"

        for row_index, row in enumerate(self.board):
            if row_index % 3 == 0:
                lines.append(border)

            values = [str(num) if num != 0 else "*" for num in row]
            line = (
                f"| {' '.join(values[0:3])} "
                f"| {' '.join(values[3:6])} "
                f"| {' '.join(values[6:9])} |"
            )
            lines.append(line)

        lines.append(border)
        return "\n".join(lines)

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return valid_in_row and valid_in_col and valid_in_square

    def solve(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True

        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False


def solve_sudoku(board):
    gameboard = Board(board)
    if not gameboard.solve():
        raise ValueError("The provided puzzle is unsolvable.")
    return gameboard
