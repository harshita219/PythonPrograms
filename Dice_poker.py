"""
Dice game of Yacht is played with 5 standard dice (having from 1 to 6 points on their sides). The player's goal is to gather some beautiful combination of points. Suppose, the following combinations are respected:

` two of dice have the same points, like 3 6 5 6 1  called pair;
` three of dice have the same points, like 2 4 5 4 4 - called three;
` four of dice have the same points, like 1 4 1 1 1 - called four;
` all five dice have the same points, like 2 2 2 2 2 - called yacht;
` two pairs at once, like 3 6 5 3 5 - called two-pairs;
` pair and three at once, like 1 6 6 1 6 - called full-house;
` sequence from 1 to 5, like 2 4 3 5 1 - called small-straight (see notes);
` sequence from 2 to 6, like 6 3 4 2 5 - called big-straight.

"""

def dice(nums):
    twice = 0
    thrice = 0

    for i in range(1,7):
        for item in nums:
            if item == i:
                check[i] += 1

    for item in check:
        if item == 2:
            twice += 1
        elif item == 3:
            thrice += 1
        elif item == 4:
            return 'Four'
        elif item == 5:
            return 'Yatch'

    if twice == 1 and thrice == 1:
        return 'Full house'
    elif twice == 1:
        return 'Pair'
    elif twice == 2:
        return 'Two pair'
    elif thrice == 1:
        return 'Three'
    elif list(range(1,6)) == nums:
        return 'Small-straight'
    elif list(range(2,7)) == nums:
        return 'Big-straight'
    else:
        return None

mylist = input('Enter five dice points: ').split()

# A list to store number of occurances of each number on dice
check = [0]*7

mylist = [int(i) for i in mylist]
mylist.sort()
print(dice(mylist))

