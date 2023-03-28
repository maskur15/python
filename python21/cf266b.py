#python test file
n , t= map(int,input().split())
string=input()
s=list(string)
while t>=1:
    t-=1
    i=0
    while i<n-1:
        if s[i]=='B' and s[i+1]=='G':
            s[i]='G';s[i+1]='B';i+=1
        i=i+1

s="".join(s)
print(s)
