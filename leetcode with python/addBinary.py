# -*- coding:utf-8 -*-
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = abs(len(a) - len(b))
        if len(a) > len(b): b = "0" * diff + b
        else: a = "0" * diff + a

        res = ""
        carry = 0
        m, n = len(a) - 1, len(b) - 1
        #al, bl = len(a), len(b)
        while m >= 0 and n >= 0:
            ac, bc = a[m], b[n]
            if ac == "1" and bc == "1":
                if carry == 1: res += "1"
                else: res += "0"
                carry = 1
            elif ac == "0" and bc == "0":
                if carry == 1: res += "1"
                else: res += "0"
                carry = 0
            else:
                if carry == 1: res += "0"
                else: res += "1"
            m -= 1
            n -= 1

        if carry == 1: res += "1"
        return res[::-1]
s = Solution()
print s.addBinary('110', '10')