"""
题目描述：Python计算周同比
编写者：gfsq
日期：2025-10-12
"""
import datetime


# 得到日期和价格的字典
def get_date_money(file_name):
    date_money_dic = {}
    with open(file_name, "r", encoding="utf-8") as f:
        is_first_line = True
        for line in f:
            if is_first_line:
                is_first_line = False
                continue
            if line[-1] == "\n":
                line = line[:-1]
            date, money = line.split()
            if date not in date_money_dic:
                date_money_dic[date] = float(money)
    return date_money_dic


def get_weekly_same(date_money_dic):
    date_huanbi = {}
    for date in date_money_dic:
        current_money = date_money_dic.get(date, 0)
        # 得到七天前的日期
        time_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        time_gap = datetime.timedelta(days=7)
        past_time_date = time_date - time_gap
        past_time = past_time_date.strftime("%Y-%m-%d")  # 改成无前置0的格式，为了匹配字典的格式
        past_money = date_money_dic.get(past_time, 0)
        if (current_money == 0 or past_money == 0):
            print("日期数据不存在，请确认数据后重新输入")
            huan_bi = "NONE"
        else:
            huan_bi = (current_money - past_money) / past_money
        date_huanbi[date] = str(huan_bi)
    return date_huanbi


def write_huanbi(read_file_name, date_huanbi_dic, write_file_name):
    # 目的读取read_file_name中的内容，并将date_huanbi_dic中的环比，添加write_file_name中
    all_line_list = []
    with open(read_file_name, "r", encoding="utf-8") as f:
        is_first_line = True
        for line in f:
            if line[-1] == "\n":
                line = line[:-1]
            if is_first_line:
                is_first_line = False
                line_list = line.split()
                line_list.append("周比")
                all_line_list.append(line_list)
                continue
            line_list = line.split()
            line_list.append(date_huanbi_dic[line_list[0]])
            all_line_list.append(line_list)
    # 接下来把all_line_list中的内容写入到write_file_name中
    with open(write_file_name, "w", encoding="utf-8") as fout:
        for line_list in all_line_list:
            fout.write(" ".join(line_list) + "\n")


"""
dict.get() 是 Python 字典的内置方法，用于安全获取指定键的值，核心优势是 “键不存在时不会抛出 KeyError，而是返回默认值”。以下是详细用法：
一、基本语法
dict.get(key, default=None)
"""

date_money_dic = get_date_money("date_sale_data.txt")
# print(date_money_dic)
# # print(get_weekly_same("2021-04-30",date_money_dic))
# print(get_weekly_same(date_money_dic))#得到的是一个日期与环比的字典

write_huanbi("date_sale_data.txt", get_weekly_same(date_money_dic), "data_sale_huanbi_data.txt")
