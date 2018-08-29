import math
import os
import random
import re
import sys
from operator import lt, gt


def compareTriplets(a, b):

    result = [0, 0]
    x = map(gt, a, b)
#    print(list(x))
    for i in list(x):
        if i == True:
            result[0] += 1
        else:
            pass
    y = map(gt, b, a)
#    print(list(y))
    for i in list(y):
        if i == True:
            result[1] += 1
        else:
            pass
    return result


a = [1, 2, 3, 4, 8, 9]
b = [1, 2, 3, 4, 8, 9]
print(compareTriplets(a, b))
