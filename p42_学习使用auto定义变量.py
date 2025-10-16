"""
题目描述:学习使用auto定义变量
编写者:gfsq
时间:2025-10-14
"""
num = 2


def test():
    num = 1
    print(f"函数中的num值为{num}")
    num += 1


"""
函数执行完成后，内存会被销毁
"""
for i in range(3):
    print(f"number is {num}")
    num += 1
    test()
