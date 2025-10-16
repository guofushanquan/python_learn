"""
题目描述：分析函数参数为一个实例化的对象
编写者:gfsq
时间：2025-10-15
"""
class student:
    x=0
    c=0
def f(stu):
    stu.x=20
    stu.c="s"
a=student()
a.x=2
a.c="sd"
print(a.x,a.c)
f(a)
print(a.x,a.c)
"""
2 sd
20 s
"""