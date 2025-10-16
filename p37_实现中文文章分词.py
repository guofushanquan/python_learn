"""
题目说明：使用python实现中文文章分词
编写者：gfsq
日期:2025-10-13
"""
import jieba  # 中文分词需要使用的库
import re

with open("Chinese.txt", "r", encoding="utf-8") as f:
    content = f.read()
content = re.sub(r"[\s，\”\‘-。<>《》]", "", content)
# 把杂乱的符号去点
word_list = jieba.cut(content)
"""
print(word_list)
#输出<generator object Tokenizer.cut at 0x0000028101CE31C0>
"""
print(list(word_list))
"""
jieba.cut(content) 是中文分词库 jieba（“结巴”）中最核心的分词方法之一，
主要作用是将一段连续的中文文本（content）分割成一个个独立的词语（或 “词”），
解决中文文本没有天然空格分隔的问题（与英文不同，中文词语之间通常没有明显的分隔符）。

返回值：可迭代的生成器（generator）
jieba.cut() 的返回结果不是直接的列表，而是一个可迭代对象（生成器）。
需要通过 for 循环遍历，或用 list() 转换为列表才能直观查看分词结果。
"""
