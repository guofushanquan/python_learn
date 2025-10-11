"""

题目描述:给定一个数N，求前N个数字的平方和
编写者：gfsq
时间：2025-10-11

"""
def sum_square(number):
    sum=0
    for i in range(1,number+1):
        sum+=i**2
    return sum

number = int(input("请输入一个整数"))
print(sum_square(number))
