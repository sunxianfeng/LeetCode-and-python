# -*- coding:utf-8 -*-
'''
汉诺塔问题
下面是关于将塔经由中间杆，从起始杆移到目标杆的抽象概述：
1、 把圆盘数减一层数的小塔经过目标杆移动到中间杆 
2、 把剩下的圆盘移动到目标杆 
3、 把圆盘数减一层数的小塔从中间杆，经过起始杆移动到目标杆
'''
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
def moveDisk(fromPole,toPole):
    print("moving disk from",fromPole,"to",toPole)
    toPole.append(fromPole.pop(-1))      #三个塔用三个栈表示
A = [('A'),3,2,1]
B = [('B')]
C = [('C')]
moveTower(3,A,B,C)