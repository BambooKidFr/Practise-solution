# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer
# reverse digits of an integer.

class Solution:
    def reverse(self, x):
        """

        :type x: int
        :rtype: int
        """
        negative = x < 0  # record if negative and change to positive
        x = abs(x)
        reversed = 0

        while x != 0:
            reversed = reversed * 10 + x % 10
            x //= 10
        if reversed > 2**31 - 1:  # require to pass leetcode test
            return 0
        return reversed if not negative else -reversed
