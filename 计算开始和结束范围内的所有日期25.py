"""
题目描述：计算开始和结束范围内的所有日期,闭区间
编写者：gfsq
日期：2025-10-12
"""
import datetime


def get_date_range(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    """
    占位符第一个必须是%Y（大写）
    """
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    date_list = []
    while start_date <= end_date:
        date_list.append(start_date.strftime("%Y-%m-%d"))
        date_gap = datetime.timedelta(days=1)
        start_date = start_date + date_gap
    return date_list


print(get_date_range(input("请输入起始日期,格式为年-月-日"), input("请输入结束日期,格式为年-月-日")))

"""
datetime对象也可以直接比较大小
"""

"""
datetime.datetime.strptime(str,format)
是 Python 中用于将字符串转换为 datetime.datetime 类型对象的核心方法（作用是 “解析字符串为日期时间”），与 strftime()（将日期时间对象格式化为字符串）互为逆操作
format：字符串对应的格式模板，用于指定 date_string 中各个部分（年、月、日、时、分、秒等）的位置和格式（必须与 date_string 的结构完全匹配）。

"""
