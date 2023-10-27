from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        occurSet = set(counts.values())
        return len(occurSet) == len(counts)
