"""
问题描述：统计每个兴趣的学生人数
编写者：gfsq
编写时间：2025/10/12
"""
import re
#定义一个函数，其参数输入为一个文本数据，输出为一个字典
def count_interests(text):
    #先创建一个空字典
    interests_count = {}
    #读取文本内容
    with open(text,"r",encoding='utf-8') as f:
        for line in f:
            if line[-1]=="\n":
                line=line[:-1]
            word_list=re.split(r" |,",line)
            word_list.remove(word_list[0])#删除第一个元素
            for interests in word_list:
                if interests not in interests_count:
                    interests_count[interests]=0
                interests_count[interests]+=1
    return interests_count
print(count_interests("兴趣统计.txt"))
"""
list.remove(x) 是 Python 列表的内置方法，核心作用是从列表中移除 “第一个出现的指定元素 x”，并直接修改原列表（原地操作，无返回值）。
"""

"""
用 re.split(pattern, string) 实现多字符分割
re.split() 支持传入一个正则表达式模式，通过 |（表示 “或”）可以指定多个分隔符，实现 “按任意一个分隔符分割”。

import re

s = "apple,banana;orange,grape;pear"

# 按 , 或 ; 分割（正则模式 ",|;" 表示匹配逗号或分号）
result = re.split(r",|;", s)  # r 表示原始字符串，避免转义问题

print(result)
# 输出：['apple', 'banana', 'orange', 'grape', 'pear']

"""


"""
列表推导式
核心包含「元素表达式」「循环语句」（可多层）和「条件语句」（可选，分两种场景）
1、
squares = [x ** 2 for x in range(1, 6)]
2、
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
3、
num_transform = [-x if x % 2 == 1 else x for x in range(1, 6)]
遍历可迭代对象时，所有变量都会保留，但会根据 “分支条件” 选择用「表达式 1」或「表达式 2」生成元素（类似三元运算符，控制元素的生成规则，而非筛选元素）。
4、
flattened = [x for sublist in nested_list for x in sublist]
nested_list = [[1, 2], [3, 4], [5, 6]]
# 先遍历外层列表（sublist），再遍历内层列表（x）
flattened = [x for sublist in nested_list for x in sublist]
print(flattened)  # 输出：[1, 2, 3, 4, 5, 6]
"""
