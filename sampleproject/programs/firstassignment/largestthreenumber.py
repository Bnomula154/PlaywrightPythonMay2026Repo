#Largest among three numbers
a = int(input("Enter the value:"))
b = int(input("Enter the value:"))
c = int(input("Enter the value:"))
if(a > b and a > c):
    print("A is Largest",a)
elif(b > c and b > a):
    print("B is Largest",b)
else:
    print("C is largest:",c)