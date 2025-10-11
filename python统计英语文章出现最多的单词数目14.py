"""
题目描述：使用PYTHON统计英语文章中出现最多的单词数目
编写者：gfsq
日期：2025-10-11
"""


def word_count(file_name):
    all_words = {}
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            if line[-1] == "\n":
                line = line[:-1]  # 出去最后的换行符
            words = line.split()  # 把单词都存在一个列表中
            for word in words:
                if word not in all_words:  # 字典无序，但是也是可迭代，遍历的是字典的key值
                    all_words[word] = 0
                all_words[word] += 1
    return all_words


all_words = word_count("englishtex.txt")
print(all_words)
# most_word=max(all_words)#会比较key值，所以这种方法不行
# print(f"出现最多的单词是{most_word}，出现了{all_words[most_word]}次")
most_word = max(all_words, key=lambda x: all_words[x])
print(f"出现最多的单词是{most_word}，出现了{all_words[most_word]}次")
