"""
题目描述:使用python查找字符串
编写人:gfsq
时间：2025-10-14
"""
"""
在 Python 中，str.find(sub) 是字符串对象的内置方法，用于查找子字符串 sub 在当前字符串中首次出现的位置（索引），返回值为子串的起始索引；如果未找到，则返回 -1。
字符串.find(子字符串, start=0, end=len(字符串))
start（可选）：查找的起始位置（索引，默认从 0 开始）；
end（可选）：查找的结束位置（索引，默认到字符串末尾，不包含 end 本身）。
"""
s="hello world, hello python"
print(s.find("llo"))
print(s.find("llo",5,20))
print(s.find("java"))