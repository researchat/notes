import csv
tsvFile = open("../reference/manga_annotataed_db.tsv")
tsv = csv.reader(tsvFile, delimiter = '\t')
for i, s in enumerate(tsv):
    eplink = []
    for t in s[-1].split(','):
        eplink.append("[{}](https://researchat.fm/episode/{})".format(s[1],s[1]))
    print ("|" + '[{}]({})'.format(s[0],s[2]) + '|' + '<a href="{}" > <img src="{}" height=120 alt="{}"></a>'.format(s[2],s[1],s[0]) + "|" + s[3] + "|" + s[3] + "|" + " ".join(eplink) + "|")
        

