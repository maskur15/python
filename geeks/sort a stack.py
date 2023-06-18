class Solution:
    def sort(self,s):
       if len(s)>=1:
           temp = s.pop()
           self.sort(s)
           self.insert_sort(s,temp)
    def insert_sort(self,s,val):
        if len(s)==0:
            s.append(val)
        else:
            top = s.pop()
            s.append(top)
            if val > top:
                s.append(val)
            else:
                temp = s.pop()
                self.insert_sort(s,val)
                s.append(temp)
if __name__ == '__main__':
    ar = list(map(int,input().split()))
    obj = Solution()
    obj.sort(ar)
    for _ in range(len(ar)):
        print(ar.pop())