#https://leetcode.com/discuss/interview-question/633508/amazon-onsite-english-words-to-integer

#Input: "Three hundred million"
# Output: 300,000,000

word={
    "one":1,"two":2 , "three":3, "four":4,"five":5, "six":6,"seven":7,"eight":8,"nine":9,"ten":10,
    "eleven":11,"twelve":12,"thirteen":13, "fourteen":14, "fifteen":15,"sixteen":16,"seventeen":17,
    "eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"fourty":40,"fifty":50,"sixty":60,"seventy":70,
    "eighty":80
}
bigboss={"ninety":90,"hundred":100,"thousand":1000,"million":1000000,"billion": 1000000000}
num=0
ans=0
s = input().split()
for w in s:
    if w in word:
        num+=word[w]
    elif w=="hundred":
        num*=100
    else:
        num*=bigboss[w]
        ans+=num
       # print(ans)
        num=0
ans+=num
print(ans)


