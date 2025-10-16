"""
题目描述:从键盘输入字符串，将小写字符全部转换为大写字符，然后输出到磁盘文件中保存
编写者:gfsq
时间：2025-10-16
"""
str1=input("请输入一个字符串")
str1=str1.upper()
fp=open("test.txt","w")
fp.write(str1)
fp.close()
"""
string.upper() 是 Python 字符串（str）的内置方法，用于将字符串中所有小写字母转换为对应的大写字母，并返回一个新的字符串（原字符串不会被修改，因为字符串是不可变类型）。
返回值：一个新字符串，其中原字符串中的所有小写字母（a-z）被转换为大写字母（A-Z），其他字符（如大写字母、数字、符号、中文等）保持不变。
user_input = "python"
keyword = "PYTHON"

# 忽略大小写比较
if user_input.upper() == keyword.upper():
    print("匹配成功")  # 输出：匹配成功
"""

"""
string.lower
lower()：全大写转小写，其他字符不变（与 upper() 功能相反）；
capitalize()：仅将字符串首字母转为大写，其余小写（如 "hello" → "Hello"）；
title()：将每个单词的首字母转为大写，其余小写（如 "hello world" → "Hello World"）。
"""