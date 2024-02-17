class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                empty_left_plot = (i == 0) or (flowerbed[i-1] == 0)
                empty_right_plot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    count += 1

        return count >= n

  # Used the Editorial answer for this one, couldn't come up with a solution on my own really.
  # using the leetcode 75 currently, and will probably try to use it for future ones too.

