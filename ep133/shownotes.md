---
actor_ids:
  - maz
  - tadasu
audio_file_path: https://traffic.libsyn.com/secure/researchat/133.mp3
audio_file_size: 99168344
date: 2022-03-28 20:35:00 +0900
rec_date: 2022-02-19 08:00:00 -0500
edit_by: tadasu
description: mazさんをゲストに迎え、自身の研究の変遷を軸に、バイオメカニクスのおもしろさを話していただきました。
duration: "02:36:39"
layout: article
tags:
  - 研究
  - ゲスト
title: 133. The longest self-introduciton

---
## Show notes
- [maz](https://twitter.com/dynamicsoar)
- [maz式ツイートの例](https://twitter.com/dynamicsoar/status/1368332326858526727)
- [Kagayaさん](https://twitter.com/katzkagaya) … リザバーコンピューティングについてお聞きしたい。maz & kagaya回お待ちしております。
- biomimetics/bio-inspired design: このあたりについて全く話せなかったが、生物は人の目から見て有用な特定の指標に特化しているとは限らない（一般にはしていない）ので、模倣する（バイオミメティクス）よりもそこから何らかの設計指針や着想を得るのに使う（生物規範工学・設計）方が良いだろうというのが大まかな流れとしてある、と思う。
- [Soft Robotics](https://en.wikipedia.org/wiki/Soft_robotics)
- [Wyss Institute](https://wyss.harvard.edu/)
- Intelligence requires a body
- [ゆるふわ生物学さんのシャコパンチ回](https://www.youtube.com/watch?v=u6gDoawF8pc)
- ショウジョウバエのホバリング： 高速度カメラによる運動計測 [Fry et al., 2003](https://doi.org/10.1126/science.1081944); それを基にした数値流体力学シミュレーション (computational fluid dynamics, CFD) の論文 [Aono et al., 2008](https://doi.org/10.1242/jeb.008649), および[動画](https://youtu.be/d2gleoY9_2I).
- ハイスピードカメラ（高速度カメラ）とフィルム
- 分解能と解像度： mazの私見だが「解像度 ([image resolution](https://en.wikipedia.org/wiki/Image_resolution))」は、画像や画面などについて、その実空間での物理的な寸法とは無関係に縦と横の画素数だけを指す場合と、寸法を考慮しての画素密度 (dpi, ppi) の意味との両方で使われることがあるように思う。密度や「2点を区別できる最小の距離」という方について議論したいことを明確にするためには「空間分解能 ([spatial resolution](https://en.wikipedia.org/wiki/Spatial_resolution))」の方が誤解を避けやすくてよいのではないかと思う。同様に時間方向の刻み幅については「時間分解能 ([temporal resolution](https://en.wikipedia.org/wiki/Temporal_resolution))」がある。
- 29:45あたり、シャッタースピードをなぜ上げたいか（露光時間をなぜ減らしたいか）の説明がないが、物体の運動を撮影するときの「ぶれ（モーションブラー）」を減らしたいから。その直後、絞りと被写界深度の話で「奥行方向に動くようなカメラ」というのは意味不明だが、動くのはもちろんカメラではなく翼。「複数台のカメラで同時に撮影したときに、画像上で翼が奥の方に動いていくように見える配置になってしまうカメラがある」という意味。
- 飛ばした修士の研究（の一部）は、地面や水面の近くを飛行するときに生じる「地面効果 ground effect」という空気力学的現象が研究テーマで、ホバリング中のショウジョウバエについてこれをシミュレートしたら、羽ばたきによる吹き下ろしが地面付近に高圧のエア・クッションをつくり、この上に胴体 (abdomen) が乗る、いわばホバークラフト的なことが起きていた、というもの（[論文](https://doi.org/https://doi.org/10.1299/jbse.8.344)）。
- マルハナバチ： ここで言っている羽ばたき周波数（1秒間の羽ばたき回数）は過大で、実際にはホバリングでは 145-165 Hz程度 (Fig. 7 in [Dudley & Ellington, 1990](https://doi.org/10.1242/jeb.148.1.19))。
- 翼： 読みは「つばさ」または「よく」だが工学的には後者の読みが多い。昆虫の翼は「翅（はね）」と呼ばれる事が多い。鳥の場合、1枚1枚の feather は羽毛（うもう）または羽根（はね）と呼ばれる。
- ライト兄弟が史上初の動力飛行とされる Write Flyer I を飛ばしたのは [キルデビルヒルズ](https://ja.wikipedia.org/wiki/%E3%82%AD%E3%83%AB%E3%83%87%E3%83%93%E3%83%AB%E3%83%92%E3%83%AB%E3%82%BA)（複数形が正しかった）で、[キティホーク](https://ja.wikipedia.org/wiki/%E3%82%AD%E3%83%86%E3%82%A3%E3%83%9B%E3%83%BC%E3%82%AF_(%E3%83%8E%E3%83%BC%E3%82%B9%E3%82%AB%E3%83%AD%E3%83%A9%E3%82%A4%E3%83%8A%E5%B7%9E))はその少し北にある町。
- レイノルズ (Reynolds) の相似則： たとえば [日本語版](https://ja.wikipedia.org/wiki/%E7%9B%B8%E4%BC%BC%E5%89%87) や [英語版ウィキペディア](https://en.wikipedia.org/wiki/Similitude) あるいは [NASAのページ](https://www.grc.nasa.gov/www/k-12/airplane/airsim.html) などを参照。
- 前縁渦 (leading-edge vortex, LEV) の発見:
  - スズメガ（昆虫）： [Ellington et al., 1996](https://doi.org/10.1038/384626a0). 翼の長さが約1 mの拡大模型でホバリング飛行を模擬。このサイズは元にした蛾の約10倍。一方、本物の蛾は1秒間に26回羽ばたく (= 26 Hz) が、この模型は大きくしたぶんだけ 0.3 Hz とゆっくりと動かすことができた。
  - アマツバメ（鳥）： [Videler et al., 2004](https://doi.org/10.1126/science.1104682). 模型（1.5倍に拡大）で滑空を模した風洞実験をし、流れを煙とレーザーシートで可視化 (= particle image velocimetry, PIV)。
  - コウモリ： [Muijres et al., 2008](https://doi.org/10.1126/science.1153019). 生きたコウモリに風洞で飛んでもらい、流れをPIVで可視化。
  - マダラヒタキ（鳥）： [Muijres et al., 2012](https://doi.org/10.1098/rsbl.2012.0130). 生きた鳥に風洞で飛んでもらい、流れをPIVで可視化。
  - 翼果・翅果（植物）： [Lentink et al., 2009.](https://doi.org/10.1126/science.1174196n) [explanation TBD（ちょっとちゃんと読みます）] [動画](https://youtu.be/ce2HUKizMTw) (Wired)
  - 前縁渦じゃないけどタンポポ： [Cummins et al., 2018](https://doi.org/10.1038/s41586-018-0604-2). [動画 (Nature)](https://youtu.be/N2UbaDV9O9Q)
- 「1秒間に200回のミニ竜巻」←誤り。ハエやハチのホバリングでは、打ち下ろしで1回だけでなく打ち上げでも1回発生するため、1秒間には400回ほど生成・消滅を繰り返している。後でハチドリの羽ばたきの話をするときにもこれに言及している。なお全く話せなかったが、前縁渦以外にも空気力（くうきりょく）増大メカニズムはいくつか提唱されている（少し古いがよく参照される総説論文 [Sane et al., 2003](https://doi.org/10.1242/jeb.00663)）。最近、蚊で後縁渦というのも見つかっている（[Bomphrey et al., 2017](https://doi.org/10.1038/nature21727)、[動画 (Nature)](https://youtu.be/JQl4OP2XdYA)、[日本語の解説記事](https://academist-cf.com/journal/?p=4632)）。
- 北米のハチドリ： 東側にいるのは Ruby-Throated hummingbird（ノドアカハチドリ）のようです。マイグレーション (migration) はこの文脈では「渡り」の意味。ノドアカハチドリはフロリダやメキシコへ渡って越冬する模様。
- 多摩動物公園： 昆虫園にかつていたチャムネエメラルドハチドリというハチドリが対象だった。長崎バイオパークにもいたらしい。ワシントン条約の関係で輸入はかなり難しいようだ。
- オオスカシバ： [ウィキペディア](https://ja.wikipedia.org/wiki/%E3%82%AA%E3%82%AA%E3%82%B9%E3%82%AB%E3%82%B7%E3%83%90)
- ハチドリの体重： 一般に最小とされる [マメハチドリ](https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%A1%E3%83%8F%E3%83%81%E3%83%89%E3%83%AA)は 2 g. 最大の[オオハチドリ](https://en.wikipedia.org/wiki/Giant_hummingbird)は 20 g を超えるがこれはかなり「外れ値」なようで、2番目に重い種より2倍ほども重い ([Fernández et al., 2011](https://doi.org/10.1086/660084)). [AVONET](https://doi.org/10.1111/ele.13898)（大元はDunning）によるとこの2番目に重い種というのは [Topaza 属](https://en.wikipedia.org/wiki/Topaz_(hummingbird)) のいずれかで、12 g 程度のようだ。
- 体温を下げる torpor（休眠？）： [英語版ウィキペディア](https://en.wikipedia.org/wiki/Torpor)
- ハチドリの体温を測りまくってる Powers lab： https://dpowerslab.com/ 
- FLIR: https://www.flir.jp/
- 「あんなちっちゃいのに（沢山の種がいる）」←小さい方が種が多いのはおそらく一般的な傾向なので、逆接は意味不明。
- 「キュービックルート2」←意味不明。体重が10倍違うなら体サイズ（1辺の長さ）は cube root 10 で、約 2.15 倍。「キュービックルート10だから約2倍」と言いたかったのかも。
- ハチドリの飛行の論文の例：空気を「ヘリウム・酸素混合ガス」に置き換えて酸素濃度を保ったまま密度だけ低下させた際の羽ばたき運動を計測した [Chai & Dudley, 1996](https://doi.org/10.1038/377722a0); 広い速度域に渡る羽ばたき運動を風洞で計測した [Tobalske et al., 2007](https://doi.org/10.1242/jeb.005686); 空気力学をPIVで調べた [Warrick et al., 2005](https://doi.org/10.1038/nature03647);[Warrick et al., 2009](https://doi.org/10.1098/rspb.2009.1003) など。他にも Hedrick, Lentink, Altshuler といった北米（当時）のラボを中心に沢山出ている。
- [mazのハチドリ運動計測論文のハイライト動画](https://rs.figshare.com/articles/media/Supplementary_video_S5_hummingbird_hovering_video_with_traced_lines_from_Quantifying_the_dynamic_wing_morphing_of_hovering_hummingbird/5406115/1)。および[シミュレーション例の動画](https://youtu.be/vmpDISKBp0k)（動画開始直後、前縁に発達する白い渦が前縁渦）。論文についての説明で「次列風切はハチドリは5枚しかない」と言っているがこれは誤り。本当はこの種では6枚ある。ただし胴体に近い一番内側の羽根 (S6) は非常に見づらく、羽軸のトレースができていない。
- 初列風切・次列風切： [ウィキペディア](https://ja.wikipedia.org/wiki/%E9%A2%A8%E5%88%87%E7%BE%BD)。東先生の本にはそう書いてたかもしれないが、「初列が推力で次列が揚力」なんていう明確な区別があるというのは眉唾、というかそもそも推力というのは揚力を分解して出てくる成分なので…（もちろん東先生はそのことはわかっているが）。
- オナガラケットハチドリ： [ウィキペディア](https://ja.wikipedia.org/wiki/%E3%82%AA%E3%83%8A%E3%82%AC%E3%83%A9%E3%82%B1%E3%83%83%E3%83%88%E3%83%8F%E3%83%81%E3%83%89%E3%83%AA)・[YouTube動画](https://youtu.be/Df8jhng3xgQ)。[ダーウィンが来た！](https://datazoo.jp/tv/%E3%83%80%E3%83%BC%E3%82%A6%E3%82%A3%E3%83%B3%E3%81%8C%E6%9D%A5%E3%81%9F%EF%BC%81%E7%94%9F%E3%81%8D%E3%82%82%E3%81%AE%E6%96%B0%E4%BC%9D%E8%AA%AC/421010)で取り上げられていたようだ。実際にはこれよりも少し前から別のハチドリ映像についての話が何度か来ていた気がする。補足すると、maz には高尚な理由が見えていなかったが、先生は先を見据えてハチドリ型ロボットを開発していたと思われる。この後の2011年に AeroVironment の [Nano Hummingbird](https://en.wikipedia.org/wiki/AeroVironment_Nano_Hummingbird) が発表されていることからも潮流を読めていたことがわかる。
- [硬骨魚綱・ニシオンデンザメ](https://ja.wikipedia.org/wiki/%E3%83%8B%E3%82%B7%E3%82%AA%E3%83%B3%E3%83%87%E3%83%B3%E3%82%B6%E3%83%A1)
- マダラヒタキ： [ウィキペディア](https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%80%E3%83%A9%E3%83%92%E3%82%BF%E3%82%AD)。気候変動（地球温暖化）関係でよく研究されているらしい。
- スウェーデン・ルンド大学のラボ： [Animal Flight Lab](https://portal.research.lu.se/en/organisations/animal-flight-lab). 昆虫・鳥・コウモリの飛行を全部やってる。昆虫と鳥とかはチラホラあるがコウモリも含めた3グループ全部というのは非常にレアと思われる。[風洞の論文](https://doi.org/10.1242/jeb.200.10.1441)があったが、7度ではなく8度傾けられるとのこと。
- 東昭（あずま あきら）： 研究者の名前。日本での生物飛行・遊泳の力学の草分け的存在。日本語の本も多いが内容的には少し古いため、今から読む場合は他の本も読んだほうが良い。
- 木から落ちる蟻： [Yanoviak et al., 2005](https://doi.org/10.1038/nature03254). [Yanoviak による動画](https://canopyants.net/research/gliding-arthropods/ant-videos/)。さらに[イシノミ](https://canopyants.net/research/gliding-arthropods/bristletail-videos/)や[クモ](https://canopyants.net/research/gliding-arthropods/gliding-spider-videos/)もあり。たまにまっすぐ落下してるやつはビー玉かなんかの対照実験です。制御について、頭を振るというのは勘違いだったようで、そもそも逆さまになって腹部 (abdomen) 側へ落ちていくらしい。さらに [Yanoviak et al., 2010](https://doi.org/10.1098/rspb.2010.0170) によると主に後脚で制御してるようです（色々な脚を remove しての比較落下試験をしている）。また、落下角度が水平から45度を境界とする（それより浅いのを gliding, 深いのを parachuting）のは確かに文献にあるようです（初出？は [Oliver, 1951](https://doi.org/https://doi.org/10.1086/281666) らしいが読めなかった）が、そういうことよりも飛行が制御されてるかどうかで分けろや、とかなんか色々あるようです。詳しくは [Moffett, 2000](https://doi.org/10.1646/0006-3606(2000)032[0569:WSUACL]2.0.CO;2) などを参照。この場合 descent としているのは、このへんのゴタゴタを避けたいからんあじゃないかって気もします。滑空関係でもっとガッツリ進化と絡んだ話を読みたい人向けにはたとえば [Dudley et al., 2007](https://doi.org/10.1146/annurev.ecolsys.37.091305.110014) の総説もあります。←書きすぎでは？？
- mealworm: [ゴミムシダマシの幼虫](https://ja.wikipedia.org/wiki/%E3%83%9F%E3%83%BC%E3%83%AB%E3%83%AF%E3%83%BC%E3%83%A0)、らしい。
- マニューバー（機動）： [コウモリの機動の論文](https://doi.org/10.1098/rsif.2018.0441)
- Robert Wood の [Harvard Microrobotics Lab](https://www.micro.seas.harvard.edu/): 超小型羽ばたき飛翔体の RoboBee で有名（[YouTube channel, ナショジオの動画](https://www.youtube.com/user/MicroroboticsLab)）。[Wyss Institute の Associate Faculty](https://wyss.harvard.edu/team/associate-faculty/robert-wood/) となっている。
- [長崎ペンギン水族館](https://penguin-aqua.jp/)： 世界で最多の9種のペンギンを飼育している。
- [ジェンツーペンギン](https://ja.wikipedia.org/wiki/%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%84%E3%83%BC%E3%83%9A%E3%83%B3%E3%82%AE%E3%83%B3)： オレンジのクチバシと、頭の上の白い帯が特徴的。似た種がいないので見分けやすい。
- GoPro: むき出しでもプール程度の水圧には耐えられるが、市販の透明な保護ケースに入れ、さらに各カメラの視野が最適になるような角度のケースを3Dプリントしておき、そこにはめ込んだ。
- ペンギンの羽ばたき周波数： 4 Hz は巡航（採餌）遊泳時としては高すぎ。体サイズによって変わる（大きいほどゆったり）だが、最小の種であるリトルペンギンで3.5 Hz, 最大の種であるエンペラーペンギンで約1.5 Hz ([Sato et al., 2010](https://doi.org/10.1098/rspb.2009.1515)).
- ペンギンの羽ばたき運動論文： [東工大のプレスリリース](https://www.titech.ac.jp/news/2021/062248)がよく書けていて動画も載っている。「なん日かに分けて…4日」は間違い。論文に使ったデータを撮影したのは連続しない2日間で、初めの日に3個体、1年半後の別の日に初回の3個体に含まれていた1個体。
- バイオロギング： 動物に記録計（ロガー）を付けて、位置・速度・深度などの行動情報を記録する研究手法。[日本バイオロギング研究会のページ](http://japan-biologgingsci.org/home/)を参照。狭義のロギングは記録計の回収が必要となる。最近は送信機を付けてのテレメトリも増えている模様。
- 菊地デイル万次郎さん・SHIOMIさん： 仲のいいバイオロギング屋さん。
- レヴィフライト (Lévy flight)： [英語版ウィキペディア](https://en.wikipedia.org/wiki/L%C3%A9vy_flight)。採餌（餌探索）の例でざっくりいうと、一箇所にとどまってその付近で餌を探すモードと、ある程度離れた場所まで割と一直線に動くモードとの組み合わせからなるような行動。レヴィウォークとも。
- 「彼らのフィールドワーク」： 話のつながりがおかしいが、これは理論屋でなくバイオロギング屋さんのこと。
- [三代始祖](https://ja.wikipedia.org/wiki/%E4%B8%89%E5%A4%A7%E5%A7%8B%E7%A5%96)：馬は専門外です。
- [三代始祖について話した回](https://researchat.fm/episode/15)
- Royal Veterinary College (RVC) の [Structure and Motion Laboratory (SML)](https://www.rvc.ac.uk/research/facilities-and-resources/structure-and-motion) という研究所。主に歩行・走行の研究者が多い。飛行のPIは2名しかいないが2人ともトップレベル（仲もいい）。
- [Alan Wilsonの論文例](https://doi.org/10.1038/nature25479)： ライオン・シマウマ・チーター・インパラでした。
- Oxford喋り[要出典] ... Oxford周辺の方々、ご意見お待ちしております。
- Imperial College of London: 自然史博物館 「Natural History Museum (NHM) London](https://www.nhm.ac.uk/) がすぐ隣にある。入場無料だしオススメ。
- mechanosensor: 機械的受容体と言っているが、受容器が正しいのかも。トンボの翅上の機械センサを調べた共著論文 ([Fabian et al., 2022](https://doi.org/10.1016/j.isci.2022.104150))。
- Imperial College London の [Huai-Ti lab](https://htlinlab.com/).
- ハエで有名な [Holger Krapp](https://hkrapp.bg-research.cc.ic.ac.uk/).
- [AutoDesk Fusion 360](https://www.autodesk.com/products/fusion-360/)： 無料なのでよく使われるCAD.
- [Rhinoceros 3D](https://www.rhino3d.com/)：有料だがかなり安い。建築や宝石分野での利用が多いが、自由曲面生成に強いサーフェスモデラー。[Grasshopper](https://www.rhino3d.com/6/new/grasshopper/) というプラグインでできるビジュアルプログラミングがおすすめ。
何度か言及のあった「メッシュを切る」というのは、CADで作った形状モデルを基にして、構造または流体シミュレーションのために表面や構造または流体内部に格子点（およびそれからなるセル）を作ること。
- [メガネウラ](https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%AC%E3%83%8D%E3%82%A6%E3%83%A9) ... 眼鏡ウラではない。メガ-ネウラ
- 翅脈（しみゃく）： 昆虫の翅のうち、膜じゃない骨組みの部分。英語は vein. ウィキペディアの[昆虫の翅の記事](https://ja.wikipedia.org/wiki/%E6%98%86%E8%99%AB%E3%81%AE%E7%BF%85)も参照。
- トンボの [pterostigma（縁紋）](https://en.wikipedia.org/wiki/Pterostigma)： [マスバランス効果を論じた論文は1992でなく1972](https://doi.org/10.1007/BF00693547)でした。
- Pterosaur（翼竜）： 翼竜の研究はしたことがないので話せることはほとんどありませんが、昔バイオメカニクス研究者が古生物学者にボロクソに言われてた話なんかはあります（ボロクソに言われていた論文 [Wilkinson et al., 2005](https://doi.org/10.1098/rspb.2005.3278)）。

## Editorial notes
- 久々に沢山話せて楽しかったです。後半、のどがかれていてちょっと聞きづらいいですね。失礼しました。残りの80%（そんなに無いと思うが）はまたいずれどこかで… (maz)
- 久々に2時間半超えました。やばい量のshownotesも執筆ありがとうございました。皆様にすこしでもバイオメカニクスという分野の面白さが伝わればうれしいです。今回は自己紹介だけで終わってしまったのでまた参戦していただきたいです。mazさんありがとうございました。(tadasu)

