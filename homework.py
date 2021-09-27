#ex1
before_ = [17, 11, 17, 11, 23, 7]
after_ = []
for i in before_:
    if i not in after_:
        after_.append(i)
print(after_)
#ex1.1

frst = [10, 12, 36, 44, 77, 85, 113, 231, 344, 4655, 789]
scnd = [10, 12, 35, 45, 77, 85, 113, 231, 340, 4655, 789, 2, 6]
res = []

for i in frst:
    if i in scnd and i not in res:
        res.append(i)
print(res)


#ex 2

divisors = [10, 12, 36, 44, 77, 85, 113, 231, 344, 4655, 789]
res = []
for i in divisors:
    if i % 5 == 0:
        res.append(i)
print(res)

#ex3
txt = input("enter any text: ")
def function(name):
    x = txt.split()
    res = x[::-1]
    return res

print(function(txt))

#ex4

my_tuple = ("armen", 16, "Muradyan")
print(my_tuple[::-1])

#ex5
my_list = ["armen", True, 0, False, "Hello", 34, 35.5, 3.3]
str_ = []
bool_ = []
int_ = []
float_ = []
for i in my_list:
    if type(i) == str:
        str_.append(i)
    elif type(i) == bool:
        bool_.append(i)
    elif type(i) == int:
        int_.append(i)
    elif type(i) == float:
        float_.append(i)
print(str_)
print(int_)
print(float_)
print(bool_)

#ex6?
