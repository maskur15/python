def solve(word1,word2):
    ans = ""
    if len(word1) > len(word2):
        for i in range(len(word2)):
            ans += word1[i]
            ans += word2[i]
        ans += word1[len(word2):]
    else:
        for i in range(len(word1)):
            ans += word1[i]
            ans += word2[i]
        ans += word2[len(word1):]
    return ans


if __name__=='__main__':
    while True:
         a,b = (input().split())
         print(solve(a,b))