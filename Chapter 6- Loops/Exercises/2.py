while True:
    Age=int(input("How old is the customer:"))

    if Age < 3:
        price=0

    if Age < 12:
        price=10

    if Age > 12:
        price=15
    
    if Age == 0:
        break

print("You're ticket is", price)