class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        temp = 0
        for i in range(len(s)):
            if temp > l:
                l = temp
            temp = 0
            for j in range(i, len(s)):
                lst = ''
                
                temp = 0
                e = s[i:(j+1)]
                for x in e:
                    if x not in lst:
                        lst += x
                    else:
                        break
                temp = len(lst)
        if temp > l:
            l = temp
        return l

s = Solution()
print(s.lengthOfLongestSubstring("bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"
))