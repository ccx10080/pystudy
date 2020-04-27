#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list，有序的集合，可以随时添加、删除元素
classmates = ['Michael','Bob','Tracy']
print(classmates)
#len()函数获得list的长度
print(len(classmates))
#用索引来访问list中每个位置的元素，索引从0开始
print(classmates[0])
#最后一个索引是len(classmates)-1
#使用-1可以直接获取最后一个索引的值
#以此类推，可以获取倒数第二个、第三个
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

#追加元素 append()
classmates.append('Adam')
print(classmates)
#插入元素 insert(i,'Jack')
classmates.insert(1,'Jack')
print(classmates)
#删除末尾元素 pop()
classmates.pop()
print(classmates)
#要删除指定位置的元素，用pop(i)方法，其中i是索引的位置：
classmates.pop(1)
print(classmates)
#修改元素值
classmates[0]='ccx'
print(classmates)

#list里面元素类型可以不一样
L = ['Apple',123,True]
print(L)
#list里面的元素也可以是list
s = ['python','java',['asp','php'],'scheme']
print(len(s))

L = []
print(len(L))

