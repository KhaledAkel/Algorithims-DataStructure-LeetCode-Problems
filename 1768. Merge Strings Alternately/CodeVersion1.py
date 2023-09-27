class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        string = ""
        for i in range(min(len(word1), len(word2))):
            string += word1[i] + word2[i]
        if len(word1) > len(word2):
            string += word1[len(word2):]
        if len(word1) < len(word2):
            string += word2[len(word1):]

        return string
