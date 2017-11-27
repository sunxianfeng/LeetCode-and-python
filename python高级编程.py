# -*- coding: utf-8 -*-
#在列表、字典和集合中根据条件筛选
import random

lis = [1,-2,-5,6,8,9,-3]  #过滤出负数
res = filter(lambda x:x >= 0,lis)

dic = { x:random.randint(60,100) for x in range(1,20)}  #过滤出成绩大于80的
res2 = {k:v for k,v in dic.iteritems() if v > 80}

data = [1,2,3,4,5,6,7,8,9]  #筛选集合中被3整除的
s = set(data)
res3 = {x for x in s if x % 3 == 0}

#统计序列中出现的频数
data = [random.randint(1,10) for _ in range(30)]
c = dic.fromkeys(data,0)
for x in data:
   c[x] += 1
sorted(zip(c.itervalues(),c.iterkeys())),sorted(c.iteritems(), key=lambda x:x[1])

#快速找出字典中公共键
s1 = {'a':1,'b':3,'c':4}
s2 = {'b':3,'c':3,'d':6}
s3 = {'c':3,'e':2}
s1.viewkeys() & s2.viewkeys()
#map(dic.viewkeys(),[s1,s2,s3])
#reduce(lambda a,b:a&b,map(dic.viewkeys(),[s1,s2,s3]))

#如何让字典有序
'''
使用collection中的OrderDict
'''
#迭代器
def f():
   print "迭代1次："
   yield 1
   print "迭代2次:"
   yield 2

g = f()
#for x in g:print x
# print g.next()
# print g.next()

#拆分含有多种分隔符的字符串
import re
s = '1 2;3,2+c&v'
re.split(r'[ ,;+&]+',s)







