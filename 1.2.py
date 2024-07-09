# -*- coding: utf-8 -*-
"""
Created: Sat Apr 13 20:48:32 2024
Author: w'm'h001 (Python 3.8)

Description:
"""
# 1.2 启动Python
# 不能仅仅进行被动的知识堆砌，应当更勇于尝试，Python并非稍有错误就损坏
# 本书使用的Python编程环境的全部组件：
#     Python：可以指代一种计算机编程语言，用于向计算机描述算法；还可以指代Python解释器或
#         语言与通用软件库的集合
#     IPython：一种Python解释器，它是一个计算机应用，提供执行Python命令和程序的便利交互
#         模式
#     Spyder：一个集成开发环境（IDE, Integrated Development Environment），它是一个
#         包含IPython的计算机应用，可以进行变量检查，也是一个编写和调试程序的文本编辑器，
#         还提供更多其他功能
#     Numpy：一个提供数值数组和算术函数的第三方函数库
#     Pyplot：一个提供可视化工具的第三方函数库
#     Scipy：一个提供科学计算工具的第三方函数库
#     Anaconda：Python的一个发布版本。它是一个包括上述所有组件的单一下载文件，提供对更多
#         其他用于特殊目的的函数库的访问，其中也包括维护所有组件版本为最新版本的软件包管理
#         器conda

# 安装Python：本项目安装Windows、Python3.8版本的Anaconda
#     图形界面安装：OS X：从Anaconda官网下载Anaconda安装包后，运行该文件，安装
#             Launcher.app。打开该应用，启动Spyder，或打开Anaconda安装文件夹中的
#             Spyder程序，或打开终端，输入命令spyder
#         Windows：从Anaconda官网下载Anaconda安装包后，运行该文件。开始菜单“所有程序”中
#             Anaconda3(64-bit)文件夹中包含启动Spyder的快捷方式；或执行Anaconda3\
#             Scripts文件夹中的spyder-script.py脚本；或执行Anaconda3\Scripts文件夹
#             中的spyder.exe程序
#     命令行安装：从Miniconda官网下载Miniconda安装包后，运行该文件，安装conda。使用
#             conda安装其他模块：在终端执行conda install 模块名。安装的模块：磁盘空间充
#             足可以安装包含所有所需模块的模块anaconda；磁盘空间不足可以独立安装所需的模
#             块：numpy、matplotlib、scipy、ipython、pillow、sympy、spyder以及输出
#             提示中提示丢失的模块、pyflakes、docutils、jinja2

# 配置Spyder：使用“工具”菜单的偏好菜单项
#     配置工作目录：在面板左侧“工作目录”选项配置“指定目录”（打开文件默认打开的文件夹和新建
#         文件默认所在的文件夹）
#     配置交互图形：在面板左侧“IPython控制台”选项中选择“绘图”选项，配置图形的后端为自动或
#         除行内（图形为静态）之外的其他选项
#     配置脚本模块：在面板左侧“编辑器”选项中选择“高级设置”选项，点击“编辑用于新文件的模板”，
#         编辑文件template.py，添加作者、创建日期和时间、和简单描述。%(date)s表示创建日
#         期和时间，%(username)s表示系统用户名
#     配置完成后可能需要重启Spyder才完全生效

# 更新模块：在终端执行conda update 模块名
# 更新初始环境的所有模块：在终端执行conda update --all

# 1.2.1 IPython控制台
# Spyder默认窗口布局含有三个窗格：
#     左侧是编辑窗格用于编辑程序
#     右上方窗格用于查看各种信息，包括用于查看帮助文档、当前终端会话（从本次启动终端或上次运
#         行%reset以后）的变量的类型和值、图像和工作目录内的文件的选项卡。双击变量浏览器的
#         列表或np数组变量会弹出一个包含该变量所有元素的电子表格
#     右下角窗格用于管理命令行终端，包括用于显示名为IPython控制台的命令行终端和命令记录文
#         件的选项卡。IPython控制台的命令默认提示符为“In [本终端内的命令序数<整型数>]”
# 可以点击“查看”菜单的“窗口布局”菜单项的“Spyder默认布局”选项使当前窗口布局变为默认布局

# 命令可以是能执行的完整的一行Python语句
# Python交互模式除py文件支持的外还支持：
#     变量名
#     返回变量值
# IPython控制台除Python交互模式支持的外还支持：
#     以%开头的魔术命令：
#         %magic 显示一个介绍被支持的魔术命令的页面
#         %reset 重置Python状态，清除当前终端会话创建的所有内容

