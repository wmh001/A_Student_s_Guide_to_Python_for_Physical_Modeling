# -*- coding: utf-8 -*-
"""
Created: Wed May 22 22:47:29 2024
Author: w'm'h001 (Python 3.8)

Description:
"""
# 2.1 对象和方法
# 在Python中，凡事皆对象
# 对象是数据（属性）和函数（方法）的组合体
# 方法是操作对象本身属性的特定函数，除对象本身外还可以接收额外的参数

# 与某个对象关联的变量可用于访问该变量
# 赋值运算用于建立或更新对象与变量的关联关系

# 实例.方法(除实例本身外的参数列表)
# 调用实例的方法

f = 2.5
# 浮点数实例.is_integer()
# 返回表示浮点数实例是否为整数（小数部分是否为0）的布尔值
print(f.is_integer())
# Python中，函数也是一种特殊的对象，因此可处于赋值号右侧
print(f.is_integer)

s = "Hello"
# 字符串实例.swapcase()
# 返回原字符串实例每个字母进行大小写转换后生成的新字符串实例，原字符串实例不变
print(s.swapcase())
print(s)

L = [1, 2, 3]
print(L)
# 列表实例.reverse()
# 将原列表实例的元素顺序反转排列，原列表实例改变
L.reverse()
print(L)

L = [1, 2, 3]
print(L)
# 列表实例.pop(
#     待删除元素的索引<整型数>: 仅限关键字实参 | -1 : 列表最后一个元素的索引)
# 返回列表实例中对应索引处的元素，原列表实例删除该元素，原列表实例改变，原列表实例中该索引后
#     的元素索引减一（前移一位）
print(L.pop(1))
print(L)

# 常量也可以调用其字面类型的方法
print("Hello".swapcase())
# 为了区分浮点数常量的.和调用方法的.需要对浮点数加括号
print((5.0).is_integer())

# 查看实例的所有属性和方法
print(dir(f))
print(dir(s))
print(dir(L))

# 一般实例的方法可以直接访问（包括使用和更改）该实例的属性，无需再调用时传递存储实例属性的参
#     数
# 某些实例的方法不能更改该实例的属性，这种对象称为不可变对象
# 字符串实例和数字都是不可变对象
# 列表实例和numpy.ndarray实例是可变的

# 实例.属性
# 返回指定实例的指定属性
