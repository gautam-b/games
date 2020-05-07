"""
Solve Soduku Puzzle thorough backtracking and recurssion
"""

import time
import puzzle
from soduku_img import draw_soduku
from utils import print_sudoku


backtracks = 0


def find_cell_to_fill(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return False


def is_valid(sudoku, row_num, col_num, number):
    if number not in sudoku[row_num]:  # check row
        if number not in [row[col_num] for row in sudoku]:  # check col

            # check square region
            region_row_start = 3 * (row_num // 3)
            region_col_start = 3 * (col_num // 3)
            for i in range(region_row_start, region_row_start + 3):
                for j in range(region_col_start, region_col_start + 3):
                    if sudoku[i][j] == number:
                        return False
            return True
    return False


def brute_force(sudoku):
    global backtracks
    cell = find_cell_to_fill(sudoku)
    if not cell:
        print("Solved")
        return True

    i, j = cell
    for number in range(1, 10):
        if is_valid(sudoku, i, j, number):
            sudoku[i][j] = number
            if brute_force(sudoku):
                return True
            backtracks += 1
            sudoku[i][j] = 0
    return False


def main(sudoku):
    # print_sudoku(sudoku)
    draw_soduku(soduku=sudoku)
    t0 = time.perf_counter()
    brute_force(sudoku)
    t1 = time.perf_counter()
    draw_soduku(soduku=sudoku, text="Soduku Solution", file_name="solution.png")
    print(backtracks)
    print(f"time taken: {(t1-t0):.4f} seconds")
    # print_sudoku(sudoku)



main(puzzle.random)
