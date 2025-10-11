"""
题目描述:给定一个区间（闭区间），输出这个区间内所有的素数
编写者：gfsq
时间：2025-10-11
"""
import math


def is_prime(left, right):
    if (left <= 0 or right <= 0):
        print("请输入大于0的数")
        return 0
    for number in range(left, right + 1):
        if number == 1:
            print(number)
        else:
            if number % 2 == 0:
                continue
            else:
                jude = int(math.floor(number / 2))
                while number % jude != 0:
                    jude -= 1
                if jude == 1:
                    print(number)


left_number, right_number = map(int, input(
    "请输入区间：").split())  # input("请输入区间：").split()会按照空白字符（空格、制表符、换行符等）分割，返回一个列表（其元素仍然是字符串类型）
is_prime(left_number, right_number)
