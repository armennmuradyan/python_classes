import random

check_to_play = True
rounds = 0
computer_score = 0
user_score = 0
while check_to_play:
    # write the gam
    user_choice = "test"
    # validation of input
    while user_choice not in ('1', '2', '3'):
        user_choice = input('1 for Rock 2 for Paper 3 for Scissors\n')
    else:
        user_choice = int(user_choice)
    # computer_choice
    computer_choice = random.randint(1, 3)

    if computer_choice == user_choice:
        print("Draw")
    elif (computer_choice == 1 and user_choice == 2) or (computer_choice == 2 and user_choice == 3)\
            or (computer_choice == 3 and user_choice == 1):
        print("You Won !!!!")
        user_score += 1
    else:
        print("You Lost ((!!!!")
        computer_score += 1
    rounds += 1

    check_input = input("wanna play again? no for exit\n")
    if check_input == 'no':
        check_to_play = False

print(f'you have played {rounds} time and the results\nuser score - {user_score} and computer score - {computer_score}')