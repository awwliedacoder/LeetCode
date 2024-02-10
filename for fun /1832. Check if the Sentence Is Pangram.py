class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence) <= 25:
            return False
        hashset = set()
        alphabet = "abcdefghijklmnopqrstuvwxyz"        
        for letter in alphabet:
            if letter not in sentence:
                return False
            else:
                hashset.add(letter)
        
        if len(hashset) > 25:
            return True

## Kind of proud, I managed to come up with a solution on my own, though I had to google how to go for it.
## Still, had the idea- though not the most efficient.
## Does the job.

##still beats 29% of others on runtime. and 79% of people with memory, and its readable, i think.
