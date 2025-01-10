def bottles():
    milk = 99
    for i in range(99):
        milk = milk - 1
        print(str(milk) + " bottles of milk on the wall")
        print(str(milk) + " bottles of milk on the wall")
        print("Take one pass it around")
        if milk == 1:
            print("1 bottle of milk on the wall")
            print("1 bottle of milk on the wall")
            print("Take it done pass it around")
        elif milk == 0:
            print("No more bottles of milk on the wall")
            print("Boo Hoo!")

bottles()
