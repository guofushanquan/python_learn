"""
题目描述：打出杨辉三角
编写人:gfsq
时间：2025-10-14
"""
def get_YH(row_number):
    YH_list=[]
    for line_index in range(row_number):
        line_list=[]
        for column_index in range(line_index+1):
            if column_index==0 or column_index==line_index:
                line_list.append(1)
            else:
                line_list.append(YH_list[line_index-1][column_index]+YH_list[line_index-1][column_index-1])
        YH_list.append(line_list)
    return YH_list

YH_list=get_YH(10)
for line in YH_list:
    print(line)
"""
当一种情况包含在另一种情况的范式中时，可以省略特殊情况，简化代码

"""