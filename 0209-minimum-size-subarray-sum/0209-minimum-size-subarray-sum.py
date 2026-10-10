class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        currSum = 0
        minLen = float('inf')
        for right in range(len(nums)):
            currSum+=nums[right]
            while currSum >= target:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                currSum -= nums[left]
                left+=1
            right+=1

        if minLen!= float('inf'):
            return minLen
        else :
            return 0