# This is slower than plain python version

import time
import puzzle
import numpy as np

backtracks = 0


def print_sudoku(sudoku):
    for i, row in enumerate(sudoku):
        if i in [3, 6]:
            print("-" * 23)
        print(row[:3], end=" ")
        print(row[3:6], end=" ")
        print(row[6:9])


def find_cell_to_fill(sudoku):
    index = np.argwhere(sudoku == 0)
    if index.shape[0] > 0:
        i, j = index[0]
        return i, j
    return ("Solved", 0)

    # for i in range(9):
    #     for j in range(9):
    #         if sudoku[i,j] == 0:
    #             return i, j
    # return ("Solved", 0)


def is_valid(sudoku, row_num, col_num, number):
    if number not in sudoku[row_num, :]:  # check row
        if number not in sudoku[:, col_num]:  # check row
            region_row_start = 3 * (row_num // 3)
            region_col_start = 3 * (col_num // 3)
            if (
                number
                in sudoku[
                    region_row_start : region_row_start + 3,
                    region_col_start : region_col_start + 3,
                ]
            ):
                return False
            return True
    return False


def brute_force(sudoku):
    global backtracks
    i, j = find_cell_to_fill(sudoku)
    if i == "Solved":
        print("Solved")
        return True

    for number in range(1, 10):
        if is_valid(sudoku, i, j, number):
            sudoku[i, j] = number
            if brute_force(sudoku):
                return True
            backtracks += 1
            sudoku[i, j] = 0
    return False


def main(sudoku):
    sudoku = np.array(sudoku)
    print_sudoku(sudoku)
    t0 = time.perf_counter()
    brute_force(sudoku)
    t1 = time.perf_counter()
    print_sudoku(sudoku)
    print(backtracks)
    print(f"time taken: {(t1-t0):.4f} seconds")


main(puzzle.diabolical)
