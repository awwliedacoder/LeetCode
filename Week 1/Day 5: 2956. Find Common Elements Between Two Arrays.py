class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        first = 0
        for num in nums1:
            if num in set2:
                first+=1 

        second = 0
        for num in nums2:
            if num in set1:
                second+=1 

        return first, second

# Kind of lost the idea on this one too, this was a optimal solution I found, compare it down to my one.
# I think the main problem was, I thought I had the idea, while I didn't. Hopefully tommorrow I'll be able to solve a easy all on my own. Don't know yet. Looking better every day though I think?
# Kind of bummed out but- I won't let it affect me. 
class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashset = set()

        for n in nums1:
            for k in nums2:
                if nums2[k] == nums1[n]:
                    hashset.add(k)
    
        return hashset

