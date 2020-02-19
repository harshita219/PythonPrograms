"""
Suffix Array is one of popular types of indexe sorting. We are going to see how it works and then try an exercise about creating one. The core idea of suffix-based data structures is like following:

- represent the whole data as a single text string (e.g. concatenate all electronic books into one file);
- the suffix is a substring starting at any position and running to the end of this text;
- so for string of N characters we have N different suffixes - let us extract them to some set or list;
- now we create some sorted structure of these suffixes - e.g. sorted array or binary tree;
- and we are ready to process requests - if we have some search word, we can find all suffixes which start with this word
- The only trouble is how to store this set of suffixes efficiently. The suffix array is probably the most compact way. Let us see how it looks like.

"""

word = input('Enter string: ')
suffixArray = []
indices = []

for i in range(len(list(word))):
    suffixArray.append([word[i:],i])

suffixArray = sorted(suffixArray)

for i in range(len(suffixArray)):
    print(suffixArray[i][0])
    indices.append(suffixArray[i][1])

print('-> Indices of respective suffix arrays: ',indices)
