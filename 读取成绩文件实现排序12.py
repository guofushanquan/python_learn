"""
 题目名称：读取文件，对文件中的成绩进行降序排序
 编写人：GFSQ
 编写时间：2025/10/11
"""


def read_file(filename):
    result = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line[-1]=="\n":
                line = line[:-1]  # 去掉每行末尾的换行符
            result.append(line.split(","))  # line.split(",")会返回一个列表
    return result


"""
with open(filename, "r", encoding="utf-8") as f:
这是 Python 中安全读取文件的标准写法，包含 3 个关键部分：
open()函数：用于打开文件，接收 3 个重要参数：
filename：要打开的文件路径（这里是"student_grade_input.txt"，表示与代码文件同目录下的该文件）；
"r"：打开模式（"r"表示只读模式，只能读取文件内容，不能修改）；
encoding="utf-8"：指定文件编码格式（utf-8是通用编码，支持中文，避免读取中文时出现乱码）。
as f：将打开的文件对象赋值给变量f，后续通过f操作文件（比如读取内容）。
with语句：这是 Python 处理文件的推荐方式，作用是自动管理文件关闭。当with语句块执行结束后（无论是否报错），会自动关闭文件，避免因忘记关闭文件导致的资源泄露（比如文件被占用无法修改）。

"""
"""
for line in f:：逐行读取文件内容
文件对象f是一个可迭代对象，for line in f会逐行读取文件内容，每次循环中line变量会接收文件中的一行内容（包含每行末尾的换行符\n）。
"""


def sort_grades(datas):
    sorted(datas, key=lambda x: int(x[2]), reverse=True)
"""
sort_grades 函数没有返回值
"""


def write_file(datas, filename):
    with open(filename, "w", encoding="utf-8") as fout:
        for data in datas:
            fout.write(",".join(data) + "\n")

"""
filename：要写入的文件路径（如果文件不存在，会自动创建；如果文件已存在，会覆盖原有内容—— 这是 “写入模式” 的重要特点）；
"W"：打开模式（实际写法通常是小写 "w"，Python 对大小写不敏感，但习惯用小写），表示写入模式：
若文件不存在，创建新文件；
若文件已存在，清空原内容后写入新数据（注意：这会覆盖原有内容，如需追加内容，应使用 "a" 模式）；
encoding="utf-8"：指定写入文件时的编码格式（和读文件保持一致，避免中文乱码）。
"""
"""
",".join(data)：将列表转换为字符串（关键字符串操作）
join() 是字符串的内置方法，作用是用指定字符串（这里是逗号 ","）连接列表中的所有元素，返回一个新字符串。
例如：data = ["赵六", "85"]，",".join(data) 会将列表中的两个元素用逗号连接，得到字符串 "赵六,85"；
这一步是读文件时 split(",") 的 “逆操作”：读文件时用 split 把字符串拆成列表，写文件时用 join 把列表合并成字符串，保证文件内容格式统一（和原文件的 “姓名，成绩” 格式一致）。
"""
"""
fout.write(...)：写入文件
fout.write(字符串) 是文件对象的写入方法，作用是将括号中的字符串内容写入到文件中。
注意：write() 方法只接受字符串作为参数，因此必须先用 join() 把列表 data 转换成字符串才能写入；
每次循环写入一个处理后的字符串（带换行符），最终文件会按行保存所有数据。
"""


# 读取文件
datas = read_file("student_grade_input.txt")
print(datas)
# 排序数据
sort_grades(datas)
# 此时datas为二维列表，每个元素为字符串列表
# 写出文件
write_file(datas, "student_grade_output.txt")
"""
sorted()函数也有返回值，对可迭代对象本身进行排序操作吗？ 不会改变可迭代对象本身！
出现错误的原因是因为我使用函数后进行赋值操作，但是函数并没有返回值
list.sort()函数无返回值，返回排序后的列表，也改变原列表
这一点与列表自带的 sort() 方法（原地排序）有本质区别：
sort() 是列表的方法，无返回值（返回 None），但会直接修改原列表（原地排序）；
sorted() 是内置函数，有返回值（新列表），不修改原对象。
sorted() 不仅能处理列表，还能处理其他可迭代对象（如元组、字典、字符串等），且始终返回一个新列表。
因此，在需要保留原对象、同时获取排序结果时，应使用 sorted()；若只需对列表排序且无需保留原列表，可使用 list.sort()。
"""