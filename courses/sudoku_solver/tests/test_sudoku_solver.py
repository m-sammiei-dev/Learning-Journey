import copy
import pytest

from sudoku_solver import Board, solve_sudoku


VALID_PUZZLE = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5],
]

SOLVED_BOARD = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

INVALID_PUZZLE = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 1, 5],
]


def make_board(puzzle):
    return Board(copy.deepcopy(puzzle))


def run_solver(board):
    if hasattr(board, "solver"):
        return board.solver()
    return board.solve()


def test_board_accepts_valid_puzzle():
    board = make_board(VALID_PUZZLE)
    assert isinstance(board, Board)


def test_board_rejects_invalid_row_count():
    invalid = VALID_PUZZLE[:-1]
    with pytest.raises(ValueError):
        Board(invalid)


def test_board_rejects_duplicate_in_row():
    invalid = copy.deepcopy(VALID_PUZZLE)
    invalid[0][0] = 2
    invalid[0][1] = 2
    with pytest.raises(ValueError):
        Board(invalid)


def test_find_empty_cell_returns_first_empty_position():
    board = make_board(VALID_PUZZLE)
    assert board.find_empty_cell() == (0, 0)


def test_find_empty_cell_returns_none_for_solved_board():
    board = make_board(SOLVED_BOARD)
    assert board.find_empty_cell() is None


def test_is_valid_returns_true_for_legal_move():
    board = make_board(VALID_PUZZLE)
    assert board.is_valid((0, 0), 5) is True


def test_is_valid_returns_false_for_conflicting_move():
    board = make_board(VALID_PUZZLE)
    assert board.is_valid((0, 0), 1) is False


def test_board_solver_solves_valid_puzzle():
    board = make_board(VALID_PUZZLE)
    run_solver(board)
    assert board.find_empty_cell() is None


def test_solve_sudoku_returns_solved_board():
    solved = solve_sudoku(copy.deepcopy(VALID_PUZZLE))
    assert isinstance(solved, Board)
    assert solved.find_empty_cell() is None


def test_solve_sudoku_raises_error_for_invalid_puzzle():
    with pytest.raises(ValueError):
        solve_sudoku(copy.deepcopy(INVALID_PUZZLE))
