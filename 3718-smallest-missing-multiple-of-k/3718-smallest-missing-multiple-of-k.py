class Solution(object):
    def missingMultiple(self, nums, k):
        n=k
        for i in sorted(nums):
            if(i==n):
                n+=k
        return n
        