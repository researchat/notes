## 制限酵素の雑なサマリ
- 外来ファージなどがバクテリアに感染したときに、外来の二本鎖DNAをぶちぶちに切断するためのシステム。制限システムと呼ばれたりする。
- 1970年代に最初に制限酵素が発見され、EcoRIと命名された。
- 5’-GAATTC-3’という配列を認識し、切断する。この配列は回文構造になっているぞ。4^6=4,096なので大体、4kbに一回くらい出現する。
- 以後、色々な生物（バクテリアやウィルス）から数百種類の制限酵素がこれまで発見されてきた。
	- きっと今の新しいCas9を見つけよう！という流れと似ているのだろう。
	- ユニークなものを探し求めたようだ。
- CRISPR-Cas9システムになんだかとても似ている。
- 分子生物学ではなくてはならない必須の道具。ハサミ。
- 一般的な分子生物学の実験で使われるのは、Type IIPやType IISと呼ばれるもの。
- 4-6文字くらいを認識して、二本鎖のDNAを平滑に切断したり (SmaIとか)、粘着末端といって、出っ張るように切断するタイプがある（こっちのほうが多い）。
- 切れたDNAは、3'に水酸基、5'にリン酸基がつくので、DNA同士をligaseで再び糊にように貼り付けてつなげることができる。これがクローニングと呼ばれるもの。
- ちなみに、違う制限酵素でも切れ方が同じだとその２つの切れた断片はお互いにくっつけることができる。たとえばNheIとXbaIとかね。マニアック。こういう情報もNEBは公開したりしている。
- なんで自分自身のゲノムを切断しないのか？
	- 基本的には制限酵素と同じオペロンから同じ配列を認識するDNAメチル化酵素が同時に発現している。
	- メチル化されたDNAは同じDNA配列でも切断されないので、これによって保護されている（すごい）共進化しているのかな？
	- 例えばよく使われる大腸菌ではdamメチラーゼやdcmメチラーゼが発現していて、認識配列が微妙にかぶっているので、XbaIやClaIはメチル化の影響を受ける。切りたいのにきれない！てなるので注意が必要ですね。あるある。
- どのように作るのか？
	- 普通にほしい制限酵素を大腸菌などで過剰発現させると大腸菌ゲノムがぼろぼろになってしまう。なので、対応するメチルトランスフェラーゼと一緒に発現させて、ゲノムをメチル化して保護してあげるらしい。プラスミドのコピー数をうまくコントロールして、制限酵素の発現量<<<メチルトランスフェラーゼとなるようにする必要があるようだ。この辺は色々なノウハウがありそう。
	- NEBが世界で初めて発売を始めた。いま300種類くらいある。日本だと東洋紡やTAKARAなどが売っている。
	- http://rebase.neb.com/rebase/rebase.enz.html ここに大量の制限酵素のリストがある。まだ認識配列が未知のやつとかもたくさん載っている。

## NEBカタログ回 (Sohのまとめ)
- [NEB Literature Portal](https://international.neb.com/support/catalog-and-literature-request)...ここからそれぞれのカタログPDFにアクセスできる。
- [Competent Cell](https://international.neb.com/-/media/nebus/files/brochures/compcell_brochure.pdf?rev=55d0a4e400624bc2a3ade6f23d1d8b9d)
  - NEB 5aやTurboなど
  - "Enhancing Transformation Efficiency"が便利。いろいろなテクニックが載っている。PEGやLigaseの持ち込みが阻害することは以外と知られていない...?
- [Golden Gate Assembly](https://international.neb.com/-/media/nebus/files/brochures/golden_gate_assembly_trifold.pdf?rev=a46639d92e6a4953ab28090c57e06400)
  - Type-IIS restriction system BsmB1やBbs1など。認識配列から数塩基離れた配列を切断でき、かつ切断箇所はNなので自由自在にoverhangを設計することができる。
  - たとえばBsaIはNNNN (4N)なので、原理的には512通りのorverhangが作れる。
  - しかしその効率は異なる、ことを知っている人はすくない。ACATよりもTGCCのほうがligationが高効率にされる、などすべての4bp overhangのチャートが載っている！
- [Molecular Cloning Technical Guide](https://international.neb.com/-/media/nebus/files/brochures/cloning_tech_guide.pdf?rev=5e4ee766c39f49e08fe1a378c4cbd2e0)
  - いわゆる制限酵素で切って入れる方法のほかに、Blant-end cloningやGateway cloningなどがチャートで載っている。FAQなども非常に読み応えがある。
  - 286 Restriction enzymes available from NEB, 50 Type-II enzymes, 11 nicking enzymes
- Others: NEB Podcast
- Q: 制限酵素の認識配列って昔の人はどうやって決定していた...?
  - https://www.sbj.or.jp/wp-content/uploads/file/sbj/9403/9403_yomoyama.pdf

