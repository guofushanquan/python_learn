"""
题目描述:数字范围(闭区间)，输出区间内所有偶数
编写者：gfsq
时间：2025-10-11
"""


def even_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")


start, end = map(int, input("请输入起始和结束数字").split())
even_numbers(start, end)
