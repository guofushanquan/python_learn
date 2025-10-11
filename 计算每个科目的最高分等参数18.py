"""
题目描述：计算每个科目的最高分等参数
编写者：gfsq
日期：2025-10-11
"""
course_grade = {}
with open("./txt/course_grade.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line[-1] == "\n":
            line = line[:-1]
        name, course, grade = line.split(",")
        if course not in course_grade:  # 如果字典中没有该学生，则添加该学生
            course_grade[course] = []
        course_grade[course].append(float(grade))  # 将成绩添加到该学生的成绩列表中
"""
course_grade.items() 是字典的一个内置方法，作用是返回字典中所有 “键值对” 的可迭代对象，每个键值对以元组 (键, 值) 的形式存在。
"""
for course, grade in course_grade.items():
    print(course, grade)
    print("最高分为：", max(grade))
    print("最低分为：", min(grade))
    print("平均分为：", sum(grade) / len(grade))
