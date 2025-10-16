"""
题目描述:求0-7组成的奇数个数
编写者:gfsq
时间:2025-10-15
"""
min=4
sum=0
wei=int(input("请输入数的位数"))
if wei>2:
    ci=wei-2
    for i in range(ci):
        min*=8
min*=7

print(min)