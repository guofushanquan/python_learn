"""
题目描述：计算一个日期前任意天的日期
编写者：gfsq
日期：2025-10-12
"""
import datetime


def get_date_before_days(date_str, days):
    # 先把字符串变成datetime对象
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    time_gap = datetime.timedelta(days=days)
    print(f"time_gap为{time_gap},其类型为{type(time_gap)}")
    """
    <class 'datetime.timedelta'>
    """
    result = date - time_gap
    return result.strftime("%Y-%m-%d")

"""
Python 中的 datetime 对象属于不可变类型（类似字符串、整数），其所有方法（包括 strftime()）都不会修改对象自身，
而是返回一个新的结果（这里是格式化后的字符串）。因此，无论调用多少次 strftime()，原对象 result 的日期、时间信息始终保持不变。
"""


"""
注意将字符串转换为时间对象和将时间对象转换为字符串的不一样
字符串转换为时间对象使用datetime.datetime.strptime(str,format)
时间对象转换为字符串使用对象.strftime(format)
"""
print(get_date_before_days(input("请输入日期（格式：2025-10-12）："), int(input("请输入间隔天数："))))
