import random
from collections import Counter
loop_while = True
lst_dice=[]
counter = 0
while counter < 5:
    for i in range(1, 10000):
        dice = str(random.randrange(1, 6, 1))
        lst_dice.append(dice)
        frequence_dice = Counter(lst_dice)
    print(frequence_dice)
    counter += 1
