"""
题目描述：学习链表
编写人:gfsq
时间：2025-10-15
"""
list=[input(f"请输入第{i+1}个元素") for i in range(2)]
print(list)
#大于0的为i的平方，小于0的为i的三次方，否则就为0
list=[i**2 if i>0 else i**3 if i<0 else 0 for i in range(-4,7)]
print(list)
"""
重温列表推导式
[表达式(也可以是函数) for 变量 in 可迭代对象]

[表达式 for 变量 in 可迭代对象 if 条件]
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in nums if x % 2 == 0]
print(evens)  # 输出：[2, 4, 6, 8]
s = "abc123def456"
non_letters = [c for c in s if not c.isalpha()]
print(non_letters)  # 输出：['1', '2', '3', '4', '5', '6']

"""

"""
python的链表之后再学，学习类和面向对象的时候
"""
