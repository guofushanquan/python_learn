"""
题目描述:求前N个数字的平方和
编写者：gfsq
日期：2025年10月11日

"""
def remove_elements(list1,list2):
    for items in list2:
        list1.remove(items)
    return list1
list1 = [1,2,3,4,5,6,7,8,9,10,5,6]
list2=[5,6]
print(remove_elements(list1,list2))
print(list1)
"""
list.remove(x) 的逻辑是：在列表中从左到右查找，找到第一个等于 x 的元素并将其删除，不会处理后续重复的 x
如果需要删除列表中所有等于 x 的元素，不能直接用 remove() 循环（可能漏删），更简单的方式是用列表推导式生成新列表，例如：
lst = [2, 5, 3, 5, 1]
x = 5
lst = [i for i in lst if i != x]  # 过滤掉所有5
print(lst)  # 输出：[2, 3, 1]

list.remove(x)也会改变原来的list
"""

"""
列表作为函数参数传入后，函数内修改会直接影响原列表
这是因为列表是 “可变对象”，在 Python 中，当可变对象（列表、字典等）作为参数传入函数时，传递的是 “对象的引用”（可以理解为内存地址）。
函数内部对列表的修改（如 remove()、append()、修改元素等），本质上是在操作原列表的内存地址，因此会直接改变原列表的值。

"""

list3 = [1,2,3,4,5,6,7,8,9,10,5,6]
list4=[5,6]
list5=[i for i in list3 if i not in list4]
print(list5)
