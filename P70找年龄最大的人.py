"""
题目描述：找出年龄最大的人
编写者：gfsq
时间：2025-10-15
"""
person_dic={"李":68,"王":38,"张":10}
max_key="李"
for keys in person_dic.keys():
    if person_dic[keys]>person_dic[max_key]:
        max_key=keys
print(f"年龄最大的人为{max_key},其年龄为{person_dic[max_key]}")
