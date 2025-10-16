"""
题目要求：数组后移
编写者:gfsq
日期:2025-10-14
"""
"""

#test
for i in range(10,1,-1):
    print(i)

10
9
8
7
6
5
4
3
2
原因分析：range() 的参数逻辑
range(start, stop, step) 的工作机制是：
从 start 开始，每次增减 step（步长），生成小于 stop（当 step 为正数时） 或大于 stop（当 step 为负数时） 的整数序列。
总是达不到stop
"""


def get_list(lenth):
    list = []
    for i in range(lenth):
        list.append(float(input(f"请输入第{i + 1}个数")))
    print("输入完毕！")
    return list


def hou_yi(list, wei):
    if wei >= len(list):
        print("参数错误，移位数大于原字符串长度")
    else:
        new_list = []
        for index in range(len(list) - wei, len(list)):
            new_list.append(list[index])
        for index in range(-1, -len(list) + wei - 1, -1):
            list[index] = list[index - wei]
        for index in range(0, wei):
            list[index] = new_list[index]


number_list = get_list(10)
hou_yi(number_list, 5)
print(number_list)
