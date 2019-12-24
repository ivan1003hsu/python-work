# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randint
st = '''
我
我的
眼睛
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止
'''
word_list = st.split('\n')
k = 0
ph = input('要有幾段?\n>>')
ph = int(ph)
while k < ph:
    a=''
    i=0
    w = randint(5,7)
    while i != w :
        a = a+ word_list[randint(0,len(word_list))]
        i = i+1
    print((a)+'\n')
    k = k+1