# 命令没有反馈的两种情况：
#     赋值语句
#     命令中包含了未匹配的(、[、{等，终端会继续读取更多的行搜索匹配的符号

import numpy as np

a = 1
b = a**2 - a
# 打印多个值
# print(
#     *values: 接收数个被打印的内容<> | "",
#     sep=两个被打印内容间的分隔符<字符串> | None = " ": 半角空格,
#     end=打印后的结束符<字符串> | None = "\n",
#     file=接收文件<文件> | None: 不将内容输出到文件,
#     flush=是否立即将输出到缓冲区的内容全部打印<布尔> | Flase: 输出到缓冲区的内容等到程
#         序运行结束后一起打印到屏幕)
# 在终端打印内容
# \n有将缓冲区的内容打印的作用，若被打印的内容含有\n或结束符为\n，缓冲区内含有\n的内容或结
#     束符\n前的内容将不管flush参数立即打印
print(a, b)

# ;或换行结束一条命令
a = 1; b = 2
c = 3
print(a, b, c)

# \将本行与下一行结合为一条命令
q = 1 + \
    2
print(q)

p = "This is a" \
    " long sentence."
print(p)

# 1.2.2 错误信息
# Python识别到代码无法被解释器理解的错误后会终止程序运行，并抛出一个异常。
# 若异常未被手动捕获将在终端打印Traceback（错误信息），错误信息包括错误类型和错误所在位置等
# 异常可以在程序运行中自动抛出，也可以手动抛出

# raise 异常类型
# 手动抛出某种异常

# Python允许在程序因异常而将终止前手动捕获异常，对其进行处理，使程序能继续运行

# 有些函数会将异常降级为警告（RuntimeWarning）
# numpy.divide(
#     x1=被除数<整型数/浮点数/numpy.ndarray类>: 仅限位置实参; 数字参数为被除数;
#         numpy.ndarray参数的元素为被除数 | 无默认值,
#     x2=除数<整型数/浮点数/numpy.ndarray类>: 仅限位置实参; 数字参数为除数;
#         numpy.ndarray参数的元素为除数; 如果x1的形状不等于x2的形状或两者一为数字一为
#         numpy.ndarray实例，则两者必须可通过广播机制转化为相同形状的numpy.ndarray
#         实例，同时这个形状也是被返回numpy.ndarray实例的形状 | 无默认值,
#     out=用于存储结果的变量<numpy.ndarray类> | None: 不存储结果而是返回一个新
#         numpy.ndarray实例,
#     where=指定哪些元素需要参与除法运算<布尔/numpy.ndarray类>: 仅限关键字实参;
#         numpy.ndarray参数元素类型为布尔 | True: 全部参与,
#     **kwargs: 接收数个关键字实参，均有默认值:
#         casting | 'same_kind',
#         order | 'K',
#         dtype | None,
#         subok | True)
# 参数x1和x2均为数字，返回两个数字的商；参数x1和x2为两个numpy.ndarray实例或一个数字和一
#     个numpy.ndarray实例，返回新创建的经过广播产生的numpy.ndarray实例对应位置相除产生
#     的numpy.ndarray实例
# 该函数支持除零运算，运算结果为模块numpy定义的numpy.float64类型的常量inf或-inf，表示正
#     无穷或负无穷。但进行除零运算会在终端打印一个警告

# numpy的广播机制：
# 辅助概念：numpy.ndarray实例形状：numpy.ndarray实例的维数和每个维度的长度，用一维元组表
#     示，一维元组的元素数量为numpy.ndarray实例的维数，元组每个元素为某维度的长度，元素顺
#     序为维度从高到低
# 目的：处理多个形状不同的numpy.ndarray实例或numpy.ndarray实例与数字间的运算
# 思路：将多个形状不同的numpy.ndarray实例或numpy.ndarray实例与数字转化为形状相同的
#     numpy.ndarray实例
# 步骤：
#     1.让所有输入的numpy.ndarray实例的维数都扩大至与其中维数最大的numpy.ndarray实例相
#         等，扩大方法为在形状元组开头增加元素1，即增加更高的维度，并设定新增加的维度的长度
#         为1，直到达到所需维数。数字的维数视为0。
#     2.从后往前比较各个numpy.ndarray实例形状元组在同位置的元素，每次比较后执行如下操作：
#         （1）如果形状元组元素相等，则完成匹配。如果未到形状元组开头则进行下一次比较，否则
#             广播机制结束。
#         （2）如果形状元组元素不相等，若其中仅有一个元素不为1，将所有元素修改为该不为1的
#             元素，新产生的numpy.ndarray实例元素由原有numpy.ndarray实例元素平行填充。
#             如果未到形状元组开头则进行下一次比较，否则广播机制结束。
#         （3）如果形状元组元素不相等，且不满足其中仅有一个元素不为1，报错。

