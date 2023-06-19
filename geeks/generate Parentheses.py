class Solution:
    def __init__(self):
        pass
    def solve(self,n):
        st=[]
        return self.insert(('()'),n,st)

    def insert(self,x,n,st):

        if n==1:
            st.append(x)
            print(x)
        else:

            for i in range(0,len(x)):
                if i<len(x)-1:
                    if x[i]=='(' and x[i+1]==')':
                        temp = x[:i+1]+'()'+x[i+1:]
                        self.insert(temp,n-1,st)
            self.insert(x + '()', n - 1, st)


if __name__ == '__main__':

    s = Solution()
    print(s.solve(3))

