


def intro():
    low = input("Enter the lowest range ==>")
    high = input("Enter the highes range ==>")

    low = int(low)
    high = int(high)

    if low > high:
        return intro()



    while low <= high:

        print("192.168.1.%s" % low)

        low += 1


intro()