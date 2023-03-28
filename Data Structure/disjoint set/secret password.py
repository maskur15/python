##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
# BY-GK
import sys

input = sys.stdin.readline
parent=[i for i in  range(26)]
def findParent(v):
    if v!=parent[v]:
        parent[v]=findParent(parent[v])
    return parent[v]
def union(u,v):
    a=findParent(u)
    b=findParent(v)
    if a!=b:
        parent[a]=b
if __name__ == '__main__':
    visit=[False]*26
    for _ in range(int(input())):
        s=input().rstrip()
        for ch in s:
            visit[ord(ch)-97]=True
            union(ord(s[0])-97,ord(ch)-97)
    ans=0
    for i in range(26):
        if visit[i] and parent[i]==i:
            ans+=1
    print(ans)

    # That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.

