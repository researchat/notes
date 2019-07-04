---
actor_ids:
  - tadasu
  - soh
  - coela
audio_file_path: /audio/16.mp3
audio_file_size: 82865670
date: 2019-07-02 09:00:00 +0900
description: DNA microscopy法と呼ばれる、これまでのイメージング技術とは一線を画するアイディアと実装により、分子間の近接性の情報から分子や細胞の位置を再構成する方法について、原著論文とその周辺技術を詳しく話しました。(出演：tadasu、soh、coela）
duration: "01:26:19"
layout: article
title: 16. Beyond imaging
---

## Title
- Beyond imaging(仮)
- DNA Microscopy

## Show notes
- [DNA Microscopy: Optics-free Spatio-genetic Imaging by a Stand-Alone Chemical Reaction](https://www.biorxiv.org/content/10.1101/471219v1)...bioRixv (Open Acess) 論文のPDFが入手できます。
- [DNA Microscopy論文のFigure 1](https://www.biorxiv.org/content/biorxiv/early/2018/11/19/471219/F1.large.jpg)...PodcastではほぼFigure1の説明に終始しているので、これを見ながら...だと理解の助けになるのかもしれない...
- [DNA Microscopy: Optics-free Spatio-genetic Imaging by a Stand-Alone Chemical Reaction](https://www.sciencedirect.com/science/article/pii/S0092867419305471)...Cell Press.
- [Joshua Weinsteinのセミナー動画 (YouTube)](https://www.youtube.com/watch?v=hrqU2RP_9rc)...1st author Joshua Weinsteinが論文には書かれていない背景なども含めてDNA microscopyについてBroad研で発表した動画。
- In-gel PCR...Four-arm PEG acrylateとHS-PEG-SHというポリエチレングリコール (PEG)をPCR反応液に追加することにより、高温下でも分子の拡散を抑えることができる。この液体の中で、Overlap extension PCRが起き、それぞれのUMIは新しいタグを持ちながら増幅され、近接する2つのUMIを持つ分子同士はUEIを受け取りつつ連結される。
- [Overlapping extension PCR](https://en.wikipedia.org/wiki/Overlap_extension_polymerase_chain_reaction)
- [Virtual microfluidics for digital quantification and single-cell sequencing. Nature Methods 2016](https://www.nature.com/articles/nmeth.3955)...In-gel PCRの元論文。
- In situ cDNA synthesis...固定した細胞に対しても逆転写酵素とプライマーなどを用いてcDNA合成を行うことができる。これを利用することで、細胞内でRNA分子の配列をその場でシーケンシングすることがIn situ RNA sequencing (FISSEQ法)で可能になった。
- [Fluorescent In Situ Sequencing (FISSEQ)](https://wyss.harvard.edu/technology/fluorescent-in-situ-sequencing-fisseq/)
- Illumina sequencing...位置塩基ごとに蛍光標識されたdyeを用いた伸長反応により大量のDNA配列を決定する。[こちらのYoutubeの動画](https://www.youtube.com/watch?v=fCd6B5HRaZ8)が原理を知るにはわかりやすい。
- [A Theory of Network Localization](https://ieeexplore.ieee.org/document/1717436)
- [A remark on global positioning from local distances](https://www.pnas.org/content/105/28/9507)... Locally rigid embeddingのオリジナル論文。
- [ブラウン運動](https://ja.wikipedia.org/wiki/%E3%83%96%E3%83%A9%E3%82%A6%E3%83%B3%E9%81%8B%E5%8B%95)...何故、あるUMIを持つDNAが溶液中を移動して、異なるUMIを持つDNAと出会い、Overlap extension PCRを介して、新たなUEIを形成することができるのか。DNA microsocpyで明らかにしようとしている空間サイズでは、PCRに用いられるような高温にしてしまうと、一瞬でDNA群は均一に混じり合ってしまうことが予想されるが、粘度が高いゲル中でPCR反応を行うことにより、DNA分子の拡散を抑えることができる。これにより、UMI diffusion cloudsが形成される。
- [距離空間](https://ja.wikipedia.org/wiki/%E8%B7%9D%E9%9B%A2%E7%A9%BA%E9%96%93)
- [正規分布](https://ja.wikipedia.org/wiki/%E6%AD%A3%E8%A6%8F%E5%88%86%E5%B8%83)
- [Comprehensive mapping of long-range interactions reveals folding principles of the human genome. Lieberman-Aiden et al. Science, 2009](https://www.ncbi.nlm.nih.gov/pubmed/19815776)...Hi-C法のオリジナル論文。この論文を起点として、核内における染色体高次構造、クロマチン構造解析が爆発的に進むようになった。この方法も光学系ではなく、シーケンシングによってクロマチン構造を明らかにしようというコンセプトからなる。DNA配列同士の"Contact Probability"を中心にしている。
- [光学顕微鏡の解像度の限界:回折限界](http://www.microscope.jp/knowledge/01-4.html)...蛍光顕微鏡を用いる際の回折限界は、波長の大きさとレンズの開口数によって計算することができる。
- [超解像顕微鏡法](https://www.sanken.osaka-u.ac.jp/labs/bse/6912kagaku_nagai-1.pdf)...2014年に超解像顕微鏡法がノーベル賞を受賞したときに書かれた阪大永井先生の総説。超解像顕微鏡法とは回折限界以下で行うことができる蛍光イメージングのことを指す。PALM, STORM, STED, SIMなど様々な方法が現在用いられている。
- [ハウスキーピング遺伝子](https://www.yodosha.co.jp/jikkenigaku/keyword/279.html)...どの細胞においても定常的に多量発現している遺伝子のこと。GAPDH（glyceraldehyde-3-phosphate dehydrogenase),β-アクチンなどが含まれる。
- [V(D)J recombination(Wikipedia](https://en.wikipedia.org/wiki/V(D)J_recombination)
- [smFISH](https://bio-protocol.org/e3070)
- [MS2 tagging(Wikipedia)](https://en.wikipedia.org/wiki/MS2_tagging)
- Github
- [CLARITY(Wikipedia)](https://en.wikipedia.org/wiki/CLARITY)


## Editorial notes
- Cell誌のTheoryセクションということもあり、日本ではほとんど報道もなく紹介記事も見当たらない中、このDNA microscopyという画期的なコンセプトが伝わればいいと思いますが果たして...(soh)
- カンゼンニリカイシタ。(coela)
- トリッキーな内容と論文の文体から、とてもスマートに感じるDNA microscopyであるが、内容を理解していくにつれて、案外膨大な試行の先にたどり着いた泥臭い方法論なのではないかと思うようになった。枯れたテクノロジーをできるだけ使いたい保守派研究者としては、DNA microscopyに対して思うことはたくさんある。しかし、そのモヤモヤは一度横に置き、自分の研究にどのように応用できるか、そしてこれからのどのように発展するか、その行き先を見つめていきたい。(tadasu)
