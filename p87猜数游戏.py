"""
题目描述:猜数游戏
编写者:gfsq
时间:2025-10-16
"""
import random
import time
num=random.randint(1,100)
guess=0
start=time.time()
while(guess!=num):
    guess=int(input("guess："))
    if guess<num:
        print("小了")
    if guess==num:
        print("猜对了")
    if guess>num:
        print("大了")
end=time.time()
print(f"你用了{end-start}秒")
"""
num = random.randint(a, b)  # 生成[a, b]范围内的随机整数
"""
