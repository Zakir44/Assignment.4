# Given two integer numbers return their product. If the product is greater than 1000, then return their sum.
a = int(input("Enter your value: "))
b = int(input("Enter your value: "))
p = 0
p = a*b
if p > 1000:
    Z = a+b
    print("Sum  is : ", a+b)
else:
 print("Product is :", a*b)
