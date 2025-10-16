"""
题目描述:将字符写入到磁盘中
编写人:gfsq
时间:2025-10-16
"""
file_name=input("请输入您要写入的文件路径")
fs=open(file_name,"w")#每次写上次的内容会被覆盖
content=input("请输入您要写入的内容:")
while(content!="#"):
    fs.write(content+"\n")
    content = input("请输入您要写入的内容:")
fs.write("end")
fs.close()

"""
1、从中断键入的字符串的"\n"不会传递给变量
2、在 Python 中，fs=open(file_name, "w") 和 with open(file_name, "w") as fs 都用于打开文件并进行写入操作，
但它们在资源管理（文件关闭） 和代码安全性上有本质区别，核心差异在于是否需要手动关闭文件。
这是 Python 的上下文管理器（context manager） 语法，会在代码块执行完毕后自动关闭文件，无论是否发生异常。
"""

"""
f.read() 会读取文件中所有的换行符（及其他所有字符），完全保留文件的原始内容结构。如果需要处理换行符（如去除或替换），可以对读取后的字符串使用 replace("\n", ...) 等方法。
"""
