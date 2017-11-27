# -*- coding:utf-8 -*-
def longestConsecutive(num):
    hashmap = {}
    for i in num:
        hashmap[i] = True
    max_n = 0
    for k, v in hashmap.items():
        if not v:
            continue
        left = k - 1
        right = k + 1
        while hashmap.has_key(left) and hashmap[left]:
            hashmap[left] = False
            left -= 1
        while hashmap.has_key(right) and hashmap[right]:
            hashmap[right] = False
            right += 1
        n = right - left - 1
        if n > max_n:
            max_n = n
    return max_n
num = [100, 4, 200, 1, 3, 2]
max_len = longestConsecutive(num)
print max_len