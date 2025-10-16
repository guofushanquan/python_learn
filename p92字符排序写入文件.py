"""
题目描述：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
编写者：gfsq
时间：2025-10-16
"""
fs=open("test.txt","r")
str1=fs.read()
fs.close()
fs=open("test1.txt","r")
str2=fs.read()
fs.close()
str3=str1+str2
word_list=sorted(str3,key=lambda x:x.lower())
# word_list=list(str3)
# print(word_list)
# # for i in range(len(str3)):
# #     word_list.append(str3[i])
# word_list.sort()
str3="".join(word_list)
fs=open("test2.txt","w")
fs.write(str3)
fs.close()

"""
字符串（str）没有 sort() 方法，
因为其不可变特性与 sort() 的 “原地修改” 逻辑冲突。若需排序字符串中的字符，需先转为列表排序，再拼接回字符串；或直接用 sorted() 函数处理，更简洁灵活。
"""


"""
sorted() 是 Python 内置函数，用于对可迭代对象（如列表、字符串、元组、字典等）进行排序，返回一个新的排序后的列表，
不会修改原对象。它支持灵活的排序规则，是处理排序需求的核心工具。
sorted(iterable, key=None, reverse=False)

"""