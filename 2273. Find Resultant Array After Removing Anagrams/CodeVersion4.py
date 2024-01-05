class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        for i in range(len(words)-1,0,-1):
            if sorted(words[i])==sorted(words[i-1]):
                words.pop(i)
        return words
        
