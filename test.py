import time

x = 1000
j = 1007
while x > 0:
    x -= 7
    j -= 7
    time.sleep(0.08)
    print(f"{j}-7 = {x}")