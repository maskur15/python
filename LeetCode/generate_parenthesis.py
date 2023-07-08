from collections import deque
def solve_backtrack(s,n,left):
    if left<0:
        return
    if len(s)== 2*n and left>0:
        return
    if len(s)== 2*n and left==0:
        answer.append(s)
        return
    solve_backtrack(s+')',n,left-1)
    solve_backtrack(s+'(',n,left+1)
    return list(answer)
def solve_parenthesis(s,n,left):
    if left==0 and len(s)==2*n:
        parenthesis.append(s)
        return parenthesis
    if len(s)<2*n and left>=0:
        solve_parenthesis(s+')',n,left-1)
        solve_parenthesis(s+'(',n,left+1)
    return parenthesis
def generateParenthesis(s,n,left,right):
    if len(s)==2*n:
        parenthesis_list.append(s)
    if left<n:
        generateParenthesis(s+'(',n,left+1,right)
    if right<left:
        generateParenthesis(s+')',n,left,right+1)
    return parenthesis

if __name__ == '__main__':
    while True:
        n=int(input())
        answer = deque()
        parenthesis = []
        parenthesis_list = []

        solve_backtrack('(',n,1)
        print(list(answer),len(answer))
        solve_parenthesis('(',n,1)
        print(parenthesis)
        generateParenthesis('',n,0,0)
        print(parenthesis_list)