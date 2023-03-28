#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        length = len(s)
        if length <= 1:
            return (length)
        i = 1
        st = 0
        d[s[0]] = 0
        ans = 0
        while i < length:
            if s[i] in d:
                ans = max(ans, i - st)
                if st < d[s[i]]+1 :
                    st = d[s[i]] + 1
                d[s[i]] = i
                i = i + 1
            else:
                d[s[i]] = i
                i += 1

        ans = max(ans, i - st)

        return ans

s = Solution()
print(s.lengthOfLongestSubstring('abba'))
