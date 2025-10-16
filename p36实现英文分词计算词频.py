"""
题目描述：使用python实现英文分词计算词频
编写者:gfsq
时间：2025-10-13
"""
import re

# 怎么分词
"""
1、先读取文件中的字符串
2、一个单词两端一定是特殊字符（除了a-zA-z)
4、分出来re.findall(),因为re.search()只返回第一个，这个还得多看看
"""


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as s:
        content = s.read()
    return content


def get_word_count(word_list, word_count):
    for word in word_list:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    return word_count


content = read_file("./txt/englishtex.txt")
pattern = r"[^a-zA-Z]*([a-zA-Z]+)[^a-zA-Z]*"
word_list = re.findall(pattern, content)
print("word_list为：", word_list)
word_count = {}  # 字典
print("单词和次数统计结果为:", get_word_count(word_list, word_count))
"""
也可以使用re.split(pattern,str)
re.split(pattern, string, maxsplit=0, flags=0)
str.split(sep)：只能用固定字符串（sep）作为分隔符，且无法处理 “多种分隔符”“连续分隔符” 等复杂情况（如同时用逗号、空格、分号分割）。
re.split(pattern)：能用正则表达式定义分隔符规则，可处理 “多种分隔符混合”“连续分隔符”“带特殊字符的分隔符” 等场景。
若使用re.split()
代码则为words_list=re.split(r"[\s.-_?!@#]",content)
\s 等价于字符集 [ \t\n\r\f\v ]，即匹配以下所有 “空白” 相关的字符：
空格（，最常见的空白）；
制表符（\t，键盘 Tab 键产生的字符）；
换行符（\n，换行产生的字符）；
回车符（\r，部分系统换行时的辅助字符）；
垂直制表符（\v）和换页符（\f，较少见的空白字符）。
"""

"""
统计每个单词有多少次，可以使用pandas库，这里先不学习，后面会系统学习
"""
