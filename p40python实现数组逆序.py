"""
题目描述：使用python实现数组逆序
编写者：gfsq
时间：2025-10-14
"""


def swap(list, index):
    temp = list[index]
    list[index] = list[-index - 1]
    list[-index - 1] = temp


list1 = [1, 23, 2, 4, 5, 6, 7, 6]
"""
算法流程：
判断列表长度是奇数还是偶数
若为奇数，则遍历到[len(list)-1]/2-1
若为偶数，则遍历到[len(list)/2]-1
交换前半部分和后半部分即swap(list[i],list[-i-1])(i为前半部分的index)
"""
lenth = len(list1)
# if lenth % 2 == 0:
#     max_index = lenth / 2
# else:
#     max_index = (lenth - 1) / 2
max_index=lenth//2
for i in range(0, max_index):
    swap(list1, i)

print(list1)
"""
list.reverse() 是 Python 列表（list）的内置方法，
用于将列表中的元素原地反转（即直接修改原列表，而不是创建新列表）。
无返回值
"""
list1.reverse()
print(f"再使用list.reverse()的结果为{list1}")
"""
在 Python 中，// 是整除运算符（也叫 “地板除”），
用于计算两个数相除的整数部分，且结果会向下取整（即向负无穷方向取最接近的整数）。
"""