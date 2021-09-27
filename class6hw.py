# _____________________Ex1

x = int(input("Tell the first number: "))
y = int(input("Tell the second number: "))
z = int(input("Tell the third number: "))


def function(frst, scnd, thrd):
    s = (frst+scnd+thrd)/2
    res = (s*(s-frst)*(s-scnd)*(s-thrd)) ** 0.5
    return res


print(function(x, y, z))

# _____________________Ex2

string_ = str(input("text any symbols: "))


def reverse_str(name):
    return name[::-1]


print(reverse_str(string_))


# _______________________Ex3

txt = input("enter any text\n")


def function(name):
    upp = 0
    low = 0
    for i in name:
        if i.islower():
            low += 1
        elif i.isupper():
            upp += 1
    return low, upp


print(function(txt))
