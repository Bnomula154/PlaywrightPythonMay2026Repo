#find number of Digits in a given number
x=int(input("Enter the value:\n"))
if(x>=0 and x<=9):
    print("The value is 1")
elif(x>=10 and x<=99):
    print("The value is 2")
elif(x>=99 and x<=999):
    print("The value is 3")
elif(x>=1000 and x<=9999):
    print("The value is 4")
elif(x>=10000 and x<=99999):
    print("The value is 5")
else:
    print("The value is more than 5")