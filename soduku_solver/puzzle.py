from bs4 import BeautifulSoup, element
import requests
from typing import List
from utils import print_sudoku


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


def format_html() -> element.ResultSet:
    """ Formats the html for a randomly selected sudoku board in such a manner that only table rows which correspond
    to rows of the board are kept """
    html = requests.get("https://nine.websudoku.com/").text
    soup = BeautifulSoup(html, 'lxml')

    board_rows_html = soup.find('table', class_='t').find_all('td')
    return board_rows_html


def html_to_array(board_rows: element.ResultSet) -> List[List[int]]:
    """ Returns the board_rows html data into one 2-dimensional  """
    final_board, row_list = list(), list()

    for cell in board_rows:

        if len(row_list) >= 9:
            final_board.append(row_list)
            row_list = []

        try:
            value_cell = int(cell.input['value'])
        except KeyError:
            value_cell = 0

        row_list.append(value_cell)

    # Final row
    final_board.append(row_list)

    return final_board


random = html_to_array(format_html())


if __name__ == '__main__':
    print_sudoku(random)
