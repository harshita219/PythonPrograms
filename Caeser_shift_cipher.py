"""
Deciphering encrypted messages in this problem, the idea of the algorithm is simple. Each letter of the original text is substituted by another, by the following rule:

- find the letter (which should be encrypted) in the alphabet;
- move K positions further (down the alphabet);
- take the new letter from here;
- if "shifting" encountered the end of the algorithm, continue from its start.
- For example, if K = 3 (shift value used by Caesar himself), then A becomes D, B becomes E, W becomes Z and Z becomes C and so on.

"""

num = int(input('Enter number of lines to be entered: '))
k = int(input('Enter number of shift steps: '))

sentences = [''] * num
encrypted = [''] * num
alpha = list(x for x in 'abcdefghijklmnopqrstuvwxyz')

for i in range(num):

    sentences[i] = input(f'Enter line {i+1}: ').lower()

    for letter in sentences[i]:
        if letter in alpha:
            x = alpha.index(letter)
            x += k
            if x >= 26:
                x -= 26
            encrypted[i] += alpha[x]
        else:
            encrypted[i] += letter

for i in range(num):
    print('\nEncrypted line ',i,': ',encrypted[i])
















