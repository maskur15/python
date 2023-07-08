def solve(n):
    from collections import  deque
    q = deque()
    answer = deque()
    q.append('(')
    while len(q)>=1:
        s = q.pop()
        if len(s)== 2*n :
            if is_valid(s):
                answer.append(s)
        else:
            q.append(s+')')
            q.append(s+'(')
    return list(answer)

def is_valid(s):
    left =0
    for ch in s:
        if left<0:
            return False
        if ch=='(':
            left+=1
        else:
            left-=1
    if left==0:
        return True
    else:
        return False





# Example usage
if __name__ == '__main__':
    while True:
        n=int(input())
        answer = solve(n)
        print(answer)

