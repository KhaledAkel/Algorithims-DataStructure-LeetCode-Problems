class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        self.BubbleSort(nums1)
        return

    def BubbleSort(self,nums1):
        for j in range(len(nums1)):
            for i in range(len(nums1)-1):
                if nums1[i] > nums1[i+1]:
                    k = nums1[i]
                    nums1[i] = nums1[i+1]
                    nums1[i+1] = k
        return
