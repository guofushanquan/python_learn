"""
问题描述：解决约瑟夫环问题
编写者:gfsq
时间：2025-10-15
"""
# from p61数组后移 import get_list
"""
思路理清：
1、生成一个列表
count=0
2、循环(这里使用while(len(list>1)):count计算报数值+1，(1)判断到设定值时就移除index所在元素index不用加1 ,count=0，否则index+1 (2)判断index==len(list) 是则Index=0，
"""
def get_list(lenth):
    list = []
    for i in range(lenth):
        list.append(float(input(f"请输入第{i + 1}个数")))
    print("输入完毕！")
    return list
def ysf(list,gap):
    count=0
    index=0
    while (len(list) > 1):
        count += 1#当前人报号
        if count == gap:
            list.pop(index)
            count=0
        else:
            index+=1
        if index==len(list):
            index=0
    return list



#主程序
number_list=get_list(3)
print(f"原始数组为：{number_list}")
gap=int(input("请输入报数间隔:"))
print(f"约瑟夫循环后的数组为{ysf(number_list,gap)}")
"""
list.pop() 是 Python 列表（list）的内置方法，用于移除并返回列表中指定位置的元素。
如果不指定位置，默认移除并返回列表的最后一个元素。
有返回值，且会改变原数组
"""

"""
在 Python 中从其他文件导入函数时出现 “函数不断重复执行” 的问题，
通常是因为被导入的文件（如 p61数组后移.py）中存在直接执行的代码（而非仅定义函数），
导致导入时这些代码被自动执行，进而产生重复效果。
问题根源：被导入文件中的 “可执行代码”
当你用 from 模块 import 函数 导入时，Python 会先执行被导入文件（p61数组后移.py）中的所有顶层代码（即不在函数 / 类定义内部的代码），
然后再导入指定的函数。
如果 p61数组后移.py 中不仅定义了 get_list() 函数，还包含直接执行的代码（如打印、调用函数等），
那么每次导入时这些代码都会被执行一次。若当前文件多次导入（或导入后又触发了相关逻辑），就会出现 “重复执行” 的现象。
"""

