def squareD(num):
    ans = 0
    while(num>0):
        x = num%10
        ans+=x*x
        num = num/10
    return ans

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = squareD(n)
        fast = squareD(squareD(n))
        while slow != fast:
            slow = squareD(slow)
            fast = squareD(squareD(fast))
            if fast == 1 or slow == 1:
                return True
        return slow == 1
        
    
    

