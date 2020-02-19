"""
This is one of the most mysterious math problems of the last century - both because its statement is extremely simple - and because the proof is still unknown. However it offers good programming exercise.
Suppose we select some initial number X and then build the sequence of values by the following rules:

if X is even (i.e. X modulo 2 = 0) then
    Xnext = X / 2
else
    Xnext = 3 * X + 1

That is, if X is odd, sequence grows - and if it is even, sequence decreases. For example, with X = 15 we have sequence:
15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1
After the sequence reaches 1 it enters the loop 1 4 2 1 4 2 1....

The intrigue is in the fact that any starting number X gives the sequence which sooner or later reaches 1 - however though this Collatz Conjecture was expressed in 1937, up to now no one could find a proof that it is really so for any X or could not find a counterexample.
Task is to calculate how many steps are necessary to come to 1 for given numbers.

"""

num = int(input('Enter number:  '))
c=0
while num>1:
    if num%2==0:
        num = num/2
    else:
        num = num*3 + 1
    c += 1
    if num==1:
        break
print('No. of steps in collatz sequence: ',c)