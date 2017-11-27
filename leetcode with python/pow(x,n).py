# -*- coding:utf-8 -*-
class Solution(object):
    def pow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1.0
        if n == 1: return x
        if n < 0: return 1.0/self.pow(x,-n)

        sub = self.pow(x,n/2)
        return sub * sub * self.pow(x,n%2)
s = Solution()
print s.pow(2,3)