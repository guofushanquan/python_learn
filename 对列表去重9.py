"""
题目：对列表去重,删除列表内的重复元素
编写人:gfsq
时间：2025年10月11日
"""
def remove_duplicates(lst):
    list_new=[]
    for i in lst :
        if i not in list_new:
            list_new.append(i)
    return list_new

lst=[1,5,7,7,8,8,4,4,2,2,5,6,7,4]
print(remove_duplicates(lst))
lst2=[1,5,7,7,8,8,4,4,2,2,5,6,7,4]
print(list(set(lst2)))#这种方法会打乱顺序
