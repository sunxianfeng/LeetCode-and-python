# -*- coding:utf-8 -*-
def divide(dividend, divisor):
    if divisor == 0: return 0x7fffffff
    ans = 0
    dividend, divisor = abs(dividend), abs(divisor)
    while dividend >= divisor:
        cnt = 1
        while (divisor << cnt) <= dividend:
            cnt += 1
        ans += (1 << (cnt - 1))
        dividend -= (divisor << (cnt - 1))
    return ans




class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0: return 0x7fffffff
        sign = 1
        if dividend * divisor < 0: sign = -1
        ans = 0
        cnt = 1
        dividend, divisor= abs(dividend), abs(divisor)
        subsum = divisor
        while  dividend >= divisor:
            while (subsum << 1) <= dividend:
                cnt <<= 1
                subsum <<= 1
            ans += cnt
            cnt = 1
            dividend -= subsum
            subsum = divisor
        return max(min(sign * ans, 0x7fffffff), -2147483648)

print divide(10,2)