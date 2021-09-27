a = int(input("enter any number: "))
x = 1
for i in range(a+1):
    if i <= 0:
        continue
    else:
        x = x*i
print(f"The factorial of {a} is {x}")