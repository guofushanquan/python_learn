"""
题目描述:读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊
编写者：gfsq
时间：2025-10-15
"""
for i in range(7):
    number=int(input("输入"))
    if not (number>=1 and number<=50):
        number = int(input("输入"))
    print("*"*number)