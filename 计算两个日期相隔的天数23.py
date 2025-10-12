"""
题目描述：计算两个日期相隔的天数
编写者：gfsq
日期：2025年10月12日
"""
import datetime

"""
两个日期的对象可以直接相减
"""


# 下面计算一个人从出生到现在活了多久
def calculate_days(str):
    birth_date = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
    now_date = datetime.datetime.now()
    days = (now_date - birth_date).days
    print(now_date - birth_date)
    # print(type(days)) days的类型是int
    print("你活了%d天" % days)
    return days


calculate_days(input("请输入你的出生日期，格式为年-月-日 时:分:秒："))
"""
datetime.datetime.strptime(str,"%Y-%m-%d")将字符串转换为日期对象
两个日期对象可以直接相减
"""
