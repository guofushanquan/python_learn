"""
题目描述：将一个数按照规律插入到数组中
编写人:gfsq
日期：2025-10-13
"""

# 下面的代码都是测试用的
# number_list=[1,23,34]
# print(number_list[1])
# number_list[1]=10
# print(number_list[1])
"""
number_list[3]=10
#IndexError: list assignment index out of range
"""


# number_list.insert(1,15)
# print(number_list)
# [1, 15, 10, 34],这种方法可以将内容插入列表,注意15的位置

# 下面不再使用笨方法插入一个元素,只理清对应思路
def insert_number(number_list, number):  # 要求number_list为递增数列
    # 找到要插入的位置
    index = 0
    max_flag = 1
    for index in range(0, len(number_list)):
        if number_list[index] >= number:
            max_flag = 0
            break
    if max_flag:
        number_list.append(number)
    else:
        number_list.insert(index, number)  # 就是要插入index
    return number_list


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(insert_number(number_list, 6.7))
