#ex 1
from random import sample


char = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*()[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQWSTUVWXYZ"
password_len = int(input('Enter the length of the password: '))
password_res = "".join(sample(char, password_len))
print(password_res)

#ex2
from random import randint
a = randint(1,100)
b = int(input("how many numbers you want?: "))
c = int(input("in what range?: "))
for i in range(1,b+1):
   a = randint(1,c-c/2)
   print(a*2)
   

