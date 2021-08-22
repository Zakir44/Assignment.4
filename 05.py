list1 = [10, 5, 30, 12, 55, 75, 22, 13, 10, 80, 20]


for item in list1:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)