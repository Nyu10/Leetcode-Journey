class Solution:
    def isPalindrome(self, x: int) -> bool:
        str0 = str(x)
        str1 = str0[::-1]
        if (str0 == str1):
            return True
        else:
            return False