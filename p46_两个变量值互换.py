"""
题目描述：实现两个变量的值互换
编写者：gfsq
时间：2025-10-14
"""
#第一种办法
a=1
b=2
temp=a
a=b
b=temp
print(a,b)

#第二种办法
a=2
b=3
a,b=b,a
print(a,b)

#第三种办法(数学办法)
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)