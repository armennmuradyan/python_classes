from random import randint

def play_game():
    user_choise = int(input("rock, paper or scissors? 1 for rock, 2 for paper, 3 for scissors: "))
    computer_choise = randint(1, 3)
    checker_1 = True
    while checker_1:
        if user_choise > 3 or user_choise < 1:
            print("value is not valid")
            user_choise = int(input("rock, paper or scissors? 1 for rock, 2 for paper, 3 for scissors: "))
        else:
            checker_1 = False
    print(f"user choise is {user_choise}")
    print(f"computer choise is {computer_choise}")
    if user_choise == 1 and computer_choise == 3:
        return "you won!"
    elif user_choise == 2 and computer_choise == 1:
        return "you won!"
    elif user_choise == 3 and computer_choise == 2:
        return "you won!"
    elif user_choise == computer_choise:
        return "draw"
    else:
        return "you lose("

print(play_game())