#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#str,字符串编码问题Unicode   UTF-8可变长编码
print("包含中文的str")
#ord()函数获取字符的整数表示
print(ord('A'))
print(ord('陈'))
# chr()函数把编码转换为对应的字符
print(chr(66))


#由于Python的字符串类型是str，
# 在内存中以Unicode表示，
# 一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，
# 就需要把str变为以字节为单位的bytes。
#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
print(x)
#以Unicode表示的str通过encode()方法可以编码为指定的bytes,

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

#反过来，如果我们从网络或磁盘上读取了字节流，
# 那么读到的数据就是bytes。
# 要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'))

#要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
print(len('中文'))
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'ABC'))
print(len('中文'.encode('utf-8')))

#格式化 
# %运算符就是用来格式化字符串的。
# 在字符串内部，%s表示用字符串替换，
# %d表示用整数替换，有几个%?占位符，
# 后面就跟几个变量或者值，顺序要对应好。
# 如果只有一个%?，括号可以省略。
print('hello,%s' % 'world')


