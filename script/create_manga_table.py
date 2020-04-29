# -*- coding: utf-8 -*-
import csv
tsvFile = open("../reference/manga_annotataed_db.tsv")
tsv = csv.reader(tsvFile, delimiter = '\t')
print ("|  名前  |  画像 | 既刊 | 完結済み | 紹介エピソード|")
print ("| ------ | ----- | ---- | -------- | ------------- |")
 
for i, s in enumerate(tsv):
    eplink = []
    for t in s[5].split(','):
        eplink.append("[{}](https://researchat.fm/episode/{})".format(t,t))
    print ("|" + '[{}]({})'.format(s[0],s[2]) + '|' + '<a href="{}" > <img src="{}" height=120 alt="{}"></a>'.format(s[2],s[1],s[0]) + "|" + s[3] + "|" + s[4] + "|" + " ".join(eplink) + "|")
        

