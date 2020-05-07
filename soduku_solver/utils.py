def print_sudoku(sudoku):
    for i, row in enumerate(sudoku):
        if i in [3, 6]:
            print("-" * 29)
        print(row[:3], end=" ")
        print(row[3:6], end=" ")
        print(row[6:9])

