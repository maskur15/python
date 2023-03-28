
series1=0; series2=0;total=0;
n=int(input("ENter a number: "))
for i in range (1,n):
    total+=i
    if i%2==0:
     series1+=i ;
    else:
        series2+=i;
print("The sum of the odd number in the range is : ",series2)
print("The sum of the even number in the range is : ",series1)
print("sum of odd division sum of even is : ",series2/series1)
print("MUltiplication : ",series2*series1)
print("difference is : ",series1-series2)
print("SUm of the numebr in this range is : ",total)
