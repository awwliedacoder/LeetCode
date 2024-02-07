class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """       
        count = Counter(nums)
        result = 0 
        for n, c in count.items():
            result += c * (c-1) // 2
        return result



// Feeling bad about this one, tried to go a bit too different of a way, to the result of neetcode's tutorial. 
// own solution.. only passed 9 / 49 testcases. Issue is ofcourse I didn't read the whole task correctly...
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """       
        counter = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    if i < j:
                        counter.add(n)
        return len(counter)

  
