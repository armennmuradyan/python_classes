count_ = 0
for i in range(1,21):
    if i == "3":
        continue
    elif i == "13":
        continue
    else:
        count_ += int(i)
print(count_)

count_ = 0
for i in range(1,21):
    if i < 15:
        count_ += int(i)
    if i == '15':
        break
print(count_)

# ___________________________Ex1


y = 5
x = 5
for i in range(y):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(x):
    for j in range(i):
        print('* ', end="")
    print('')

# __________________________Ex2


b = 1 
for i in range(1,10):
    b += 1
    print(f"{i} x {b} = {i*b}")


# __________________________Ex3

x = int(input("enter any number: "))
if x%2 == 0: 
    print(x/2)
else:
    print("error")



# ___________________________Ex5

a = 0
b =1
while b<51:
    print(b)
    a,b = b,a+b