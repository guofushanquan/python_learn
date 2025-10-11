"""
题目描述:输入一个列表，求列表中所有数字的和
编写者：gfsq
时间：2025-10-11
"""
def sum_list(param_list):
    sum=0
    for item in param_list:
        sum+=item
    return sum
if __name__=="__main__":
    param_list=[1,2,3,4,5]
    print(sum_list(param_list))

