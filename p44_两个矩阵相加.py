"""
题目描述：使用python实现两个矩阵相加
编写者:gfsq
时间：2025-10-14
"""
matrix1=[[1,2,4],
         [2,4,1.2],
         [3,4,6]]#列表中每个元素需要使用","分割

matrix2=[[1,2,4],
         [2,4,1.2],
         [3,4,6]]

matrix3=[[0,0,0],
         [0,0,0],
         [0,0,0.0]]
#遍历二维列表的每一个元素
for row in range(3):
    for column in range(3):
        matrix3[row][column]= matrix1[row][column]+matrix2[row][column]

for row in range(3):#range后面要用（）,切片操作用[]object[start:end:step]
    print(matrix3[row])