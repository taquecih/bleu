#!/usr/bin/env python
# -*- coding: utf8 -*-

# for python3
# txt1にreference、txt2にMT outputを入れてcorpus_BLEUを取得
from nltk import word_tokenize
from nltk import bleu_score
from nltk.translate.bleu_score import SmoothingFunction
cc = SmoothingFunction()

txt1 = open("txt1.txt", encoding='utf-8').read().splitlines()
txt2 = open("txt2.txt", encoding='utf-8').read().splitlines()
l = len(txt1)
ref = [0] * l
hyp = [0] * l

for i in range(l):
    ref[i] = word_tokenize(txt1[i])
    hyp[i] = word_tokenize(txt2[i])

#print(ref)
#print(hyp)
print(bleu_score.corpus_bleu(ref, hyp, smoothing_function=cc.method7))

#    b[i] = str(bleu_score.sentence_bleu([ref], hyp, smoothing_function=cc.method7))

#f = open('bleu.txt', 'w')
#b = "\n".join(b)
#f.write(b)
#f.close()
