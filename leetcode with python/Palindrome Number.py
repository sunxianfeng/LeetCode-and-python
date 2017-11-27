# -*- coding:utf-8 -*-
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x /= 10
        print res, x
        return res == x


def isPalindrome(x):
    if x > 0: return False
    len_x = 1
    while x/len_x >= 10:
        len_x *= 10
    while x != 0:
        high = x / len_x
        low = x % 10
        if high != low: return False
        x = (x % len_x)/10
        len_x /= 10
    return True