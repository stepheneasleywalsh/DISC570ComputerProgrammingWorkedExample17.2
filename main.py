x = int(input("Number > 0 or < 10 please: "))

if x <= 0:
    print("That is too small")

if x >= 10:
    print("That is too big")

if x > 0:
    if x < 10:
        print("Thank you")
