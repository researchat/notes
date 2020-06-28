# Zoom H6+Audio Hijack+Discordで録音環境のセットアップ
## 問題
ローカルとリモートにそれぞれ複数のゲストがいる、というポッドキャストの中ではかなりエクストリームな収録環境をどのように実現するか？
インターネットを探すとほとんど記事が無い、というかそういう状況があまりないのかもしれない...

## 目的
Macに接続されたZoom H6でマルチトラックで録音した音声をミックスして、Discordで配信しつつ、ゲストの声はローカルのゲストもモニターできるようにする。
Audio Hijack+SoundFlowerを使うと簡単に実現できそうだ。

## 機材など
- Audio inferface Zoom H6: 6-input (4本のXLR端子、付属するステレオXYマイク)のオーディオインターフェース
- Dynamic mic: SHURE SM58 (何でもよい)
- Audio Hijack: Macに入力される音声を自由かつ直感的にルーティングすることができる
- SoundFlower: Macに仮想オーディオを作成することができるプラグインをインストールしておく
- Discord: ボイスチャット

## Zoom H6の設定
Multi Track ModeでUSB経由でMacに接続する。48kHz 16bitで出力するように設定。
Low cut (80 kHz以下をカット)とcompressorは内蔵のものを使う。

## Discordの設定
Setting -> Voice&Audio -> Soundflower (2ch)に設定する
これによって、仮想オーディオインターフェースに集めた音声（Zoom H6）を入力にすることができる

## Macの設定を確認
Audio MIDI Setup.appで以下を設定する
Macに接続したZoomのサンプリングレートと入力ボリューム: Zoom H6とSoundFlower (2ch)をそれぞれ48kHzになっていることを確認。

<img width="500" alt="Screen Shot 2020-06-28 at 17 59 26" src="https://user-images.githubusercontent.com/1855860/85943209-83133480-b969-11ea-8e9f-b3854e059cdc.png">
<img width="500" alt="Screen Shot 2020-06-28 at 17 59 36" src="https://user-images.githubusercontent.com/1855860/85943187-59f2a400-b969-11ea-8cf7-cc0910c1a4be.png">



