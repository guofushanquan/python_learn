"""
题目描述：统计目录下的文件大小
编写者：gfsq
日期：2025-10-11
"""
import os
#单个文件的大小计算
print(os.path.getsize("englishtex.txt"))
#1,814 字节
#目录下所有文件的大小计算
#print(sum(os.path.getsize(f) for f in os.listdir("D:\pt_prac")))
sum_size=0
for file in os.listdir("."):
    if os.path.isfile(file):
        print(file)
        sum_size+=os.path.getsize(file)
print(f"all size of dir:{sum_size/1000}KB")
"""
在 Python 中，os 是 Operating System（操作系统） 的缩写，
它是 Python 内置的一个标准库（模块），专门用于与操作系统进行交互。
通过 os 模块，你可以在代码中实现对文件、目录、环境变量、系统信息等的操作，
而无需关心底层操作系统的差异（如 Windows 和 Linux 的路径格式不同）。
"""