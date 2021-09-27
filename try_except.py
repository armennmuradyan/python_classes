x = input("tell the first number: ")
y = input("tell the second number: ")
check = True 
while check:
    try:                           # porcuma ani meji grac gorcoxutyuny
        res = float(x)/float(y)
        print(res)
    except ValueError: #ete gorcoxutyune aneluc heto stanumenq ValueError 
        print("tell only numbers") #anuma excepti meji gorcoxutyune
    except ZeroDivisionError: # nuyne ZeroDivisionError-ov 
        print("Error: It is impossible to divide into zero!")
    else:                    # else ashxatuma menak ete amen inch normala
        print("all is ok")
    finally: # finally ashxatuma misht!
        print("ok, try again")
    que = input("Play again, no for exit: ")
    if que == "no":
        check = False
# -------------------------------??????????

# RAISE

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")