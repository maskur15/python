def decimalToBinary(num):
    if num==0 or num ==1:
        return num
    return decimalToBinary(num//2)*10 + num%2
if __name__ == '__main__':
   while True:
    num = int(input())
    print(decimalToBinary(num))