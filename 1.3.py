# -*- coding: utf-8 -*-
"""
Created: Tue May  7 20:21:12 2024
Author: w'm'h001 (Python 3.8)

Description:
"""
# 1.3 Python模块
# Python的优势：提供丰富的函数库。社区开发人员组合基础命令构建成函数库，用于实现复杂任务

# 1.3.1 import
# import 模块名列表
# 导入若干个模块
import numpy

print(dir(numpy))
# numpy.lookfor(
#     what=用于搜索的关键字<字符串> | 无默认值,
#     module=待搜索的文档字符串的模块名<字符串/列表>: 接收"numpy"或numpy子模块名的字符
#         串格式 | None: "numpy",
#     import_modules=是否导入待搜索模块中的子模块<布尔> | True,
#     regenerate=是否重新生成文档字符串缓存<布尔> | False,
#     output=存储搜索结果的文件实例<文件>: 将搜索结果写入该文件实例 | None: 搜索结果不存
#         储到文件实例中，而是打印到终端上)
# 对模块numpy或指定numpy子模块的所有文档字符串进行关键字搜索，搜索结果为匹配的文档字符串及
#     其所属的函数或类按相关性从高到低排序并按一定格式排版后的字符串，将搜索结果存储到文件
#     中或打印到终端上
print(numpy.lookfor("sqrt"))

# 模块名.函数名(参数列表)
# 调用指定模块内的指定函数
# numpy.sqrt(
#     x=开平方运算的被开方数或其集合<整型数/浮点数/列表/元组/numpy.ndarray类>: 仅限位置
#         实参 | 无默认值,
#     out=存储结果的变量<numpy.ndarray类>: 接收numpy.ndarray参数时，计算结果应当
#         可通过广播机制转化为与参数out形状相同的numpy.ndarray实例，该实例也为函数的返回
#         值 | None: 不对计算结果进行广播，也不在其他变量存储计算结果，仅将计算结果返回,
#     where=: 仅限关键字实参 | True,
#     casting=: 仅限关键字实参 | 'same_kind',
#     order=: 仅限关键字实参 | 'K',
#     dtype=: 仅限关键字实参 | None,
#     subok=: 仅限关键字实参 | True)
# 参数x为数字且参数out为None时，返回对其进行开平方产生的浮点数；参数x为集合或参数out不为
#     None时，对其每个位置的元素进行开平方，产生的浮点数组成numpy.ndarray实例，每个算术平
#     方根在numpy.ndarray实例的位置与其被开方数在参数x中的位置相同，返回该numpy.ndarray
#     实例依参数out进行广播后的numpy.ndarray实例
print(numpy.sqrt(2))

n1 = [[0, 1, 2], [3, 4, 5]]
n2 = numpy.array(n1)
print(numpy.sqrt(n1))
print(type(numpy.sqrt(n1)))
print(numpy.sqrt(n2))
print(type(numpy.sqrt(n2)))

a = numpy.zeros(2)
b = numpy.sqrt([2, 3], a)
print(a)
print(b)

# 1.3.2 from ... import
# from 模块名 import 函数名列表
# 导入模块中的若干个函数

# from 模块名 import *
# 导入模块中的所有函数
# 可能导致不同模块的同名函数名字冲突，不建议频繁使用
from numpy import *

# 函数名(参数列表)
# 调用已导入的函数
print(sqrt(2))

# import 模块1名 as 自定义模块1别名, 模块2名 as 自定义模块2别名, ...
# 导入若干个模块并为其取别名
import numpy as np

# 自定义模块别名.函数名(参数列表)
# 调用别名指定的模块内的指定函数
print(np.sqrt(2))

from numpy import sqrt, exp
print(sqrt(2))
print(exp(2))

# from 模块名 import 函数名 as 自定义函数别名
# 导入模块中的函数并为其取别名

# 模块名.子模块名
# 表示某个模块的子模块
from numpy.random import random as rng

# 自定义函数别名(参数列表)
# 调用已导入并取别名的函数

# numpy.random.random(
#     size=被返回numpy.ndarray实例的形状<整型数/整型数元组> | None: 不返回
#         numpy.ndarray实例，返回一个浮点数实例)
# 返回区间[0.0, 1.0)内的随机浮点数实例或这类浮点数组成的numpy.ndarray实例
print(rng())

# 1.3.3 Numpy和Pyplot模块
# Numpy模块提供了生成和分析数据的基本工具
# Pyplot模块是函数库Matplotlib的子集，提供了可视化数据的工具
import numpy as np
import matplotlib.pyplot as plt

import numpy as np, matplotlib.pyplot as plt
