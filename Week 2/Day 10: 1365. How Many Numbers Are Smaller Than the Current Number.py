class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smap = []
        count = 0
        
        for n in range(len(nums)):
            for j in range(0, len(nums)):
                if nums[n] > nums[j]:
                    count += 1
            smap.append(count)
            count = 0
        return smap


# I might've been sad as hell yesterday..
# TODAY I'M CRYING TEARS OF JOY.

# I FINALLY MANAGED TO DO IT AGAIN... I LOVE MYSELF.

# it is definetly not.. erm. efficient with a run time of 264ms. I think that means.. uh. O(n^2).. with a O(N) memory. 
# Beats 35% people though? 
