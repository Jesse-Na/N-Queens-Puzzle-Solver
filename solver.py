from typing import List, Tuple

board_number = 1


def print_board(board: List[List[int]]):
    global board_number
    print("Solution " + str(board_number) + "\n")
    board_number += 1
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print("")
    print("")


def solve(board: List[List[int]], row: int):
    # Base case
    if row >= len(board):
        print_board(board)
        return True

    # Recursive case
    solved = False
    for col in range(len(board)):
        if valid(board, (row, col)):
            board[row][col] = 1
            solved = solve(board, row + 1) or solved
            board[row][col] = 0

    return solved


def generate_all_solutions(size: int):
    #
    board = [[0 for j in range(size)]
             for i in range(size)]

    if not solve(board, 0):
        print("Solution does not exist")
        return
    return


def valid(board: List[List[int]], pos: Tuple[int, int]):
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == 1 and pos[0] != i:
            return False

    # Check diagonal
    diagonal_flag = True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                delta_x = abs(i - pos[0])
                delta_y = abs(j - pos[1])
                if delta_x == delta_y:
                    diagonal_flag = False

    return diagonal_flag


if __name__ == '__main__':
    # Input your board size
    generate_all_solutions(4)
