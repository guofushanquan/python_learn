"""
题目描述：输入一个数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
编写者：gfsq
时间：2025-10-14
"""
"""
难点：怎么实现输入数组
"""
def get_list(lenth):
    list=[]
    for i in range(lenth):
        list.append(float(input(f"请输入第{i+1}个数")))
    print("输入完毕！")
    return list
def check_para_list(number_list):
    max_number=number_list[0]
    min_number = number_list[0]
    """
    max_number=-999999
    min_number=999999

    """
    max_index=0
    min_index=0
    for index in range(1,len(number_list)):
        if number_list[index]>max_number:
            max_number=number_list[index]
            max_index=index
        if number_list[index]<min_number:
            min_number=number_list[index]
            min_index=index
    return max_index, min_index
def swap(number_list,max_index, min_index):
    number_list[0],number_list[max_index]=number_list[max_index],number_list[0]
    max_index, min_index=check_para_list(number_list)
    number_list[len(number_list)-1], number_list[min_index] = number_list[min_index], number_list[len(number_list)-1]

number_list=get_list(10)
max_index, min_index=check_para_list(number_list)
swap(number_list,max_index, min_index)
print(number_list)
