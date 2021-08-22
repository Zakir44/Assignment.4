#Accept number from user and calculate the sum of all number from 1 to a given number
a = int(input("Enter The Value: "))

SUM = 0

for i in range(a, 0, -1):

 SUM = SUM+i

print("Sum :", SUM)
