class Solution:
    def findMin(self, nums: List[int]) -> int:
        a,b = 0,len(nums)-1
        MIN = float("+inf")

        while a<=b:
            mid = (a+b)//2
            MIN = min(nums[mid], MIN)

            if nums[mid] > nums[b]:
                a = mid +1 
            else:
                b = mid -1
        return min(nums[a],MIN)

        
