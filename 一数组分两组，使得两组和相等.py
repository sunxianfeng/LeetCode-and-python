# -*- utf-8 -*-
def partition(num,index,sum):
    if sum == 0: return True
    if index < 0 or sum < 0: return False

    return (partition(num,index-1,sum) or partition(num,index-1,sum-num[index]))

if __name__ == "__main__":
    def canpartion(num):
        sum = reduce(lambda x,y:x+y,num )
        if sum%2 != 0: return False
        return partition(num,len(num)-1,sum/2)

    num = [1,4,5,10]
    res = canpartion(num)
    print res

