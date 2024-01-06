class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return sorted(count.keys(), key=count.get, reverse=True)[:k]
