import numpy.random as random
'''
LAB 3 - Minesweeper
Little messy, but works. User input is considered 1 = 1, not 1 = 0 (1 1 is equal to first cell in first row)
Ask user for size of board and amount of mines
Create empty board equal to users demands + padding (removes need to consider out of bounds), then populate it with bombs, then populate the non-bomb cells with amount of neighbors (i.e adjacent cells who are bombs)
Print the board (without padding), but mask every cell except what ever the user guesses as questionmarks
Check if users x,y input is equal to a bomb, if so quit the game
Check if amount of guesses (minus duplicates) is equal to amount of cells minus bombs, in which case the user has guessed every cell except the bombs, so user wins
'''

def init_board(width, height, mines_num):
    board = [[0 for x in range(width+2)] for y in range(height+2)]
    mine_cords = get_mines(board, mines_num)
    for x, y in mine_cords:
        board[x][y] = '*'
    get_neighbors(board)
    return board

def get_mines(board, mines_num):
    mines = []
    for _ in range(mines_num):
        random_cell = get_random_cell(board)
        # Avoid duplicate mines, not very efficient but works
        while True: 
            if random_cell not in mines:
                mines.append(random_cell)
                break
            else:
                random_cell = get_random_cell(board)
    return mines

def get_random_cell(board):
    height = len(board)
    width = len(board[0])
    x = random.choice(range(1, height - 1))
    y = random.choice(range(1, width - 1))
    return (x,y)

def get_neighbors(board):
    # For each cell, check every adjacent cell for bombs, add neighbor to list if bomb, finally change cell to show number of neighbors who are bombs
    height, width = len(board), len(board[0])
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            if board[x][y] != '*':
                neighbors = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        elif board[x+i][y+j] == '*':
                            neighbors.append(1)
                board[x][y] = len(neighbors)

def print_board(board, user_cords):
    for x in range(1, len(board) - 1):
        for y in range(1, len(board[x]) - 1):
            if (x, y) in user_cords:
                print(board[x][y], end = " ")
            else:
                print('?', end = " ")
        print()

def get_cords(cords):
    tmp = cords.split(" ")
    x, y = int(tmp[0]), int(tmp[1])
    return x, y

def check_win(board, mines_num, user_cords):
    # Remove padding before checking if number of cells is equal to length of users inputs minus number of mines
    height, width = len(board) - 2, len(board[0]) - 2
    return len(set(user_cords)) == (height * width) - mines_num

def check_lose(board, user_cords):
    x, y = user_cords[-1][0], user_cords[-1][1]
    return board[x][y] == '*'

def main():
    board_size = input("Enter width an size of board, seperated by space: ").split(" ")
    board_width, board_height = int(board_size[0]), int(board_size[1])
    mines_num = int(input("Number of mines (max {}): ".format(board_width * board_height)))
    board = init_board(board_width, board_height, mines_num)
    user_cords = []
    user_input = None

    while True:
        print_board(board, user_cords)
        print("To exit, enter 'x'")
        user_input = input("Enter coordinates (separated by space): ")
        user_cords.append(get_cords(user_input))
        
        if user_input == 'x':
            break
        elif check_lose(board, user_cords):
            print_board(board, user_cords)
            print("You lost")
            break
        elif check_win(board, mines_num, user_cords):
            print_board(board, user_cords)
            print("You win!")
            break
            

if __name__ == "__main__":
    main()