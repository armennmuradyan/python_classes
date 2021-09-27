my_tuple = (1, "Text", 1, True)
my_tuple_1 = 1, "Text", 1, True
single_tuple = (1,)

print(type(my_tuple))
print(len(my_tuple_1))

for item in my_tuple:
    print(item)

print('Text' in my_tuple)

text = "text"
new_tuple = tuple(text)
print(new_tuple)

print(my_tuple_1.count(1))
print(f'the index of one is {my_tuple_1.index(1, 1)}')

del my_tuple

text = ''
for item in new_tuple:
    print(item)
    text += item

print(text)


def tuple_to_string(my_tuple: tuple) -> str:
    text_ = ''

    for item_ in my_tuple:
        text_ += str(item_)

    return text_


new_tup = ('t', 'e', 'x', 't', 4, 5, '4')

word = "".join(new_tup)
print(word)

second_tuple = (1,)
result = new_tup + second_tuple
print(result)
a = tuple()
print(tuple_to_string(new_tuple))
num = 5
types = (int, float)

if type(num) in types:
    pass


my_list = []
print(id(my_list))
my_list.append(5)
my_list.append(5)
my_list.append(5)


my_list.insert(1, 4.5)
print(my_list.index(4.5))

print(my_list, id(my_list))
my_list.remove(5)
print("after", my_list, id(my_list))

print(my_list.pop(0))
print("after", my_list, id(my_list))
del my_list[:1]
print("after del", my_list, id(my_list))

my_list.clear()

print("after clear", my_list, id(my_list))

my_list_1 = [(1, [5, 6])]
print(my_list_1[0])
print(my_list_1[0][1])
print(my_list_1[0][1][1])
my_tuple = ([4, 5], 5)
my_tuple[0].append("new one")
print(my_tuple)
from copy import deepcopy

sample_list = [[4, 5], 4, "name"]
sample_list_2 = sample_list
sample_list.append(5)
print(sample_list_2 is sample_list)
print(sample_list_2)

sample_list_3 = sample_list.copy()
sample_list.append(9)
print(f"origin {sample_list} copied {sample_list_3}")

sample_list[0].append('wonder')
print(f"origin {sample_list} copied {sample_list_3}")

sample_list_4 = deepcopy(sample_list)
sample_list.clear()
print(f"origin {sample_list} deepcopied {sample_list_3}")

sample_list = [[4, 5], 4, "name"]

sample_list.extend([4, 5])

print(sample_list)


list_1 = list()

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