class Solution:
     def __init__(self):
        pass
     def atoi(self,string):
         ar=[]
         first = None
         for ch in string:
             if first is None :
                 if ch=='-':
                    first=-1
                 else:
                     first=1
             elif ch in ['0','1','2','3','4','5','6','7','8','9']:
                 ar.append(ord(ch)-ord('0'))
             else:
                 return -1
         return first*get_num(ar,0)
def get_num(ar,sum):
    if len(ar)==0:
        return sum
    sum = sum*10 + ar.pop(0)
    return get_num(ar,sum)
if __name__ == '__main__':


    string = input()
    sol= Solution()
    ans = sol.atoi(string)
    print(ans)
