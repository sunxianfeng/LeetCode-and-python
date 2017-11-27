# -*- coding:utf-8 -*-

#递归版
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base: return convert_string[n]
    else:
       return to_str(n / base, base) + convert_string[n % base]

#使用栈
r_stack = []
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base: r_stack.append(convert_string[n])
        else:
            r_stack.append(convert_string[n % base])
        n = n // base
    res = ""
    while r_stack:
        res = res + str(r_stack.pop(-1))
    return res
print(to_str(1453, 16))

