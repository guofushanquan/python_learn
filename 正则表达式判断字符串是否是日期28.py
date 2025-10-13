"""
题目描述：使用正则表达式判断字符串是否是日期
编写者：gfsq
日期：2025-10-13
"""
import re


def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}", date) is not None


date1 = "2015-10-13"
date2 = "2046-12-12"
date3 = "22-2-12"
date4 = "21-12-2"
"""
正则表达式（Regular Expression，简称 regex 或 regexp）
是一种用于描述、匹配、查找、替换文本中 “特定模式字符串” 的工具。
它通过预先定义的 “规则表达式”，精准描述需要匹配的文本结构，从而高效完成复杂的字符串操作。

核心作用
验证格式：如检查邮箱、电话号码、身份证号是否符合规范。
提取信息：从大段文本中提取 URL、日期、数字等特定内容。
替换文本：批量替换符合某种模式的字符串（如统一修改日期格式）。
分割文本：按复杂规则分割字符串（如按 “逗号 + 任意空格” 分割）。

正则表达式由普通字符（如字母、数字）和元字符（具有特殊含义的字符，如 *、+、.）组成。
元字符是正则的 “核心工具”，通过它们组合出灵活的匹配规则。



"""

print(date1, date_is_right(date1))
print(date2, date_is_right(date2))
print(date3, date_is_right(date3))
print(date4, date_is_right(date4))
"""
is not None的作用是将re.match()的 “匹配对象 / None” 结果明确转换为True/False
is not None 是一种用于判断 “对象是否不是 None” 的语法，属于身份运算符的组合使用，
核心作用是检查变量 / 表达式的结果是否为 None（Python 中表示 “空值” 的 singleton 对象）
x = None
print(x is not None)  # 输出: False（x 是 None）

y = "hello"
print(y is not None)  # 输出: True（y 不是 None）

# 函数返回值场景（如 re.match）
import re
match = re.match(r"\d+", "123")
print(match is not None)  # 输出: True（匹配成功，返回 Match 对象，不是 None）
"""
