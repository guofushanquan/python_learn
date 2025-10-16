"""
题目描述：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数
编写者:gfsq
时间:2025-10-15
"""
def find_ji(number):
    if number%2==0:
        print("输入错误，请输入一个奇数")
        return -1
    count=1
    max_number=9
    while(1):
        if max_number%number==0:
            break
        else:
            count+=1
            max_number=max_number*10+9
    return count

number=int(input("请输入一个奇数:"))
print(find_ji(number))