import time
import puzzle

backtracks = 0


def print_sudoku(sudoku):
    for i, row in enumerate(sudoku):
        if i in [3, 6]:
            print("-" * 29)
        print(row[:3], end=" ")
        print(row[3:6], end=" ")
        print(row[6:9])


def find_cell_to_fill(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return False


def is_valid(sudoku, row_num, col_num, number):
    if number not in sudoku[row_num]:  # check row
        if number not in [row[col_num] for row in sudoku]:  # check col
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
    print_sudoku(sudoku)
    t0 = time.perf_counter()
    brute_force(sudoku)
    t1 = time.perf_counter()
    print_sudoku(sudoku)
    print(backtracks)
    print(f"time taken: {(t1-t0):.4f} seconds")


main(puzzle.diabolical)
