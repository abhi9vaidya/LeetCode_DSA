class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = set()
        maxSum = 0
        currSum = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                currSum -= nums[left]
                left += 1
            
            seen.add(nums[right])
            currSum += nums[right]

            if(right - left + 1) > k:
                seen.remove(nums[left])
                currSum-=nums[left]
                left +=1
            
            if(right - left + 1) == k:
                maxSum = max(currSum, maxSum)
        return maxSum