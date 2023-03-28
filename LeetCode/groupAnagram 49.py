#https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict
if __name__ == '__main__':
    strs=list(input().split())
    d= defaultdict(list)
    for x in strs:
        word= ''.join(sorted(x))
        d[word].append(x)
    print(d.values())