#!/usr/bin/env python
# coding: utf-8

# In[19]:


# -*- coding:utf-8 -*-

#导入所需要用到的模块
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image

#此处文件路径我用的是绝对路径来获取背景图片及测试文本文件
img = np.array(Image.open(r'D:\code\NLP\John.jpg'))
text_from_file = open(r'D:\code\NLP\johns.txt').read()

#通过jieba分词进行分词并通过空格分割
Word_spilt_jieba = jieba.cut(text_from_file,cut_all = True)
word_space = ' '.join(Word_spilt_jieba)

#配置Wordcloud参数
my_wordcloud = WordCloud(
    background_color='black', #设置背景颜色
    mask=img,  #背景图片
    max_words = 200, #设置最大显示的词数
    stopwords = STOPWORDS, #设置停用词
    #设置字体格式，字体格式 .ttf文件需自己网上下载，最好将名字改为英文，中文名路径加载会出现问题。
    font_path = r'D:/code/NLP/font_free.ttf', 
    max_font_size = 100, #设置字体最大值
    random_state=100, #设置随机生成状态，即多少种配色方案
    ).generate(word_space)

#根据图片生成词云颜色
iamge_colors = ImageColorGenerator(img)
my_wordcloud.recolor(color_func = iamge_colors)

#显示生成的词云图片
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()

#保存生成的图片，当关闭图片时才会生效，中断程序不会保存
my_wordcloud.to_file('dream.jpg')

