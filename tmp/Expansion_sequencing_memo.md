```
Expansion sequencing memo (Church+Boyden lab)
06182020
Soh
```

- Nanoscaleの細胞の組織学ができるようなイメージング手法はこれまでに報告されていない。とくに超解像イメージングとSeqFISHを組合せたSeqFISH+ (Cai lab)は、高解像なRNAイメージングを可能にしたが、詳細な細胞や組織の構造をタンパク質の発現とともに観察できるものではない、と彼らは主張している。このため、ターゲット分子が予め定義しておく必要のないin situ sequencingが必要である。

- これまでのFISSEQは細胞サンプルではin situシーケンシングでできたが、組織サンプルではデモされていなかった。これは密な組織サンプルでは試薬の浸透が十分におきないためであると考えられた。そこでExpansion microscopyのchemistry (おむつに使われているpolymer, sodium polyacrylateなど)によってRNAやタンパク質同士の物理的な距離をおおよそ4倍くらいまでに線形的に広げて (=decrowd)してやればいいのでは？というシンプルなアイディア。これまでにもBoydenはExpansion microscopyを使ったRNAのイメージングなども確立してきた。これが今回のExSeqになった (ex in situ sequencing)。

- FISSEQは、laserを当ててサイクルごとに取るので退色するなどでリード長が30bpくらいしか取れない。そこで、ExSeq一度、FISSEQ imagingしたあとに、gelを壊してin situで読んだcDNAをもう一度illuminaで読み直して対応づけるということで擬似的ex situ readsを作り、解決した。マウス脳、C. Elegans Drosophila embryo Helaなどで実証した。15-50 umくらいの厚みのあるサンプルでも可能であることを示した。

- ダイセロスの作ったin situ sequencing法のStarmapはmaxで8umだが、ExSeqは50 uｍの厚みのあるサンプルでも可能である。さらにstarmapはresolutionの限界はdiffraction limitedがその限界になるが (超解像を使っていないので)、ExpansionしたExSeqは100nm x 100nm x 300 nmまでいける。またstarmapはantibody stainとの併用はデモされていない。
