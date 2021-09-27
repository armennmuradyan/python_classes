# def foo(*args):
    # # for a in args:
        # # a = a.upper()
        # # print(a)
#     print(f"the type of args is {type(args)}")
#     print(*args, sep = "------") # print("a", "b", "c", "d", sep = "------")
# foo("a", "b", "c", "d")
#
# def sum_elements(*elements):
#     sum_ = 0
#     for e in elements:
#         sum_ += e
#
#     return sum_
#
# print(sum_elements(1, 2, 3, 4))
#
# name_tuple = ("Nikita", "Max", "Armen", "Narek")
# print(*name_tuple, sep = "\n")


# def foo(name, *args):
#     for a in args:
#         a = a.upper()
#         print(a)
#     print(f"the type of args is {type(args)}")
#     print(*args, sep = "------") # print("a", "b", "c", "d", sep = "------")
#
#
# foo("name")
# foo()


# number = input("tell me the number and see the half of it\n")

# try:
#     number = int(number)
# except ValeError:
#     print("this is not a number so you'll get 0")
#     number = 0

# half = number/2

# print(half)

# number = input("tell the number and I'll return the half of it: ")
# try:
#     half = float(number) 

# except ValueError:
#     print("print only numbers")

# except ValueError:
#     num_1 = int(input("tell me number only number"))


from typing import Type


password = input("tell the password! ")
try:
    if len(password) < 8:
        raise ValueError("at least 8 symbols ")
    
    check = True 
    for i in password:
        if i.isalpha() and i.isupper():
            check = False
    if check:
        raise TypeError("Password should contain at least one uppercase character: ")
    
    check_symbols = True
    for i in password:
        if not i.isaplpha() and not i.isdigit() and i != " ":
            break
    else:
        raise TypeError("password should contain at least one symbol")    
except:
    pass