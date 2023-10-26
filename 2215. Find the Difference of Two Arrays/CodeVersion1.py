class Solution:
    def findDifference(self, nums1, nums2):
        answer = [[], []]

        set_ans1 = set(answer[0])
        set_ans2 = set(answer[1])

        for num1 in nums1:
            if num1 not in nums2 and num1 not in set_ans1:
                answer[0].append(num1)
                set_ans1.add(num1)

        for num2 in nums2:
            if num2 not in nums1 and num2 not in set_ans2:
                answer[1].append(num2)
                set_ans2.add(num2)

        return answer
