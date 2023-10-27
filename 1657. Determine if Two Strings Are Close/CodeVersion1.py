from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        counter1 = Counter(word1)
        counter2 = Counter(word2)

        return (sorted(list(counter1.keys())) == sorted(list(counter2.keys())) and
                sorted(list(counter1.values())) == sorted(list(counter2.values()))
               )

    
        
