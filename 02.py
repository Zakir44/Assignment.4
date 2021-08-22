#Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration
 #print the sum of the current number and previous number

num = list(range(10))
previousNum = 0
for i in num:
    sum = previousNum + i
    print('CN '+ str(i) + ' PN' + str(previousNum) + 'is ' + str(sum))
    previousNum =i