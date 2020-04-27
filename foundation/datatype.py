#数据类型

#整数
a=123
#浮点数
b=1.23
#字符串 '' 或 "" 转义字符 \
print('I\'m \"OK\"!')
#r''标识''内部的字符串默认不转义
print(r'\\\t\\')
#如果字符串有很多换行'''  '''
print('''line1
line2
line3''')
#布尔值 True,False
print(3>2)
print(3>5)
#布尔值运算 and,or,not
print(True and True)
print(True and False)
print(False and False)
print(5>3 or 1>3)
#布尔值经常用在条件判断中
age=19
if age>=18:
    print('adult')
else:
    print('teenager')

#空值 None
