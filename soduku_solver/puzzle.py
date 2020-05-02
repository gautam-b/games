from bs4 import BeautifulSoup, element
import requests
from typing import List, Optional

diabolical = [
    [4, 0, 7, 0, 0, 0, 6, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 8, 0, 0, 2],
    [0, 6, 0, 0, 0, 3, 5, 0, 0],
    [0, 5, 0, 8, 0, 0, 7, 4, 0],
    [0, 9, 0, 0, 7, 0, 8, 0, 1],
    [0, 0, 0, 1, 0, 2, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 6, 0, 5, 0, 0, 0, 0],
]

evil = [
    [0, 9, 0, 6, 3, 0, 0, 0, 0],
    [5, 1, 0, 0, 9, 0, 4, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 6, 9],
    [7, 2, 0, 1, 0, 0, 0, 0, 6],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 9, 0, 0, 6, 0, 0, 1],
    [0, 0, 0, 5, 0, 7, 0, 0, 2],
]


hrd = [
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 3, 0, 7, 0, 0, 6, 0, 4],
    [0, 6, 4, 0, 9, 8, 0, 0, 0],
    [4, 7, 0, 1, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 3, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 4, 0, 1, 7],
    [0, 0, 0, 4, 6, 0, 2, 5, 0],
    [8, 0, 9, 0, 0, 5, 0, 3, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
]

easy0 = [
    [8, 5, 0, 3, 6, 0, 7, 0, 0],
    [0, 3, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 1],
    [0, 1, 0, 0, 8, 9, 0, 0, 7],
    [5, 0, 0, 6, 1, 0, 0, 0, 0],
    [0, 7, 0, 5, 3, 0, 6, 1, 4],
    [1, 6, 0, 7, 0, 0, 0, 8, 0],
    [2, 8, 5, 1, 9, 3, 4, 0, 0],
    [0, 0, 9, 8, 2, 6, 0, 0, 5],
]

easy1 = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

easy2 = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [0, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 0, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 3, 0, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

medium = [
    [1, 0, 5, 7, 0, 2, 6, 3, 8],
    [2, 0, 0, 0, 0, 6, 0, 0, 5],
    [0, 6, 3, 8, 4, 0, 2, 1, 0],
    [0, 5, 9, 2, 0, 1, 3, 8, 0],
    [0, 0, 2, 0, 5, 8, 0, 0, 9],
    [7, 1, 0, 0, 3, 0, 5, 0, 2],
    [0, 0, 4, 5, 6, 0, 7, 2, 0],
    [5, 0, 0, 0, 0, 4, 0, 6, 3],
    [3, 2, 6, 1, 0, 7, 0, 0, 4],
]

hard = [
    [8, 5, 0, 0, 0, 2, 4, 0, 0],
    [7, 2, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 7, 0, 0, 2],
    [3, 0, 5, 0, 0, 0, 9, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 7, 0],
    [0, 1, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 6, 0, 4, 0],
]

diff = [
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0],
]

#TODO Somehow fix this non-randomness
#id 1 = 6, 7 = 2

def format_html() -> element.ResultSet:
    default_gateway = "https://testdrive-archive.azurewebsites.net/Performance/Sudoku/Default.html"

    html = requests.get(default_gateway).text
    soup = BeautifulSoup(html, 'lxml')
    board_cells = soup.find_all('td', class_="boardCell")
    return board_cells


def html_to_array(board_cells: element.ResultSet) -> List[Optional[int]]:
    """ Returns the board_cells html data into one large array-like list of integers """
    cell_possibilities = [None for i in range(89)]
    for cell in board_cells:
        have_value = cell.find('div', class_="staticValue")
        if not have_value:
            have_value = cell.find('div', class_="editValue")
            value = 0
        else:
            value = int(cell.span.text)
        cell_possibilities[int(have_value.attrs['id'])] = value

    cell_singular = [i for i in cell_possibilities if i is not None]
    return cell_singular


def array_to_final_board(input_list: list) -> List[List[int]]:
    """ Returns the final board using output from html_to_array

    Precondition: <input_list> is of length 81
    """
    temp_final_list = []

    for i in range(9):
        row_list = list()
        for j in range(9):
            row_list.append(input_list[i*9 + j])
        temp_final_list.append(row_list)

    return fix_board(temp_final_list)


def fix_board(board_broken: List[int]) -> List[int]:
    """ Returns a transposed version of board_broken

    Precondition: <board_broken> is a list with 9 nested lists of size 9
    """
    final_board = list()
    for big_row_partition in range(3):
        row_1, row_2, row_3 = [], [], []
        for row_selection in range(3):
            row = board_broken[(big_row_partition * 3) + row_selection]
            row_1.extend(row[:3])
            row_2.extend(row[3:6])
            row_3.extend(row[6:])

        final_board.append(row_1)
        final_board.append(row_2)
        final_board.append(row_3)

    return final_board

daily = array_to_final_board(html_to_array(format_html()))


if __name__ == '__main__':
    for i in range(9):
        print(daily[i])
