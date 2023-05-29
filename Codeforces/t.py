
from math import  comb
from itertools import  combinations
if __name__ == '__main__':

    ar=[i for i in range(5)]
    a = combinations(ar,3)
    y = [value for value in  a]
    print(y)