print(np.divide(1, 0))

# try:
#     正常代码
# except 异常类型1:
#     处理该异常的代码
# ···
# except 异常类型i:
#     处理该异常的代码
# ···
# except 异常类型n:
#     处理该异常的代码
# 先执行正常代码
# 如果未发生异常，执行结束后结束该程序块
# 如果发生了指定类型的异常，正常代码将执行到发生异常的语句之前，然后执行处理该异常的代码，执
#     行结束后结束该程序块
# 如果发生了未指定类型的异常，正常代码将执行到发生异常的语句之前，然后程序停止，并在终端打印
#     一个Traceback，其中包含有关异常的报告
try:
    1 / 0
except ZeroDivisionError:
    print("1/0 -> infinity")

# 一些常见错误及示例：
# SyntaxError：语法错误，命令不正确
try:
    # exec(
    #     source=要执行的代码<字符串/code类>: 仅限位置实参 | 无默认值,
    #     globals=全局命名空间内的变量及其值<字典>: 仅限位置实参; 键值对的键为字符串格式
    #         的变量名，值为该变量的值 | 当前代码文件的全局命名空间内的变量及其值组成的字
    #         典,
    #     locals=当前局部命名空间内的变量及其值<字典>: 仅限位置实参; 键值对的键为字符串格
    #         式的变量名，值为该变量的值 | 与参数globals相同)
    # 将接收的字符串格式或code类的代码转化为可执行Python代码并执行该代码
    # 代码的语法错误在执行前就可以检查出来并报错，故需要使用函数exec()使该错误可捕获
    exec("if q=3:\n        print('yes')\n    else:\n        print('no')")
except SyntaxError:
    print("SyntaxError")
# ImportError：导入错误，无法找到试图导入的模块
try:
    import Numpy
except ImportError:
    print("ImportError")
# AttributeError：属性或方法错误，请求了实例不具有的属性或方法
try:
    np.atan(3)
except AttributeError:
    print("AttributeError")
# NameError：名字错误，请求了不存在的变量、函数或模块
try:
    print(zlist)
except NameError:
    print("NameError")
# IndexError：索引错误，请求的索引值处于序列实例的索引范围之外
try:
    x = [1, 2, 3]
    print(x[3])
except IndexError:
    print("IndexError")
# TypeError：类型错误，无法处理某类型的数据
try:
    abs("-3")
except TypeError:
    print("TypeError")
# AssertionError：断言错误，
try:
    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16, 25]
    # assert 表达式
    # 断言语句，如果表达式的值为True正常执行后结束该程序块；如果表达式的值为False，停止程
    #     序并抛出断言错误
    # assert 表达式, 参数
    # 断言语句，如果表达式的值为True正常执行后结束该程序块；如果表达式的值为False，停止程
    #     序并抛出断言错误，若错误未被捕获需在打印到终端的Traceback中的错误类型后打印参
    #     数
    assert len(x) == len(y), "Lists must be same length!"
except AssertionError:
    print("AssertionError")

# 1.2.3 如何获取帮助
# 查看Python文档：访问网站https://www.python.org/doc
# 查看各种帮助信息：
#     在IPython控制台输入或在py文件中运行命令 help(函数名/模块名/模块别名/变量名)
#     在IPython控制台输入命令 函数名/模块名/模块别名/变量名？
#     Spyder特有的方法：
#         光标停在函数名/模块名/模块别名/变量名，按Ctrl+I，将在右上方窗格的“帮助”选项卡按
#             一定排版方式显示帮助信息
#         在右上方窗格的“帮助”选项卡顶部的输入框输入函数名/模块名/模块别名/变量名，回车，
#             将在该选项卡按一定排版方式显示帮助信息
# 查看当前终端会话中已导入或创建的所有模块、函数和变量的名字：
#     dir(
#         o=实例<>: 仅限位置实参 | 当前终端会话对应的实例)
#     调用实例的方法__dir__
#     未自定义方法__dir__的实例的默认方法__dir__返回一个列表实例，其元素为参数的属性名和
#         方法名的字符串格式
#     当前终端会话对应的实例的方法__dir__返回一个列表实例，其元素为当前终端会话中已导入或
#         创建的所有模块名、函数名和变量名的字符串格式
#     特殊实例__builtins__的方法__dir__返回一个列表实例，其元素为所有Python内置模块名和
#         函数名的字符串格式

# 1.2.4 好的做法：记录日志
# 每次解决问题后，记录解决方法
