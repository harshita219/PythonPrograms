"""
A number is called happy if it leads to 1 after a sequence of steps where in each step number is replaced by sum of squares of its digit
That is if we start with Happy Number and keep replacing it with digits square sum, we reach 1.
This program prints first 10 happy numbers.

"""

def happy(num):
    sum = 0
    while num>0:
        sum += (num%10)**2
        num = int(num/10)
    if sum == 1:
        return True
    elif sum < 10:
        return False
    else:
        return happy(sum)

ctr, i = 0, 0
print('Showing first 10 happy numbers...')
while ctr < 10:
    num = i
    if happy(i):
        print(num)
        ctr += 1
    i = num + 1

