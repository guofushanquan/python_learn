"""
题目描述:将字符串日期转换为易读的格式
编写者:gfsq
时间:2025-10-16
"""
import datetime
import time
from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print(dt)
"""
dateutil 是 Python 的一个第三方库（非标准库），提供了比内置 datetime 模块更强大的日期时间处理功能，尤其是自动解析非标准格式的日期时间字符串的能力。
"""
local_time=datetime.datetime.now()
print(local_time)
print(parser.parse(time.ctime()))

"""
parser.parse()的作用就是将日期的非标准字符串转为标准的字符串，年-月-日 时：分：秒
"""

print(parser.parse("2015-08-28 00:00"))  # 标准格式 → 2015-08-28 00:00:00
print(parser.parse("August 28, 2015 12:00 AM"))  # 全称月份+逗号 → 2015-08-28 00:00:00
print(parser.parse("8/28/2015 12:00"))  # 斜杠分隔 → 2015-08-28 12:00:00（默认月/日/年）
print(parser.parse("28-08-2015"))  # 横线分隔 → 2015-08-28 00:00:00（日-月-年）