"""
题目描述:读取成绩文件计算最高分等参数
编写者:gfsq
时间:2025年10月11日
"""
def file_read(file_name):
    datas=[]
    with open(file_name,"r",encoding="utf-8") as fin:
        for data in fin:
            if data[-1]=="\n":
                data=data[:-1]
            datas.append(data.split(","))
    return datas

def get_max_grade(datas):
    max_grade=datas[0][2]
    for items in datas:
        if items[2]>max_grade:
            max_grade=items[2]
    return max_grade

def get_min_grade(datas):
    min_grade=datas[0][2]
    for items in datas:
        if items[2]<min_grade:
            min_grade=items[2]
    return min_grade

def get_avg_grade(datas):
    avg_grade=sum([int(x[2]) for x in datas])/len(datas)
    return avg_grade
"""
[int(x[2]) for x in datas]
这是一个列表推导式
[int(x[2]) for x in datas]是 Python 中的列表推导式（List Comprehension），这是一种简洁创建列表的语法，结构为：[表达式 for 变量 in 可迭代对象]
作用是：遍历 “可迭代对象” 中的每个元素，用 “表达式” 处理每个元素，最终生成一个包含处理结果的新列表。
int(x[2]) for x in datas

"""
def write_file(max_grade,min_grade,avg_grade,file_name):
    with open(file_name,"w",encoding="utf-8") as fout:
        fout.write(f"这些学生的最高分为{max_grade}分，最低分为{min_grade}分，平均分为{avg_grade}分")

#先将数据读取存在变量中
datas=file_read("student_grade_input.txt")
#求最大值
# max_grade=max(datas,key=lambda x:x[2])
max_grade_list=max(datas ,key=lambda x:x[2])
max_grade_2=max_grade_list[2]
print(f"这些学生的最高分为{max_grade_2}分")
"""
max 是 Python 内置函数，核心功能是从 “可迭代对象” 中找出 “最大值”，但它有两种关键用法：
带 key 参数用法：有 key 参数时，不直接比较元素本身，而是先通过 key 指定的函数处理每个元素，用 “函数返回值” 作为比较依据，最终返回的是 “原元素中对应返回值最大的那个”。
key 参数必须传入一个 “函数”
max 返回的是 “原元素”，不是比较值：
"""
max_grade=get_max_grade(datas)
#求最小值
# min_grade=min(datas,key=lambda x:x[2])
min_grade=get_min_grade(datas)
#求平均分
# avg_grade=sum([int(x[2]) for x in datas])/len(datas)
"""
sum() 会遍历 iterable（可迭代对象）中的每个元素，将所有元素累加，最终返回总和。

"""
avg_grade=get_avg_grade(datas)
#输出，写到一个文档里
write_file(max_grade,min_grade,avg_grade,"student_grade_para.txt")


print(f"这些学生的最高分为{max_grade}分，最低分为{min_grade}分，平均分为{avg_grade}分")
"""
可迭代对象（Iterable）是指能被 for 循环遍历、且能通过 iter() 函数获取迭代器的对象，常见类型如下：
集合类型是无序的可迭代对象，元素不重复：
"""