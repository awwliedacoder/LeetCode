class Solution(object):
    def singleNumber(self, nums):
        unique = 0;
        for i in nums:
            unique ^= i;
        return unique;

# Had to resort to community tab really to understand the problem again,
# I feel like it is getting better though, I'll probably switch to using python only for a while.
# Getting better at trying to solve these though. 

# own solution -> doesn't pass any tests- Missed the point of the task pretty much.... I blame math.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)
        for i in hashset:
            if i not in hashset:
                hashset.add(i)
            elif i in hashset:
                if nums[i] == i-1:
                    hashset.add(i)
                

