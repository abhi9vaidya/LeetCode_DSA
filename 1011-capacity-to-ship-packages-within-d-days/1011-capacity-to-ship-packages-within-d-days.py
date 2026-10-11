def getMax(weights):
    mx = 0
    for w in weights:
        mx = max(mx, w)
    return mx

def getSum(weights):
    total = 0
    for w in weights:
        total+=w
    return total

def canShip(weights, days, capacity):
    dayCount = 1
    currLoad = 0
    for w in weights:
        if currLoad + w > capacity:
            dayCount+=1
            currLoad = 0
        currLoad +=w
        if dayCount > days:
            return False
    return True

class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = getMax(weights)
        high = getSum(weights)
        while low < high :
            mid = low+(high-low)//2 
            if canShip(weights,days,mid):
                high = mid
            else:
                low = mid+1
        return low