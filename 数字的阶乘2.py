"""
题目：编写一个程序，输入一个整数，求出该整数的阶乘。
编写人：gfsq
编写时间：2025/10/10
"""
#使用函数进行代码编写
def factorial(number):
    result=1
    while number>0:
        result*=number
        number-=1
    return result
if __name__=="__main__":

    number=int(input("请输入一个整数："))
    print(f"{number}的阶乘是{factorial(number)}")