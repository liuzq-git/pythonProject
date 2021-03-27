#获取文件中的每个单词的tfidf值

#1获取文件中内容
import math
from collections import Counter


urls=['english.txt','english2.txt']

news =[]
for itemurl in urls:
    news.append(open(itemurl).read())

#2.分词
word_list = []
for i in range(len(news)):
    word = news[i].split(' ')
    if word!='':
        word_list.append(word)


#3.统计每个文件中的分单词数
words_cnt=[]
for i in range(len(word_list)):
    words_cnt.append(Counter(word_list[i]))


#4统计每个文件的总单词数
filesall_cnt = []
for i in range(len(words_cnt)):
    count = 0
    for value in words_cnt[i].items():
        count += value[1]
    filesall_cnt.append(count)

#获取总文档数
fileslen= len(urls)

#获取每个单词所在文档数
words_arr={}
for i in range(len(words_cnt)):
    for value in words_cnt[i].items():
        if value[0] in words_arr:

            words_arr[value[0]]+=1
        else:
            words_arr[value[0]] = 1


#获取每个单词的tf值
for i in range(len(words_cnt)):
    print("文档%s：" %(urls[i]))
    for value in words_cnt[i].items():

        tf = value[1]/filesall_cnt[i]
        idf = math.log10(fileslen/(words_arr[value[0]]+1))
        print("%s的tf值：%f,idf值：%f,tf-idf值：%f" %(value[0],tf,idf,tf*idf))

