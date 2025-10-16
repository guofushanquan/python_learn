"""
题目描述：独立编写代码实现input()和output()输入和输出函数信息
编写者：gfsq
时间：2025-10-15
"""
"""
思路描述
1、输入信息
（1）先确定输入几个学生的信息（number)，这道题我们统计学生的姓名(name)、学号(id)、[语文、数学、英文成绩]
（2）创建一个空列表装所有信息all_inf=[]，每个学生的信息为一个子列表，每个学生的成绩又是子列表中的子列表
(3)对于每个学生(for i in number循环）：all_inf.append([]) 输入各个参数，all_inf.[i].append 然后all_inf.append([]),all_inf[i][-1].append()
(4)return
2、输出信息
for list in all_inf:
    for item in list:
        print
"""


def stu_input():
    number = int(input("您要输入几个学生的信息："))
    all_inf = []
    for i in range(number):
        name = input(f"现在输入第{i + 1}个学生的姓名:")
        id = input(f"现在输入第{i + 1}个学生的学号:")
        Ch_score = float(input(f"现在输入第{i + 1}个学生的语文成绩:"))
        Ma_score = float(input(f"现在输入第{i + 1}个学生的数学成绩:"))
        En_score = float(input(f"现在输入第{i + 1}个学生的英语成绩:"))
        all_inf.append([])
        all_inf[i].append(name)
        all_inf[i].append(id)
        all_inf[i].append({})
        all_inf[i][-1]["语文成绩"] = Ch_score#这个注意一下，要先选中字典
        all_inf[i][-1]["数学成绩"] = Ma_score
        all_inf[i][-1]["英语成绩"] = En_score
    return all_inf


def stu_output(all_inf):
    for list in all_inf:
        for item in list:
            print(item)


all_inf = stu_input()
stu_output(all_inf)
