# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
#多重索引
s = pd.Series(np.array([1,2,3,4,5]),index=list("abcda"))
a = [['a','b','c'],[1,2,3]]
t = list(zip(*a))
index = pd.MultiIndex.from_tuples(t,names=['level1','level2'])
s2 = pd.Series(np.random.rand(3),index=index)

df = pd.DataFrame({'a': range(4),'b':range(7,3,-1),'c':['one','one','two','two']})
df.set_index(['a','b'])

#分组运算
df2 = pd.DataFrame({'key1':['a','a','b','b'],
                    'key2':['one','two','one','two'],
                    'data':np.random.randint(1,10,4)})
df2['data'].groupby(df2['key1']).mean()

df3 = pd.DataFrame(np.random.randint(1,10,(5,5)),
                   columns=['a','b','c','d','e'],
                   index=['星','月','神','话','日'])
df3.ix[1,1:3] = np.NaN
mapping = {'a':'red','b':'red','c':'blue','d':'orange','e':'orange'}
grouped = df3.groupby(mapping,axis=1)
grouped.sum(),grouped.size(),grouped.count()

#聚合
df4 = pd.DataFrame({'key1':['a','a','a','b','b'],
                    'key2':['one','two','one','two','one'],
                    'data1':np.random.randint(1,10,5),
                    'data2':np.random.randint(1,10,5)})
k1_mean = df4.groupby('key1').mean().add_prefix('mean_')
merged = pd.merge(df4,k1_mean,left_on='key1',right_index=True)

#IO操作
# f = pd.read_table('new.csv',header=None,sep=',',names=['a','b','c','d'],chunksize=2) #chunksize分块读取，成为迭代器
# for chunk in f:
#     print chunk

#时间序列
from datetime import datetime
from datetime import timedelta
now = datetime.now()
date1 = datetime(2017,10,13)
date2 = datetime(2017,10,10)
delta = date1 - date2
# print delta.days,delta.total_seconds()
# print date2 + timedelta(4.5),str(date2)
dates = [datetime(2016,3,1),datetime(2016,3,2),datetime(2016,3,3)]
s3 = pd.Series(np.random.randn(3),index=dates)
# print s3,type(s3.index)
date_range = pd.date_range('20171013','20171020')#date_range = pd.date_range('20171013',periods=10)
date_range2 = pd.date_range('20171013',periods=10,freq='d')

#时间序列转换
p = pd.Period('2016Q4','Q-JAN')
p.asfreq('M',how='start'),p.asfreq('M',how='end')
#获取该季度倒数第二个工作日下午4点20分
(p.asfreq('B')-1).asfreq('T')+16*60+20

#重采样
ts = pd.Series(np.random.randint(0,50,60),index=pd.date_range('2016-04-25',periods=60,freq='T'))#每分钟转化为每5分钟
ts.resample('5min',how='sum'),ts.resample('5min',how='ohlc')
#通过groupby重采样
ts2 = pd.Series(np.random.randint(0,50,100),index=pd.date_range('2016-03-01',periods=100,freq='D'))
print ts2.groupby(lambda x:x.month).sum()










