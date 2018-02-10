# -*- coding: utf-8 -*-
# @Time    : 2018/1/29 17:05
# @Author  : ZTS
# @Software: PyCharm


a = [1, 2, 3, 4, 5, 5, 6, 6, 6]
b = set(a)

print(b)

for i in b:
    print(type(i))
    print(i)