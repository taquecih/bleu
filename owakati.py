#!/usr/bin/env python
# -*- coding: utf8 -*-

# 改行区切りのファイルをお分かちする
import sys
import MeCab

mecab = MeCab.Tagger('-Owakati')
txt = open("owakati.txt", encoding='utf-8').read().splitlines()
l = len(txt)
ow = [0] * l

for i in range(l):
    ow[i] = mecab.parse(txt[i]).strip()
    print(ow[i])

f = open('owakati.txt', 'w', encoding='utf-8')
ow = "\n".join(ow)
f.write(ow)
f.close()