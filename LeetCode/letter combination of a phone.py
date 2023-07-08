mp={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
    '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
def getLetter(s,next,i):
    if i==len(next):
        ans.append(s)
        return
    getLetter(s+ mp[next[i]][0],next,i+1)
    getLetter(s+ mp[next[i]][1],next,i+1)
    getLetter(s+ mp[next[i]][2],next,i+1)
    return ans
if __name__ == '__main__':
    while True:
        ans =[]
        s = input()

        print(getLetter('',s,0))