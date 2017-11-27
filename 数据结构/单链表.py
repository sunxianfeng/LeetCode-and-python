# -*- coding:utf-8 -*-
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class SingleLinkList(object):
    def __init__(self,node = None):
        self.__head = node
    def is_empty(self):
        return self.__head == None
    def length(self):                        #空链表要考虑
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.value,end=' ')
            cur = cur.next
    def append(self,item):
        node = Node(item)
        if self.__head == None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next !=  None:
                cur = cur.next
            cur.next = node
    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
    def insert(self,pos,item):
        node = Node(item)

        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count != pos-1:
                count += 1
                cur = cur.next
                node.next = cur.next
                cur.next = node
    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False
    def remove(self,item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.value == item:
                if cur == self.__head:
                   self.__head = cur.next
                else:
                   pre.next = cur.next
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    ll.insert(10,100)
    ll.travel()
    print(ll.search(100))