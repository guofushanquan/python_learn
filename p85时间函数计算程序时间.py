"""
题目描述：使用时间函数计算程序时间
编写人:gfsq
时间：2025-10-15
"""
import time
start=time.time()
for i in range(3000):
    print(i)
end=time.time()
print(end-start)
"""
time.time() 返回从 “epoch 时间”（1970 年 1 月 1 日 00:00:00 UTC）到当前时刻的总秒数，是一个浮点数。例如：
1728985200.123456 表示距离 epoch 时间过去了 1728985200 秒，加上 0.123456 秒（即 123.456 毫秒）。
"""