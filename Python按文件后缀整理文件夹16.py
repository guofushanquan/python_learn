"""
题目描述：Python按文件后缀整理文件夹
编写者：gfsq
日期：2025-10-11
"""
import os
import shutil

dir = "."
for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")
    if ext == "txt":
        shutil.move(f"{dir}/{file}", f"{dir}/{ext}/{file}")
    print(file, ext)
# 删除”py"文件夹，它是空的
if os.path.isdir("py"):
    os.rmdir("py")
"""
若为非空，则
用 shutil.rmtree(path) 函数，可强制删除包含内容的文件夹（慎用，删除后无法恢复）：
import shutil

if os.path.isdir("py"):
    shutil.rmtree("py")  # 无论是否为空，都会删除（包括所有内容）

"""

"""
os.path.splitext(path)：分割文件路径的 “文件名” 和 “扩展名”
作用：将一个文件路径拆分成 “文件名（含路径）” 和 “扩展名” 两部分，返回一个包含这两部分的元组。
"""

"""
os.path.isdir(path)：判断路径是否为 “目录（文件夹）”
作用：检查给定的路径是否存在，且该路径对应的是一个目录（文件夹），返回布尔值 True 或 False。
"""
