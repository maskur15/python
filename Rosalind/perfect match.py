#https://rosalind.info/problems/pmch/
from math import factorial

seq = 'UCACCGGGUCUUCUCAGGGGAAGUUCCUAGGUAAUGAGGCUUUCCAAAAUACAGGUUAGCCCAGUAAAUCCAUU'

match = factorial(seq.count('U')) * factorial(seq.count('G'))
print(match)