class Solution:
    def lengthOfLongestSubstring(self, s):
        whole_list = []
        for x in range(len(s) + 1):
            for y in range(x):
                whole_list.append(s[y:x])
        
        temp1 = 0
        for x in whole_list:
            temp = 0
           
            empty_lst = []
            for y in range(len(x)):
                if x[y] not in empty_lst:
                    empty_lst.append(x[y])
                    temp+=1
                else:
                    break
            if temp > temp1:
                temp1 = temp
            
        return temp1




    
s = Solution()
print(s.lengthOfLongestSubstring("abaaaaacdeasdafghhfhijklmnuyuiobpqrstyuyuvadawxyzAasddBCDEsfFbGHIJiuKLMNafOPQRSTsfdUVsXYZ012345fds678s9!"))