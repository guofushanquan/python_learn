"""
题目描述:海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，
拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，
拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
编写人:gfsq
时间:2025-10-15
"""
"""
思路理清:
使用遍历的方法：
用一个永远正确的循环
peach_number从10开始
就是要找到(每次减1后%5==0 and 每次/5！=0)连续5次的数
while(1):
检查一下每一个number是不是想要的值：
怎么检查:
count=0
while(check_number(copy)):
    number=change(number)
    count+=1
if c
    

   
"""
def change(number):
    number-=1
    number=number*4/5
    return number

def check_number(number):
    number-=1
    if number%5==0 and number/5!=0:
        return True
    else:
        return False
number=10
while(1):
    count = 0
    copy=number
    while (check_number(copy)):
        copy = change(copy)
        count += 1
    if count>=5:
        break
    number+=1

print(f"桃子最少有{number}个")


