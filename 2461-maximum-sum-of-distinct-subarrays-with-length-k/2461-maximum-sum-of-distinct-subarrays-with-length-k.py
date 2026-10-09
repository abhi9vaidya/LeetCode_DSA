class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        set1 = set()
        currentSum = 0
        maxSum = 0
        left = 0
        for right in range (len(nums)):
            while nums[right] in set1 or len(set1)==k:
                set1.remove(nums[left])
                currentSum -= nums[left]
                left+=1
            currentSum += nums[right]
            set1.add(nums[right])
            if len(set1) == k:
                maxSum = max(currentSum, maxSum) 
        return maxSum