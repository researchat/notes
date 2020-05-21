```
SHERLOCK
Nucleic acid detection with CRISPR-Cas13a/C2c2
Science 2017
```

Cas13を用いた核酸の検出技術

- (1) Cas13の持つ核酸への特異的な結合
- (2) Isothermal amplification
- この大きく２つの性質を組み合わせて、CRISPR Casタンパク質による核酸の認識機構を初めて、Zikaやデングvirusの検出といった診断のアプリケーションをつくった。
感度はアトモルレベル。10^－18

そもそも核酸の検出は大きなニーズがあり、
感度、特異度、簡便性、コスト、スピードの観点からこれまでの技術はさまざまなトレードオフが存在した。
これを一気に解決したい。

Cas13はRNAに結合し、活性化されるとnon-targetedにRNAを分解するという特殊な活性を持っている。
したがって、あるRNAがサンプル中に存在するときに、無差別にサンプル中に存在するRNAを分解する (RNase activity in HEPN domain)
collateral activity (コラテラルRNA分解活性)

(a) dsDNAの場合 -> recombinase polymerase amplification (RPA)で増幅
(b) RNAの場合 -> RT-RPAで増幅
-> そのあと、T7 transcriptionで検出用にRNAを大量に増幅させる
そこへクエンチされているRNA probe、gRNA、Cas13aを入れる。この段階では蛍光シグナルは検出されない。
ところが、
標的のRNA probeとgRNAがマッチした場合、Cas13aは標的のRNA probeを分解する。
これにより蛍光を発して、検出することができる。

SHERLOCK for corona virus
https://www.broadinstitute.org/files/publications/special/COVID-19%20detection%20(updated).pdf

```
Multiplexed and portable nucleic acid detection platform with Cas13, Cas12a
Science 2018
SHERLOCK v2
```

- (1) 4チャンネルによるmultiplexing
- (2) 2 アトモル以下でも定量的に検出できるように
- (3) 3.5-fold感度が上がった
- (4) lateral flow readout (paper based diagnosis)

ことなるオーソログを使うと、2塩基のRNAに対して、4つのオーソログは異なるコラテラルRNA分解活性を示した。
例えば、LwaCas13はAUを切断するし、LbaCas13bはGAで、非常に直交性がたかく、互いに排他的であることを発見した。
-> つまりこれを利用すれば、RNA probeに異なる蛍光標識をつけ、同時に異なる標的をそれぞれ検出できるはず
4色でやってみるとうまく検出できた。

lareral flow detectionへ。
Cas13を染み込ませた紙を用意し、これに増幅させたサンプルを乗せて反応させることにより、
コントロールのバンド (anti-biotin antibody)とそれに対応するサンプルのバンド (anti-FAM antibody)を目視によって確認することができるようになった

