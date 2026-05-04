ch=input("Enter The Character to Verify, Whether it is which month: \n")

match ch:
    case '1':
        print("1 is a January")
    case '2':
        print("2 is a February")
    case '3':
        print("3 is a March")
    case '4':
        print("4 is a April")
    case '5':
        print("5 is a May")
    case '6':
        print("6 is a June")
    case '7':
        print("7 is a July")
    case '8':
        print("8 is a August")
    case '9':
        print("9 is a September")
    case '10':
        print("10 is a October")
    case '11':
        print("11 is a November")
    case '12':
        print("12 is a December")
    case _:
        print(ch," is not a Month")