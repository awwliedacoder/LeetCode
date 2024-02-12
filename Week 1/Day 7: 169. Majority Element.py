class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        element = 0

        for num in nums:
            if count == 0:
                element = num
            if element == num:
                count += 1
            else:
                count -= 1

        return element


## Used the Community tab to understand it somewhat. 
## Never heard of this AlrgoRythm, but now I have.
## Down is my own first attempt...(?)
## Used the community tab for it too, but it didn't pass every test.
## Maybe tommorrow I'll get it..

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MajElem = nums[0]
        count = 1

        for i in range(n):
            if nums[i] == MajElem:
                ++count
            else:
                --count
                if count == 0:
                    MajElem = nums[i]
                    count = 1
        
        return MajElem
