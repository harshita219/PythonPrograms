"""
In arithmetic, the remainder (or modulus) is the amount "left over" after performing the division of two integers which do not divide evenly (from Wiki). This task will provide further practice with modulo operation.

Suppose, we are given two timestamps - for example:

start: May 3, 17:08:30
end  : May 8, 12:54:15
and we are curious to know, how much time (in days, hours, minutes and seconds) is spent in traveling. One of the easiest way is:

- convert both timestamps to big numbers, representing seconds from the beginning of the month (or year, or century);
- calculate their difference - i.e. travel time in seconds;
- convert this difference back to days, hours, minutes and seconds.

In this task we are given several pair of timestamps in format 'd h m s'. We suppose that both dates in the pair are always in the same month, so only number of day will be given.
We want to calculate difference between timestamps of given serial number.

"""

num = int(input('Enter number of entries: '))

d = [[]]*num
totalsec = [0] * num

for i in range(num):

    d[i] = input(f'{i+1}> Enter d h m s: ').split()
    # Storing one d/h/m/s value
    d[i] = [int(item) for item in d[i]]

    totalsec[i] = d[i][0] * 24 * 3600 + d[i][1] * 3600 + d[i][2] * 60 + d[i][3]

[x, y] = input('Enter serial number of two entries to find difference: ').split()

diff = abs(totalsec[int(x)-1] - totalsec[int(y)-1])
d = int(diff / (24*3600))
h = int( (diff % (24*3600))/3600)
m = int( ((diff % (24*3600))% 3600)/60 )
s = int( ((diff % (24*3600))% 3600)%60)

print(f'\n Difference is is {d} day {h} hrs {m} mins {s} secs')

