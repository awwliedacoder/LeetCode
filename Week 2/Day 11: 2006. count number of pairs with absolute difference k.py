class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(0, len(nums)):
                if nums[i] - nums[j] == k:
                    count += 1
        return count

  # First try, again not optimal.
  # I couldve used a hashmap to make it more efficient, but the runtime is O(n^2)I think. 
