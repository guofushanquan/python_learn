"""
题目描述：提取一本小说中出现次数最多的人名
编写者：gfsq
时间:2025-10-13
"""
import jieba.posseg as posseg
import re
import pandas as pd

with open("ni_tian_xie_shen.txt","r",encoding="utf-8") as f:
    content=f.read()
name_list=[]
for word,flag in posseg.cut(content):
    if flag=="nr":
        name_list.append(word)
print(name_list)
print(pd.Series(name_list).value_counts())

