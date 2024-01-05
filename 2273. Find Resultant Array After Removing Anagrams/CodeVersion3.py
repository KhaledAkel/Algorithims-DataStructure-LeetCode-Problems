class Solution:
    
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        last_normalized = None

        for word in words:
            normalized = sorted(word)
            if last_normalized != normalized:
                last_normalized = normalized
                result.append(word)
        
        return result
            
