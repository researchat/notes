# -*- coding: utf-8 -*-
import csv
tag = "researchatf04-22"
tsvFile = open("../reference/manga_annotataed_db.tsv")
tsv = csv.reader(tsvFile, delimiter = '\t')
print ("|  名前  |  画像 | 既刊数 |  紹介エピソード|")
print ("| ------ | ----- | ---- |  ------------- |")
 
for i, s in enumerate(tsv):
    eplink = []
    for t in s[5].split(','):
        eplink.append("[Episode{}](https://researchat.fm/episode/{})".format(t,t))
        s[2] = s[2] + "?tag=" + tag
    if s[4] == 'yes':
        s[3] = '全'+ s[3] + '巻'
    else :
        s[3] = '既刊'+ s[3] + '巻'

    print ("|" + '[{}]({})'.format(s[0],s[2]) + '|' + '<a href="{}" > <img src="{}" height=120 alt="{}"></a>'.format(s[2],s[1],s[0]) + "|" + s[3] + "|" + ",".join(eplink) + "|")
        

