# F2 = F0+F1
# f3= f2+f1a
"""
nth fibonaccci
"""

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    print(fibonacci(100))