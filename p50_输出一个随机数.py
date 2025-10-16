"""
题目描述：使用python输出一个随机数
编写者:gfsq
时间:2025-10-14
"""
import random
#介绍三个最常用的方法
print(random.randint(10,20))#随机整数
"""
返回一个闭区间 [a, b] 内的随机整数,random,ranint()
"""
print(random.random())
"""
返回一个半开区间 [0.0, 1.0) 内的随机浮点数（包含 0.0，不包含 1.0）random.random()
"""
print(random.uniform(10,20))
"""
返回一个区间 [a, b] 或 [b, a] 内的随机浮点数（根据 a 和 b 的大小自动调整范围，包含两端边界值的概率极低，但逻辑上是闭区间）。
random.uniform()
"""
