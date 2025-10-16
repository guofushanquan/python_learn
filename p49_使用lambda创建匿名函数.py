"""
题目要求:使用lambda创建匿名函数
编写者:gfsq
时间:2025-10-14
"""
power=lambda x,y:x ** y
print(power(2,3))
"""
在 Python 中，lambda 是用于创建匿名函数（即没有名字的函数）的关键字。
它的核心作用是快速定义简单的、单行的函数，通常用于临时需要一个函数的场景（如作为其他函数的参数）。
lambda 参数: 表达式
表达式：函数的返回值，必须是单行表达式（不能包含循环、条件判断的多行逻辑等）
lambda 的优势在于 “即用即弃”，尤其适合作为其他函数的参数（如排序、过滤、映射等场景）。
# 列表中的元素是元组（姓名, 年龄）
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]

# 按年龄升序排序（用 lambda 提取年龄作为排序key）
sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)  # 输出：[('Bob', 20), ('Alice', 25), ('Charlie', 30)]

# 对列表中的每个数求平方
nums = [1, 2, 3, 4]
squared_nums = list(map(lambda x: x **2, nums))
print(squared_nums)  # 输出：[1, 4, 9, 16]








"""