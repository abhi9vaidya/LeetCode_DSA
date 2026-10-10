class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mp = {0:1}
        total = 0
        count = 0
        for num in nums:
            total+=num
            if total - k in mp:
                count+=mp[total-k]
            mp[total] = mp.get(total,0)+1
        return count