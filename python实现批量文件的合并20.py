"""
题目描述：实现批量文件的合并操作
编写者:gfsq
时间：2025-10-12
"""
"""
fin.read()可以一次性读取文件中的内容,输出字符串
"""
import os


def read_folder(folder_name):
    all_content = []  # 用来装载每一个文件的内容，每一个文件的内容为一个字符串
    for file in os.listdir(folder_name):  # 遍历文件夹
        if file.endswith(".txt"):
            file_path = folder_name + "/" + file  # 拼接文件路径，文件操作的“/”和换行符"\n"要区分清楚
            if os.path.isfile(file_path):  # 判断是否是文件
                with open(file_path, "r", encoding="utf-8") as fin:
                    content = fin.read()
                    all_content.append(content)
    return all_content


"""
os.listdir(folder_name) 返回的是一个列表，列表中的每个元素都是字符串，这些字符串对应着 folder_name 目录下的 “文件或子目录的名称”（不包含完整路径，仅包含条目本身的名字）。
os.path.isfile(file_path) 判断 file_path 是否是一个文件，如果是文件则返回 True，否则返回 False。
os.listdir()
os.path.isfile()
"""

"""
目录和文件的区别：
要搞清楚这个问题，核心是先明确「目录」和「文件」的本质区别，再对应到具体操作的边界 ——f.read()/f.write() 只能操作文件，而目录的操作需要用专门的工具（如 os 模块的目录相关函数）
文件是 “存内容的容器”，目录是 “存文件 / 子目录的索引”
目录不存具体数据，只存 “索引信息”，不可被 “打开”（无法生成文件对象），只能对其 “结构” 进行操作（如创建、删除、遍历）
对目录操作的场景：
场景 1：创建目录（避免文件无处放）
比如你想把所有 .txt 文件放到 ./txt 目录里，但这个目录还不存在 —— 就需要先创建目录，用 os.mkdir()。
import os
if not os.path.isdir("./txt"):  # 先判断目录是否已存在，避免重复创建报错
    os.mkdir("./txt")  # 创建 ./txt 目录
 场景 2：删除目录（清理无用的分类）
 比如 ./old_dir 目录是空的，想删掉它 —— 用 os.rmdir()（只能删空目录）；如果目录非空，用 shutil.rmtree()。
   import os
if os.path.isdir("./old_dir"):
    os.rmdir("./old_dir")  # 删空目录
场景3 遍历目录
略
场景四,判断是否为目录
比如你想确认 ./target 是目录还是文件，避免误把文件当目录操作 —— 用 os.path.isdir()（你代码里也用过）。
import os
path = "./target"
if os.path.isdir(path):
    print(f"{path} 是目录，可遍历/创建子目录")
else:
    print(f"{path} 是文件（或不存在），可打开读写")
"""


def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as fout:
        fout.write("\n".join(content))
    if os.path.isfile(file_path):
        print("文件写入成功")
    else:
        print("文件写入失败,请检查路径是否正确")


dir = "./txt"
print(read_folder(dir))  # 把所有txt文档的内容合并在列表中
# 下一步就是把列表中的内容写在一个文档中
write_file("./文本文件汇总.txt", read_folder(dir))

"""
你的代码报错 PermissionError: [Errno 13] Permission denied: './' 的核心原因是：试图将目录（文件夹）当作文件来写入，而操作系统不允许这种操作。
open 函数在以 "w"（写入模式）打开路径时，要求路径必须是一个文件（如果文件不存在，会创建新文件）。
但如果你传入的是目录（文件夹）路径（如 "./"），操作系统会拒绝访问（因为文件夹不能被当作文件直接写入），从而抛出 “权限不足” 的错误（Permission denied）。
"""

"""
文件对象.read() 是 Python 中文件对象的核心方法之一，作用是从文件中读取内容，具体行为取决于是否传入参数，以及文件的打开模式（文本模式 / 二进制模式）。
read() 方法会从文件的当前位置开始读取内容，返回读取到的结果。它有两种常用用法：
1. 不带参数：file.read()
读取文件中从当前位置到末尾的所有内容，返回一个字符串（文本模式下，'r'）或字节串（二进制模式下，'rb'）。读取完成后，文件内部的 “指针” 会移动到文件末尾，再次调用 read() 会返回空字符串（因为已经没有内容可读）。
2. 带参数：file.read(size)
size 是可选参数，指定要读取的字节数（文本模式下，通常按字符数处理，但本质仍是字节数）。
如果文件剩余内容的字节数 ≤ size，则读取所有剩余内容；
如果文件剩余内容的字节数 > size，则只读取 size 字节的内容，文件指针停在本次读取的末尾，下次读取从这里继续。
with open("test.txt", "r", encoding="utf-8") as f:
    # 第一次读取：前 5 个字符（字节数可能因字符编码不同而变化，utf-8 中英文占 1 字节，中文占 3 字节）
    part1 = f.read(5)
    print("第一次读取：", part1)  # 输出：第一次读取：Hello

    # 第二次读取：从上次结束位置继续读 10 个字符
    part2 = f.read(10)
    print("第二次读取：", part2)  # 输出：第一次读取：, Python!
"""
"""
f.write() 是 Python 中文件对象的核心写入方法，作用是将指定内容写入到已打开的文件中，是实现数据持久化（将内存中的数据保存到硬盘文件）的关键操作。
语法：f.write(content)
参数 content：要写入的内容。
若文件以文本模式（'r'/'w'/'a' 等，带 encoding 参数）打开，content 必须是字符串（str 类型）；
若文件以二进制模式（'rb'/'wb'/'ab' 等）打开，content 必须是字节串（bytes 类型，如 b"hello"）。
with open("notes.txt", "w", encoding="utf-8") as f:
    # 写入单行字符串
    count1 = f.write("第一行内容：Hello World\n")  # 手动加换行符 \n 实现分行
    # 写入多行字符串（可拼接）
    count2 = f.write("第二行内容：Python 写入操作\n第三行内容：结束\n")
    
    print(f"第一次写入了 {count1} 个字符")  # 输出：第一次写入了 15 个字符（包含 \n）
    print(f"第二次写入了 {count2} 个字符")  # 输出：第二次写入了 30 个字符（包含两个 \n）
第一行内容：Hello World
第二行内容：Python 写入操作
第三行内容：结束
"""
