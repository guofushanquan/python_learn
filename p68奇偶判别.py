"""
题目描述：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
编写者:gfsq
时间:2025-10-15
"""
"""
先输入一个整数
判断这个数为偶数还是技术
偶数调用even_number_sum,for i in range(2,n+2,2)

奇数调用odd_number_sum,for i in range(1,n+2,2)
"""

def even_number_sum(number):
    sum=0.0
    for i in range(2,number+2,2):
        sum+=1/i
    return sum

def odd_number_sum(number):
    sum=0.0
    for i in range(1,number+2,2):
        sum+=1/i
    return sum

number=int(input("请输入一个整数"))
if (number&1==1):
    print(odd_number_sum(number))
else:
    print(even_number_sum(number))