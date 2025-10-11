"""
题目描述:对学生成绩排序
编写者：gfsq
时间：2025年10月11日
"""
students=[{'name':'张三','score':95},#这相当于一个字典，
          {"name":"李四","score":99},
          {"name":"王五","score":91},
          {'name':'赵六','score':85}]
students_new=sorted(students,key=lambda x:x["score"])#lambda为匿名函数，
"""
lambda 参数: 表达式
必须是单行的简单表达式（不能包含循环、多分支条件语句等复杂逻辑），函数的返回值就是这个表达式的计算结果。

"""
print(students_new)
print(students)
