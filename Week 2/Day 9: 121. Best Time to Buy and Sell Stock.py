class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0 
        right = 1

        max_profit = 0

        while right < len(prices):
            currentProfit = prices[right] - prices[left] 
            if prices[left] < prices[right]:
                max_profit = max(currentProfit,max_profit)
            else:
                left = right
            right +=1
        
        return max_profit

  #Failed again, had to look for an answer, otherwise tears would've started to fall upon my cheeks.
  # feeling stupid, rightfully so, but we just gotta grind more, soon enough, I guess. 
  # gotta have them ups and downs. 
      
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        hashset = set()

        for i in range(len(prices)):
            for j in range(len(prices)):
                if prices[i] > prices[j]:
                    return 0:
                else:
                    return prices[j]
