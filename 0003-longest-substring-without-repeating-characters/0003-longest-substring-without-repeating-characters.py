class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res,maxm = "", 0
        for char in s:
            if char not in res:
                res+= char
            else:
                maxm = max(maxm, len(res))
                res = res[res.index(char) +1:] + char
        return max(maxm, len(res))