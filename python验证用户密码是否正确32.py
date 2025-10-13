"""
题目描述：使用python验证用户密码是否正确
编写者：gfsq
日期：2025-10-13
"""
"""
对用户密码的要求：
1、长度在6-10位
2、至少一个大写字母
3、至少一个小写字母
4、至少一个数字
5、至少一个特殊字符
"""
import re
#判断密码是否符合规范，符合返回True，不符合返回False
def password_is_right(pass_word):
    if 6<=len(pass_word)<=15:
        pass
    else:
        print("密码长度在6-15位")
        return False
    #判断是否有大写字母
    if not re.findall(r"[A-Z]",pass_word):
        print("密码最少需要包含一个大写字母")
        return False
    if not re.findall(r"[a-z]",pass_word):
        print("密码最少需要包含一个小写字母")
        return False
    if not re.findall(r"[0-9]",pass_word):
        print("密码最少需要包含一个数字")
        return False
    if not re.findall(r"[^0-9A-Za-z]",pass_word):
        print("密码最少需要包含一个特殊字符")
        return False
    return True
"""
re.findall(pattern,str)
返回一个list
"""


while (not password_is_right(input("创建您的密码："))):
    pass
print("创建密码成功！")
"""
在这个程序中，需要注意算法思维：
 if 6<=len(pass_word)<=15:
        pass
    else:
        print("密码长度在6-15位")
        return False 
这段代码（正确的话无用，错误执行程序），可以写为
if not 条件：

while (not password_is_right(input("创建您的密码："))):
    pass
print("创建密码成功！")

当条件错误时不断执行函数（条件），就把函数作为判断条件，程序执行时会先执行函数再判断。正确时输出,感觉常用在有外部输入时
"""

"""
[]：字符集，匹配括号内的任意单个字符
"""




"""
1. 当 ^ 在字符集 [] 外部时：匹配 “字符串的开头”
这是你提到的常见用法：^ 放在正则表达式的最前面，用于约束 “匹配的内容必须出现在字符串的开头”。
示例：
正则 ^hello 只能匹配以 hello 开头的字符串（如 hello world 中的 hello），无法匹配 xhello 中的 hello（因为不在开头）。
2. 当 ^ 在字符集 [] 内部时：表示 “否定”（排除字符集内的字符）
这是另一种核心用法：^ 放在 [] 内的最开头，用于表示 “匹配不是字符集内的任意字符”（即 “排除这些字符”）。
"""



