"""
题目描述：实习不同文件的关联
编写者:gfsq
时间：2025-10-12
"""


def gen_dic(file_name):
    dic = {}  # 创建一个空字典，保存老师及其对应的课程，老师为字符串类型，课程为list类型
    with open(file_name, "r", encoding="utf-8") as fin:
        for line in fin:
            if line[-1] == "\n":
                line = line[:-1]  # 去掉换行符
            course, teacher = line.split(",")  # 将一行字符串按照逗号分割，得到课程和老师
            if course not in dic:
                dic[course] = []  # 这里让新加入字典的keuy对应的value为空列表，因为考虑的情况为一个科目可能有多个老师教授
            dic[course].append(teacher)
    return dic


def read_file(file_name):
    """
    读取文件内容并将每行数据分割成列表

    参数:
        file_name (str): 要读取的文件名

    返回:
        datas: 包含文件所有行的列表，每行数据被分割为子列表
    """
    datas = []  # 用于存储处理后的数据列表
    # 使用with语句打开文件，确保文件正确关闭
    with open(file_name, "r", encoding="utf-8") as fin:
        for line in fin:  # 逐行读取文件内容
            if line[-1] == "\n":
                line = line[:-1]  # 去掉换行符
            data = line.split(",")
            datas.append(data)
    return datas


# 该函数用来关联教师_课程字典和课程成绩数据
def associate(teacher_dic, datas):
    for data in datas:
        teacher_list = teacher_dic[data[1]]
        teacher_string = str(teacher_list)
        teacher_string = teacher_string[2:len(teacher_string) - 2]
        data.append(teacher_string)
    return datas


def write_file(file_name, datas):
    with open(file_name, "w", encoding="utf-8") as fout:
        for data in datas:
            fout.write(",".join(data) + "\n")


teacher_dic = gen_dic("./txt/teacher.txt")
print(teacher_dic)
datas = read_file("./txt/course_grade.txt")
datas = associate(teacher_dic, datas)
print(datas)
write_file("./txt/course_grade.txt", datas)
print("文件写入成功")
"""
dict.get(key, default=None) 是字典的内置方法，作用是：
如果字典中存在键 key，则返回该键对应的值；
如果字典中不存在键 key，则返回指定的 default 值（默认是 None，即不指定 default 时返回 None）。
"""
