a=input("Enter The Character to Verify, Whether it is which weekday: \n")

match a:
    case '1':
        print("1 is a Sunday")
    case '2':
        print("2 is a Monday")
    case '3':
        print("3 is a Tuesday")
    case '4':
        print("4 is a Wednesday")
    case '5':
        print("5 is a Thursday")
    case '6':
        print("6 is a Friday")
    case '7':
        print("7 is a Saturday")
    case _:
        print(a," is not a Day")