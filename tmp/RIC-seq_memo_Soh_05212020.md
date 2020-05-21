06212020 Memo
Soh

https://doi.org/10.1038/s41586-020-2249-1

### RIC-seq (RNA in situ conformation sequencing), Cai et al 2020 Nature.
- 細胞内におけるRNAとRNAの物理的な位置―どのRNAとRNAが細胞内で近接するのか?―について、一斉にその近接情報をDNAシーケンシングによって取得するという技術。

**How RIC-seq works**
- 基本的にはRNA版のHiCだと思ってよい。固定した細胞にたいしてin situで近接するRNA同士を連結させてそれをシーケンシングすることで、3D空間におけるRNAのcontact mapが二次元に圧縮？されて得られるというもの。おそらく、RNA結合蛋白を介したRNAの相互作用を想定していて、これがHiCにおけるクロマチンのようなアナロジーなのだろう。
- 細胞を固定したあと、NMaseでfreeなRNAを分解して、RBPに保護されたRNAだけが細胞中に残るようにして、さらにリン酸化されたビオチン化シチジンを3’末端につけて、二つのRNA同士をRNA ligationで結合させる。
- これによって、キメラになったRNA分子は必ずその結合点がCになる。RNA_A―C―RNA_Bみたいな感じ。
- ビオチン化されたキメラRNAをその後、pull downして、cDNA変換したあとに超並列シーケンサーでキメラのリードを大量に得る。おおよそ100ntくらいのキメラのRNAが取れる。

### RIC-seq faithfully captures RNA secondary structures and tertiary interactions

Fig 1a: 
コンセプトの説明。

Fig 1b: キメラの結合点の塩基組成を見ると80%以上がCに変換されていることが分かる。ランダムだと25%くらいが期待値。

Fig 1c: pre-miRNAのstem loop構造が反映されたリードが取れていた。loopが削れたキメラが得られる。

Fig 1d: HeLaに発現する280種類のpre-miRNAのプロファイルを見ると、Cの分布がstem loopにつよくエンリッチしていることが分かる。このことから、pre-miRNAの特徴的な構造をRIC-seqが捉えたことを示した。

Fig 1e: TERCというRNAについて見てみた。
Pseudoknotなど複雑な二次構造をとるようなRNAについても、その部分構造を反映するようなキメラリードが得られていた。

Fig 1f: Non-coding RNAの一種であるMALAT1がsplicingされるときのU1 binding sitesが同定できた。
HEKでやったPARIS (別のin vivo二次構造解析手法)とも結構一致する。

Fig 1g: この結果はqPCRによるone-by-oneなvalidation assayでも確かめられた。

Fig 1h: RIC-seqから得られたシグナル (contact map)は、タンパクやRNAの立体構造を解析する技術であるCryo-EMによる結果と一致するのか？を定量的に28S rRNAについて調べた。クライオで解けた構造、とくに20Å以下のRNAの相互作用をRIC-seqは捉えている―200bpくらいに相当するようだ―ということが分かった。この中には、kissing loopや長い相互作用などがちゃんと含まれていた。
Q: RIC-seqだけで、de novoに大量に3Dモデリングぽいことができるんだろうか？

Fig 1i: RIC-seqの精度について、既知構造28S rRNAについて、おおよそAUC=0.89くらいで当たられることが分かった。

### Global view of protein-mediated RNA–RNA interactions
Fig 2a: 全染色体上にmapされたRIP-seqリードから再構成されたglobal interaction mapの全体像。
NEAT1とMALAT1の二つのRNAについて、遠位の相互作用が観察された。

Fig 2c: RNA FISHでvalidationしたらNEAT1とMALAT1は近くにいた。

Fig 2d: トポロジカルドメインも見えた。

Fig 2e: MALAT1などは発現する他のRNAと沢山相互作用しているぽい。

Fig 2f: 全体でみるとこのNEAT1やMALAT1はtop5に入るくらい大量に相互作用するパートナーを持っている。
これがRNA hubとなっている。

Fig 2g: 同定されたRNA hubのうち、10%くらいがsuper enhancer (定義なんだっけ…)と一致するようだ。

### Memo
- HiCから得られるデータからは3次元的な染色体の構造を再構成することができるようだ。おおよそ以下のような方法でやるっぽい。
   - まずHiCから得られるchimeric readsからcontact mapを作る。contact mapは、距離が近いAとBほど頻度 (リード数)が高い。
   - ここから、距離行列へと変換 (ナイーブには頻度の逆数が距離になると仮定できるから)する。
   - そのあと、この距離行列を多次元尺度構成法 (Multi-dimensional scaling, MDS)によって、空間構造への推定を行う。
   - これによって３次元空間における互いのDNA断片の距離が分かるというもの。








