from random import randint, gauss
from time import time

letters = "A B C D E F G H I J L M N O P Q R S T V W X".split()

def genPairs():
    #gen a list, length normally distributed around 11
    pairs = []
    length = int(gauss(11, 1))
    lett = letters[randint(0, 21)]
    pairs.append(lett)
    for i in range(1, length):
        lett = letters[randint(0, 21)]
        while lett == pairs[len(pairs) - 1]:
            lett = letters[randint(0, 21)]
        pairs.append(lett)
    # prints the letters in pairs, as they would be memorised
    r = 0
    for i in pairs:
        if r % 2 == 0:
            print(i, end = '')
        else:
            print(i, end = ' ')
        r += 1
    return pairs

def memo():
    #prints a list of pairs, hides them on command, and the checks recall
    input("Press enter to begin. Press enter again when you have memorised the list.")
    pairs = genPairs()
    start = time()
    input()
    end = time()
    t = str((end - start))[:-13]
    print('\n'*50) # cheap way to hide the pair list while you recall
    # checks recall against the correct pairs
    recall = input('Type memo here (no spaces): ')
    recall = [x.upper() for x in recall]
    if recall == pairs:
        print('Correct ' + t + 's')
    else:
        print('Incorrect ' + t + 's')
        if len(pairs) != len(recall):
            print('Length of recall does not match pairs')
        # Displays errors in recall, caps for incorrect letters, lower case for correct letters
        errors = []
        for i in range(min(len(pairs), len(recall))):
            if pairs[i] == recall[i]:
                errors.append(pairs[i].lower())
            else:
                errors.append(pairs[i].upper())
        if len(pairs) > len(recall):
            errors.append(''.join(pairs)[-(len(pairs) - len(recall)):])
        print('Errors in caps: ' + ''.join(errors))
                   
memo()
