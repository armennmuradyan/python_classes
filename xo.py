import random
computer_random = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = ["_","_","_",
        "_","_","_",
        "_","_","_",]

def board_function():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def gamer_choose():
    x_or_o = input("X or O?, 1-X 2-O\n")
    if x_or_o == "1":
        pos = input("Choose a position from 1-9\n")
        pos = int(pos) - 1
        random_O = random.choice(computer_random)
        board[pos] = "X"
        if random_O != pos:
            board[random_O-1] = "O"
            print(f"computer choise = {random_O}")

    elif x_or_o == "2":
        pos = input("Choose a position from 1-9\n")
        pos = int(pos) - 1
        board[pos] = "O"
        random_X = random.choice(range(1,10))
        print(random_X)
    board_function()

gamer_choose()
