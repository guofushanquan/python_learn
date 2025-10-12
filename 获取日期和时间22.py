"""
题目描述：使用python获取当前日期和时间，并格式化输出。
编写者：gfsq
时间：2025年10月12日
"""
import datetime

curr_datetime = datetime.datetime.now()
print(curr_datetime)
"""
datetime为<class 'module'>，是表示模块（Module） 的数据类型，这个先不管（目前还无法理解）
"""
print(curr_datetime.strftime("%Y-%M-%D %H:%M:%S"))
"""
strftime() 函数用于格式化日期，返回一个字符串
"""
print(type(curr_datetime))
"""
为<class 'datetime.datetime'>
一、<class 'datetime.datetime'> 是什么意思？
<class 'datetime.datetime'> 表示一个具体的日期时间对象的类型。
datetime 是 Python 标准库中的一个模块（用于处理日期和时间）；
该模块内部定义了一个同名的 datetime 类（datetime.datetime），这个类专门用于表示 “具体的某一时刻”（包含年、月、日、时、分、秒、微秒等信息）。
当你通过 datetime.datetime(2023, 10, 12, 8, 30) 或 datetime.datetime.now() 创建对象时，得到的就是 datetime.datetime 类型的实例（对象）
"""
# 获取当前日期的年
print(curr_datetime.year)
# 获取当前日期的月
print(curr_datetime.month)
# 获取当前日期的日
print(curr_datetime.day)
# 获取当前日期的星期几
print(curr_datetime.weekday())
"""
0 → 星期一
1 → 星期二
...
4 → 星期五
5 → 星期六
6 → 星期日
"""
# 获取当前日期的小时
print(curr_datetime.hour)
# 获取当前日期的分钟
print(curr_datetime.minute)
# 获取当前日期的秒
print(curr_datetime.second)
