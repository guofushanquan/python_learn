"""
题目描述：某个公司采用公用电话传递数据，数据是四位的整数，
在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
编写人:gfsq
时间:2025-10-15
"""
"""
思路理清
输入一个四位数字
for
注意字符串不能直接赋值
"""
number=input("请输入一个四位数字:")
number_list=[]
for index in range(len(number)):
    num=int(number[index])
    num+=5
    num=num%10
    number_list.append(str(num))
number_list[0],number_list[3]=number_list[3],number_list[0]
number_list[2],number_list[1]=number_list[1],number_list[2]
print("".join(number_list))

"""
一、正确语法：str.split(sep=None, maxsplit=-1)
参数说明：
sep（可选）：分隔符，默认为 None（表示以任意空白字符，如空格、换行 \n、制表符 \t 等为分隔符，且多个连续空白会被视为一个分隔符）；
maxsplit（可选）：最大分割次数，默认为 -1（表示不限制分割次数，尽可能多分割）。
返回值：一个由分割后的子字符串组成的列表。
"""