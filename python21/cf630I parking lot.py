n=int(input())
ln= n*2-2
left=ln-n
x1=4* pow(4,left)- pow(4,left)
x2=4* pow(4,left)- (2*pow(4,left)-pow(4,left-1))

index= n-1
ans=2*x1
ans+= (index-2)*x2
print(ans)