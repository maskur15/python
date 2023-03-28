#calculate a mathematical expression
#the input expression must be valid
#contain only parantheses and (+,-,*,/)
#time complexity is o(n)
#further reading : https://www.geeksforgeeks.org/expression-evaluation/
from collections import  deque

def precedence(op):
    if op=='+' or op=='-':
        return 1
    if op=='*' or op=='/': return 2
    return 0
def applyOp(a,b,op):
     if op=='*': return  a*b
     if op=='+' : return a+b
     if op=='/':
         return  a/b
     if op=='-': return  a-b

def evaluate(tokens):
   values= deque()
   ops = deque()
   i=0
   while i<len(tokens):

       if tokens[i]==' ':
           i+=1
           continue
       elif tokens[i]=='(': ops.append(tokens[i])
       elif str(tokens[i]).isdigit():
            #when the token is digit
            val=0
            #number can be multiple digit
            while i<len(tokens) and str(tokens[i]).isdigit():
                val=val*10+ int(tokens[i])
                i+=1
            i-=1
            values.append(val)

       elif tokens[i]==')':
           while len(ops)>=1 :
               op=ops.pop()
               if op=='(':
                   break
               val2=values.pop()
               val1=values.pop()
               values.append(applyOp(val1,val2,op))
       else:

           #currnt token is an operateor
            while len(ops)>=1:
                top = ops.pop()
                if precedence(top)<precedence(tokens[i]):
                    ops.append(top)
                    break
                val2=values.pop()
                val1=values.pop()
                values.append(applyOp(val1,val2,top))
            ops.append(tokens[i])
       i+=1

   while len(ops)>=1:
       val2=values.pop()
       val1=values.pop()
       op=ops.pop()
       values.append(applyOp(val1,val2,op))
   return values.pop()

if __name__=='__main__':
    print(evaluate("10 + 2 * 6"))

    print(evaluate("100 * 2 + 12"))
    print(evaluate("100 * ( 2 + 12 ) / 14"))
