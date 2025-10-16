"""
题目描述：学习列表的排序及连接
编写人：gfsq
时间:2025-10-15
"""
import re
a=[3,4,5,1,2]
a.sort()
print(a)
"""
输出[1, 2, 3, 4, 5]
"""
b=[2,1,5,7,1,0]
print(sorted(b,reverse=True))

print(b+["ssdd"])
print(b)
"""
[2, 1, 5, 7, 1, 0, 'ssdd']
[2, 1, 5, 7, 1, 0]
"""