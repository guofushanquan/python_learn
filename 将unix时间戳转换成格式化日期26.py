"""
题目描述：将unix时间戳转换成格式化日期
编写者：gfsq
日期：2025-10-12
"""
import datetime


def unix_to_date(unix_timestamp):
    date_obj = datetime.datetime.fromtimestamp(unix_timestamp)
    return date_obj.strftime("%Y-%m-%d %H:%M:%S")


'''
这个占位符有固定要求（strptime()也这样记忆就好了)
Y-年
m-月
d-日
H-小时
M-分钟
S-秒
datetine.datetime.strptime()
'''

"""
datetime.datetime.fromtimestamp() 是 Python 中 datetime 模块的一个类方法，核心作用是将 “时间戳（timestamp）” 转换为对应本地时间的 datetime.datetime 对象。
"""
print(unix_to_date(int(input("请输入unix时间戳："))))

"""
关于字符串的一些知识：
1.字符串是不可变类型，所以字符串的任何操作所有针对字符串的操作（如拼接、替换、切片等）都不会改变原字符串，而是返回一个新的字符串
“不可变” 意味着字符串一旦创建，其内容、长度就无法修改。任何看似 “修改” 字符串的操作，本质都是基于原字符串生成了一个新的字符串，原字符串始终保持不变。
如果看到类似 s += "abc" 的代码，表面上像 “在原字符串后追加”，但本质仍是生成新字符串并重新赋值给变量 s，原字符串（修改前的 s）依然存在且未变，只是变量 s 指向了新的字符串对象。例如：
# 1. 字符串拼接（+）
s = "hello"
new_s = s + " world"  # 生成新字符串，原字符串 s 不变
print(s)        # 输出："hello"（原字符串未变）
print(new_s)    # 输出："hello world"（新字符串）

# 2. 字符串替换（replace()）
s = "apple"
new_s = s.replace("a", "A")  # 生成新字符串，原字符串 s 不变
print(s)        # 输出："apple"（原字符串未变）
print(new_s)    # 输出："Apple"（新字符串）

# 3. 字符串切片（[:]）
s = "python"
new_s = s[1:4]  # 截取第2-4个字符，生成新字符串
print(s)        # 输出："python"（原字符串未变）
print(new_s)    # 输出："yth"（新字符串）

# 4. 字符串大小写转换（upper()/lower()）
s = "Hello"
new_s = s.upper()  # 生成全大写新字符串
print(s)        # 输出："Hello"（原字符串未变）
print(new_s)    # 输出："HELLO"（新字符串）
s = "a"
print(id(s))  # 输出原字符串的内存地址（假设为 140708345678928）

s += "b"      # 生成新字符串 "ab"，变量 s 指向新地址
print(id(s))  # 输出新字符串的内存地址（假设为 140708345679088，与原地址不同）

"""
