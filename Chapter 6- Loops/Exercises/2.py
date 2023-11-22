while True:
    Age=int(input("How old is the customer:"))

    if Age < 3:
        print("Ticket is free")

    if Age < 13:
        print("Ticket is 10")

    if Age > 12:
        print("Ticket is 15")
    
    if Age == 0:
        break