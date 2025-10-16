"""
题目描述：求一个字符串的长度
编写者：gfsq
时间:2025-10-15
"""
def get_len(list):
    len=0
    for item in list:
        len+=1
    return len

list="siabuabda,daosjda"
print(get_len(list))