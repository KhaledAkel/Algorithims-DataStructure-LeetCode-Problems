class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeroSeq = 0 if flowerbed[0] else 1

        for ele in flowerbed:
            if ele:
                n -= int((zeroSeq - 1) / 2) 
                zeroSeq = 0
            else:
                zeroSeq += 1
        n -=(zeroSeq) // 2
        return n <= 0
