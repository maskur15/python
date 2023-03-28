from collections import deque
def precedence(operator):
    if operator=='+' or operator=='-':
        return  1
    if operator=='*' or operator=='/':
        return 2
    return 0
def applyOperation(v1,operator,v2):
   if operator=='+':return  v1+v2
   if operator=='-':return  v1-v2
   if operator=='*': return  v1*v2
   if operator=='/': return  v1/v2

def calculate(expression):
    #use a stack for values
    values= deque()
    #use a stack for store opearator
    operator = deque()
    i=0
    while i<len(expression):
        ch= str(expression[i])
        if ch==' ':
            i+=1
            continue
        elif ch.isdigit():
            val=0
            while i<len(expression) and str(expression[i]).isdigit():
                val=val*10+ int(expression[i])
                i+=1
            i-=1
            values.append(val)
        elif ch=='(':
            operator.append(ch)
        elif ch==')':
            while len(operator)>=1:
                top= operator.pop()
                if top=='(':
                    break
                #top value is the second value
                v2=values.pop()
                v1=values.pop()
                values.append(applyOperation(v1,top,v2))
        else:
            #its a operator +,-,*,/

            while len(operator)>=1 :
                top=operator.pop()
                if precedence(top)<precedence(ch):
                    operator.append(top)
                    break
                v2=values.pop()
                v1=values.pop()
                values.append(applyOperation(v1,top,v2))
            #apppend curernt operator
            operator.append(ch)
        i+=1
    while len(operator)>=1:
        top=operator.pop()
        v2=values.pop()
        v1=values.pop()
        values.append(applyOperation(v1,top,v2))
    return  values.pop()

if __name__=='__main__':
   print(calculate('14/(2*2)'))
   print(calculate('10* 2+6'))