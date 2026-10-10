class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for num in nums:
            total+=num
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            if rightSum == leftSum:
                return i
            leftSum += nums[i]
        return -1
            