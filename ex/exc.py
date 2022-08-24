def findMedianSortedArrays(nums1, nums2) -> float:
        i = 0
        j = 0
        slist = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                slist.append(nums1[i])
                i += 1
            else:
                slist.append(nums2[j])
                j += 1
                
        while i < len(nums1):
            slist.append(nums1[i])
            i += 1
            
        while j < len(nums2):
            slist.append(nums2[j])
            j += 1
            
        n = len(slist)
        result = 0
        if n % 2 == 0:
            temp = n//2
            result = (slist[temp - 1] + slist[temp])/2
            return result
            
        else:
            result = n//2
            return slist[result]
          

ls = [1,2]
ls2 = [3, 4]
print(findMedianSortedArrays(ls, ls2))