"""
The temperature of the air is measured each hour so that after several days a long sequence of values is obtained. This data is required to be more smooth to avoid random jumps in values.
To achieve this, every value is to be substituted by the average of it and its two neighbors. For example, if he have the sequence of 5 values like this:
3 5 6 4 5
- Then the second (i.e. 5) should be substituted by (3 + 5 + 6) / 3 = 4.66666666667,
- the third (i.e. 6) should be substituted by (5 + 6 + 4) / 3 = 5,
- the fourth (i.e. 4) should be substituted by (6 + 4 + 5) / 3 = 5.
- By agreement, the first and the last values will remain unchanged.

"""

num = int(input('Enter number of entries: '))
weather = [0]*num
smoothWeather = [0] * num

weather = input(f'Enter {num} temperatures: ').split()
weather = [int(i) for i in weather]

smoothWeather[0], smoothWeather[num - 1] = weather[0], weather[num - 1]

for i in range(1,num-1):
    smoothWeather[i] = (weather[i - 1] + weather[i] + weather[i + 1]) / 3

print('\nSmoothened values: ',smoothWeather)