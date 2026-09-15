n=int(input("Enter 4 digits:"))
n1=int(n/1000)%10
n2=int(n/100)%10
n3=int(n/10)%10
n4=n%10
if n1==n4 and n2==n3:
    print("1")
else:
    print("0")

