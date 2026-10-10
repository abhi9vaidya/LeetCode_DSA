class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum , rightSum = 0, sum(nums)
        for i, elem in enumerate(nums):
            rightSum -= elem
            if leftSum == rightSum:
                return i
            leftSum += elem
        return -1
            