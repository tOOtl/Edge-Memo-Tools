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
    input("Press enter.")
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
        solves[solveNumber] = [float(t), True]
    else:
        print('Incorrect ' + t + 's')
        solves[solveNumber] = [float(t), False]
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

def stats():
    allTimes = [solves[x][0] for x in solves]
    print('Mean of all attempts: ' + str(sum(allTimes)/len(allTimes))[:decimalTrim(allTimes)])
    correctTimes = [solves[x][0] for x in solves if solves[x][1] == True]
    print('Mean of correct attempts: ' + str(sum(correctTimes)/len(correctTimes))[:decimalTrim(correctTimes)])

def decimalTrim(times):
    divLength = len(str(sum(times)/len(times)))
    integralLength = len((str((sum(times)/len(times))//1)))
    if divLength < integralLength + 2:
        return
    else:
        return (integralLength + 2)


# start

end = ''

solves = {}
solveNumber = 0

print('Press enter when prompted to generate a sequence to memo. Press enter again to move onto recall.')

# main loop

while end.lower() != 'q':
    solveNumber += 1
    if end.lower() == 's':
        stats()
    else:
        memo()
    end = input('Enter "q" to quit, "s" to view stats, or press enter for another letter sequence.')

stats()
