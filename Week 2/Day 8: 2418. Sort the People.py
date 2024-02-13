class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        hashMap = {}
        n = len(names)
        for i in range(n):
            hashMap[heights[i]] = names[i]

        heights.sort(reverse=True)
        ans = []

        for i in range(len(heights)):
            ans.append(hashMap[heights[i]])

        return ans

      # Dont feel proud about this either, I had the idea, but just used the wrong set of tools, again.
      # Starting to feel bad because of it, but- 
      # I'm only on my first half a year, and we haven't gone over really any programming other than simple for- and while loops.
      # So I guess being able to even get a hint of the idea is something.

      # own solution attempt.

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        hashset = set(names,)

        for h in range(len(heights)): 
            for n in range(h+1, len(names)):
                if heights[h] > heights[n]:
                    hashset.add(names[h])
            return hashset

      # As you can see, the idea is kind of there- but in different a lot more stupid way.
      # and as I hate to admit it, I wasn't able to solve it at all. 
      # I managed to get the first one right- but then failed. Sucks to suck I guess, we'll get them next time.

