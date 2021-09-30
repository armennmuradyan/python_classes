##5. Write a python script to find the highest of given three numbers


# a = [15, 56, 1, -3, 465, 77, 29]
# a.sort()
# print(a[-1])



##write a python program to check leap year without using datetime library (google for conditions)


# year = int(input('Enter the year: '))
# if year % 400 == 0:
#    print("leap year")
# elif year % 100 == 0:
#    print("no leap year")
# elif year % 4 == 0:
#    print("leap year")
# else:
#    print("no leap year")


## Write a Python program to add ‘ing’ at the end of a given string (length should be at least 3). 
## If the given string already ends with ‘ing’ then add ‘ly’ instead.
## If the string length of the given string is less than 3, leave it unchanged.
 

# def myfunction():
#    ing_ly = input("Enter any word: ")
#    if len(ing_ly) < 3:
#       print(ing_ly)
#    elif ing_ly.endswith("ing"):
#       print(ing_ly +"ly")
#    else:
#       print(ing_ly + "ing")
      

# myfunction()



## Write a Python program to get a string from a given string where all occurrences of its 
## first char have been changed to ‘$’, except the first char itself. 


# a = input("enter any word: ")

# def dollar(name):
#    frst = name[0]
#    name = name.replace(frst, "$")
#    name = frst + name[1:]
#    return name
# print(dollar(a))


## Write a python program to count number even of digits in a string


# txt = [1, 12, 54, 43, 44, 88, 965, 47, 5]

# def evennums(name):
#    count_ = []
#    for i in name:
#       if i % 2 == 0:
#          count_.append(i)
#    return count_

# print(evennums(txt))


