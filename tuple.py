#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#元组：tuple，有序列表，一旦初始化就不能修改
classmates=('Michael','Bob','Tracy')

t = (1,2)
print(t)
t = ()
print(t)

# 定义一个元素的元组
t=(1,)
print(t)

t=('a','b',['A','B'])
t[2][0]='X'
t[2][1]='Y'
print(t)
