# ローカルとリモートに複数人のゲストがいる場合のレコーディング
## 問題
ローカルとリモートにそれぞれ複数のゲストがいる、というポッドキャストの中ではかなりエクストリームな収録環境をどのように実現するか？というのがこの記事が扱う主な内容である。リモートゲストが一人で、計2人で録音するというのはダブルエンダー方式で録音すれば、比較的簡単であり、コロナウィルスの影響もあり今日のポッドキャストで多く採用されている方式である。一方、同じ場所に複数人がいて、1人以上のリモートゲストと会話しながら録音する、となるとハードルが一気に上がる。インターネットを探すとほとんど記事が無い、というわけでその知見をまとめておきたい。

## 概要
Macに接続されたZoom H6 (Audio interface)で録音した音声をミックスして、Discordで配信する。同時にゲストの声はローカルのゲストもモニターできるようにする。これをAudio Hijack+SoundFlowerを使うことで実現する。

<img width="500" alt="Screen Shot 2020-07-05 at 18 06 07" src="https://user-images.githubusercontent.com/1855860/86529259-3f30aa00-beea-11ea-8ce3-11b996b4a90b.png">


## 機材など
- Audio inferface Zoom H6: 6-input (4本のXLR端子、付属するステレオXYマイク)のレコーダー兼オーディオインターフェース
- マイク: ダイナミックマイク SHURE SM58を使用しているがXLR入力であれば何でもよい。
- Audio Hijack (https://rogueamoeba.com/audiohijack/): Macに入力される音声を自由かつ直感的にルーティングすることができる (65USDの有料アプリ)。
- SoundFlower (https://github.com/mattingalls/Soundflower/releases): Macに仮想オーディオを作成することができるプラグインをインストールしておく。
- Discord: ボイスチャットとしてリモートゲストとの会話に使用する。

## Zoom H6の設定
- Multi Track ModeでUSB経由でMacに接続する。`48kHz 16bit`で出力するように設定。
- Low cut (80 kHz以下をカット)とcompressorは内蔵のものを使う (Comp2(Vocal)を使用)。

<img width="500" alt="img" src="https://user-images.githubusercontent.com/1855860/85943662-64626d00-b96c-11ea-8e0f-cad8ce3beb44.jpg">

## Discordの設定
- `Setting` -> `Voice&Audio` -> `Soundflower(2ch)`に設定する。
- これによって、仮想オーディオインターフェースにミックスしたZoom H6の出力をDiscordの入力にすることができる

## Macの設定
- Audio MIDI Setup.appで以下を設定する。
- Macに接続したZoom H6のサンプリングレートと入力ボリューム: Zoom H6とSoundFlower (2ch)をそれぞれ48kHzになっていることを確認。

<img width="500" alt="Screen Shot 2020-06-28 at 17 59 26" src="https://user-images.githubusercontent.com/1855860/85943209-83133480-b969-11ea-8e9f-b3854e059cdc.png">
<img width="500" alt="Screen Shot 2020-06-28 at 17 59 36" src="https://user-images.githubusercontent.com/1855860/85943187-59f2a400-b969-11ea-8cf7-cc0910c1a4be.png">

## Audio Hijackの設定
以下のような感じにルーティングする。レコーディングを開始しないとAudio Hijackの中でモニタリングすることができず、とても不便なので、レコーディングブロックをOFFにしてからレコーディングを開始するとファイルへ保存しないでモニタリングすることができる。コンプレッサーやdenoise機能もあるがそれは使わない。編集はのちのポストプロダクションで行うためである。

<img width="800" alt="Screen Shot 2020-06-28 at 18 06 17" src="https://user-images.githubusercontent.com/1855860/85943414-e6519680-b96a-11ea-9db6-8b2b5f21a4a1.png">

以下のような感じで、ルーティングを開始することで音声がルーティングされる。

![hoge](https://user-images.githubusercontent.com/1855860/85944005-bd330500-b96e-11ea-84b7-1b0b1248c0b5.gif)

## モニタリング
- Discordから出力されるリモートゲストの音声を2人以上のローカルのゲストが聞くためには、Macの3.5mmイヤフォン出力をステレオ・ヘッドホンアンプで分岐させればよい （https://www.amazon.co.jp/gp/product/B000KIPT30）
- Behringer HA400 MICROAMPなど。これは6.3mm標準フォンなので3.5mm変換プラグも必要になる。これで最大で4人まで同じDiscordの音声を聞くことができる。

![download](https://user-images.githubusercontent.com/1855860/86528806-82891980-bee6-11ea-9344-bac5e0757824.jpg)


