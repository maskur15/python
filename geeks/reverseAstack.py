class Solution:
        def reverse(self,st):
           if len(st)>=1:
            temp = st.pop()
            self.reverse(st)
            print(temp)

if __name__ == '__main__':
    ar = list(map(int,input().split()))
    obj = Solution()
    obj.reverse(ar)
    for _ in range(len(ar)):
        print(ar.pop())
