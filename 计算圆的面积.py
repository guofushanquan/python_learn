"""
题目：编写一个程序，输入圆的半径，计算并输出圆的面积
编写人：gfsq
编写时间：2025/10/10
"""
import math
#使用math库进行代码编写
print(math.pi)
def circle_area(raidus):
    return round(math.pi*raidus*raidus,2)#round函数可以保留小数点后两位

if __name__=="__main__":
    radius=float(input("请输入圆的半径："))
    print(f"半径为{radius}的圆的面积为{circle_area(radius)}")