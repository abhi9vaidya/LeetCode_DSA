class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS = s.lower()
        newS = "".join(char for char in newS if char.isalnum())
        if newS == newS[::-1]:
            return True
        else:
            return False