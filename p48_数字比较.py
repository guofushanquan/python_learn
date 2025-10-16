"""
题目描述:使用python实现数字比较
编写者:gfsq
时间:2025-10-14
"""
num1 = float(input("输入第一个数字："))
num2 = float(input("输入第一个数字："))
if num1 < num2:
    print(f"{num1}<{num2}")
elif num1 == num2:
    print(f"{num1}={num2}")
elif num1 > num2:
    print(f"{num1}>{num2}")
else:
    print("未知")

"""
1、elif 后面要加判断条件，else不用加
2、"=="为判断相等的符号，不要写成"="
"""
