---
date: 2019-07-25 09:00:00 +0900
layout: blog
title: 3. Neuralinkのまとめ(2019-07-25)
category: blog
author: tadasu
permalink: /blog/3/
---


## 論文
[An integrated brain-machine interface platform with thousands of channels](https://www.biorxiv.org/content/10.1101/703801v1)
- Musk and Neuralink, bioRxiv 2019 ... 今回のNeuralinkの発表とともに公開。メイン論文。科学研究論文というよりは企業が公開するホワイトペーパーという形態である。

[The “sewing machine” for minimally invasive neural recording](https://www.biorxiv.org/content/10.1101/578542v1)
- Hanson et al. bioRxiv 2019 ... 2019年の3月にUCSFから発表されていた論文。ラストオーサーのPhilip Sabesは現在NeuralinkのSenior Scientist。今回の発表の根幹を担う技術についてかなり詳しく述べられている。発表時にNeuralinkとの関係は示されていない。

## YouTube
[Neuralink Launch Event](https://www.youtube.com/watch?v=r-vbh3t7WVI)
- Elon Mask-> Max Hodak->Matt Mcdougall -> Vanessa Tolosa-> DJ Seo -> Philip Sabes -> 質疑応答

## podcast (ep19)
[Neuron Musk](https://researchat.fm/episode/19)

## もう少し詳しい資料
[Scrapbox(Musk_bioRxiv_2019)](https://scrapbox.io/researchatfm/Musk_bioRxiv_2019)

## Neuralinkとは
 [Neuralink](https://www.neuralink.com/): 2016年7月に創業、最初の大きな報道は2017年4月
 Elon MuskがOwner
- 1.彼らの最終的な目標、到達点、ゴール
  - 人間とAIを融合させる。
- 2. 現時点での目標
  - 長期間、生体適合性がある侵襲性デバイスの開発
  - 広範囲な脳の領域において、同時に数十万の神経細胞ニューロンの活動を読み書きできる。
- 3. 今回達成したこと
  - "侵襲性"BMIを達成するために必要なNeuralinkの基幹技術の開発(1. threads, 2. robots, 3. electronics, 4. algorithm)
  - Ratにおける実験
  - [質疑応答によると猿でも実験はすすんでいるらしい (コンピューター(カーソル?)をBMIを通して動かすことができるサル)](https://www.msn.com/en-us/video/l/elon-musks-neuralink-reveals-monkey-was-able-to-control-computer-with-its-brain/vp-AAEsApu)
 
## これまで
どうやって脳と機械、コンピューターをつなげるのか。
- BMI(Brain Machine interface)とは
  - 脳内における情報の伝達と処理は神経細胞（ニューロン）の働きによる。
  - ニューロンは電気信号を使って情報伝達する。
  - 脳内に電気信号を読み出したり、電気信号を送り込む、書き込むことによって、脳とコンピュータ、機械とのインタフェースをとなる機器の総称がBMIである。
  - BMIは臨床疾患の広い範囲の人々を助けるポテンシャルがある。
  - コンピューターカーソルの神経補綴(ほてつ)制御やロボットの手足、音声合成装置をデモンストレートしてきた。  
- BMIは頭蓋骨の開頭を伴う侵襲式と伴わない非侵襲式に大別される。
  - 非侵襲式BMI
   - 頭皮上に伝わる脳波を゙計測することが可能なEEG(electroencephalogram) ... 数百万のニューロンの情報を頭蓋骨を通して記録することができる
   - 血流量の増減を指標として脳の広い領域の活動パターンを視覚化するfMRI
   - 近赤外光の透過性を使って血中ヘモグロビン濃度から局所脳活動を 安全に、かつコンパクトな装置で測定可能な NIRS (near-infrared optical)
    - 利点と欠点
     - 利点:非侵襲式では脳を損傷する(および感染症、免疫応答の)リスクが少ないこと、人での研究が比較的容易であること 
     - 欠点:EEGに関しては頭蓋骨などの影響で脳波が歪んでしまうため、侵襲式と比較して空間分解能が劣るなどの問題点がある。そして大量のニューロンのシグナルを平均化した情報しか見れない。



