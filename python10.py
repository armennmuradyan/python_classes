# list_1 = [(i, i*i) for i in range(11)]

# a = int(input("tell number and see the half\n"))

# half_number = a/2 if a%2 == 0 else a // 2

# print(half_number)


# list_2 = [i if i == 0 else i*i for i in range(11) if i%2 == 0]
# print(f"list values are {list_2}")

# dict_1 = {key: key*key for key in range(11)}
# print(dict_1)
# dict_1 = {key: key if key == 0 else key*key for key in  range(11) if key % 2 == 0}
# print(dict_1)



# import sys

# gen_1000 = (i if i == 0 else i*i for i in range(5))
# list_1000 = [i if i == 0 else i*i for i in range(1000)]
# print(type(gen_1000))
# print(next(gen_1000))

# x = input("tell any word\n")
# gen_upper_letters = (letter for letter in x if letter.isupper())

# for item in gen_upper_letters:
#     print(item)

# def my_generator():
#     print(10)
#     yield
#     print(30)
#     yield

# first_one = my_generator()
# print(first_one)

# def my_generator(end,start = 0 ,step = 1):
#     for element in range(start, end, step):
#         yield element

# g_2 = my_generator(5)
# g_3 = my_generator(start = 10, end = 0, step = -1)
# print(next(g_2))
# print(next(g_2))
# print(next(g_3))
# print(next(g_2))


def my_generator(end):
    i = 0
    b=1
    while True:
        yield i
        i,b += b,i+b

gen_4 = my_generator(5)
print(next(gen_4))
print(next(gen_4))
print(next(gen_4))
print(next(gen_4))
print(next(gen_4))
print(next(gen_4))
print(next(gen_4))
print(next(gen_4))
print(next(gen_4))
print(next(gen_4))
print(next(gen_4))