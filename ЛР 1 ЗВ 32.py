import math
first=int(input("Enter the size of the first side:"))
second=int(input("Enter the size of the second side:"))
third=int(input("Enter the size of the third side:"))
p=int((first+second+third)/2)
print(math.sqrt(p*(p-first)*(p-second)*(p-third)))
