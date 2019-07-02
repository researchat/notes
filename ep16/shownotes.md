---
actor_ids:
  - tadasu
  - soh
  - coela
audio_file_path: /audio/16.mp3
audio_file_size: 82865670
date: 2019-07-02 09:00:00 +0900
description: これまでのイメージング技術とは一線を画するアイディアと実装により、分子間の近接性だけの情報から分子や細胞の位置を再構成するというDNA microscopy法について、原著論文とその周辺技術について詳しく話しました。(出演：tadasu、soh、coela）
duration: "01:26:19"
layout: article
title: 16. Beyond imaging
---

## Title
- DNA Microscopy(仮)
- Beyond imaging

## Show notes
- [DNA Microscopy: Optics-free Spatio-genetic Imaging by a Stand-Alone Chemical Reaction](https://www.biorxiv.org/content/10.1101/471219v1)...bioRixv (Open Acess) 論文のPDFが入手できます。
- [DNA Microscopy論文のFigure 1](https://www.biorxiv.org/content/biorxiv/early/2018/11/19/471219/F1.large.jpg)...PodcastではほぼFigure1の説明に終始しているので、これを見ながら...だと理解の助けになるのかもしれない...
- [DNA Microscopy: Optics-free Spatio-genetic Imaging by a Stand-Alone Chemical Reaction](https://www.sciencedirect.com/science/article/pii/S0092867419305471)...Cell Press.
- [Joshua Weinsteinのセミナー動画 (YouTube)](https://www.youtube.com/watch?v=hrqU2RP_9rc)...1st author Joshua Weinsteinが論文には書かれていない背景なども含めてDNA microscopyについてBroad研で発表した動画。
- In-gel PCR...Four-arm PEG acrylateとHS-PEG-SHというポリエチレングリコール (PEG)をPCR反応液に追加することにより、高温下でも分子の拡散を抑えることができる。この液体の中で、Overlap extension PCRが起き、近接する2つのUMIを持つ分子同士はUEIを受け取りつつ連結される。
- [Virtual microfluidics for digital quantification and single-cell sequencing. Nature Methods 2016](https://www.nature.com/articles/nmeth.3955)...In-gel PCRの元論文。
- In situ cDNA synthesis...固定した細胞に対しても逆転写酵素とプライマーなどを用いてcDNA合成を行うことができる。これを利用することで、細胞内でRNA分子の配列をその場でシーケンシングすることがIn situ RNA sequencing (FISSEQ法)で可能になった。
- [Fluorescent In Situ Sequencing (FISSEQ)](https://wyss.harvard.edu/technology/fluorescent-in-situ-sequencing-fisseq/)
- Illumina sequencing...位置塩基ごとに蛍光標識されたdyeを用いた伸長反応により大量のDNA配列を決定する。[こちらのYoutubeの動画](https://www.youtube.com/watch?v=fCd6B5HRaZ8)が原理を知るにはわかりやすい。
- [Locally rigid embedding](https://www.pnas.org/content/105/28/9507)


- 距離関数
- ガウシアン
- contact probability
- Hi-C
- 蛍光顕微鏡の解像度
- フォトンの数
- 解像度の限界
- 超解像
- TCR recombination
- GAPDH, ACTN
- smFISH
- MS2 live cell imaging
- Github
- Clality


## Editorial notes
- Cell誌のTheoryセクションということもあり、日本ではほとんど報道もなく紹介記事も見当たらない中、このDNA microscopyという画期的なコンセプトが伝わればいいと思いますが果たして...(soh)
- (coela)
- トリッキーな内容と論文の文体から、とてもスマートに感じるDNA microscopyであるが、内容を理解していくにつれて、案外膨大な試行の先にたどり着いた泥臭い方法論なのではないかと思うようになった。枯れたテクノロジーをできるだけ使いたい保守派研究者としては、DNA microscopyに対して思うことはたくさんある。しかし、そのモヤモヤは一度横に置き、自分の研究にどのように応用できるか、そしてこれからのどのように発展するか、その行き先を見つめていきたい。(tadasu)
