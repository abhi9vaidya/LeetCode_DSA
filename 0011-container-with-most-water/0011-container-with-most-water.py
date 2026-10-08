class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxArea = 0
        while(left<right):
            currArea = min(height[left], height[right]) * (right-left)
            maxArea = max(currArea, maxArea)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return maxArea