---
date: 2019-12-31 05:25:00 +0900
layout: blog
title: 6. Podcastをライブ配信したときの設定まとめ
category: blog
author: Researchat.fm
permalink: /blog/6/
---

# MacでTwitch + OBS + Discordでライブ配信する方法

[Episode 39. Podcast Year](https://researchat.fm/episode/39)と[40. Empty Dumpty](https://researchat.fm/episode/40)は収録の様子を[TwitchのResearchat.fmチャンネル](https://www.twitch.tv/researchat_fm/)でライブ配信しました。ここではその時の各種設定をメモしておきます。

普段Researchat.fmではDiscordで３人で会話をしつつ、それぞれのマシンで音源をローカルで保存するダブルエンダーと呼ばれる方式で収録を行っています。今回はなるべくその形式を崩さずに、Discord上で行われている会話をTwitchでライブ配信することにしました。

ここではDiscordの音声をライブ配信する方法についてのみ触れるので、ポッドキャストの収録・編集方法について興味がある方は[Rebuild.fmのmiyagawaさんの記事](https://weblog.bulknews.net/podcasting-guide-2017-2e88531a367d)、[白金工業.fmのysdytさんの記事](https://qiita.com/ysdyt/items/9a95857aed85a19766b0)、あと手前味噌ですが[以前我々がまとめたブログ記事](https://researchat.fm/blog/2/)などの情報が参考になると思います。

また今回はライブ配信をTwitchで行いましたが、これはcoelaの趣味によるところが大きいので[Mixlr](http://mixlr.com/)や[twitterのライブ配信機能](https://help.twitter.com/ja/using-twitter/twitter-live)など他の配信プラットフォームを使う選択肢もあると思います。

## 必要なアプリケーション
以下のアプリケーションを入手し、インストールを完了しておいてください。

- [OBS Studio](https://obsproject.com/ja)
- LadioCast (AppStoreで入手）
- [Discord](https://discordapp.com/)
- [Soundflower](https://github.com/mattingalls/Soundflower)


## 各アプリケーションの設定

### Discord
1. Discordの「ユーザー設定」>「音声・ビデオ」。「入力デバイス」を普段使用しているマイクに、「出力デバイス」をSoundFlower(2ch)に設定する。（SoundFlowerのチャンネルはこの後の設定で揃っていれば逆でもOK)

![Discord設定](/images/blog/discord.png)
こんな感じになります！

### LadioCast
1. 「Input1」を普段使用しているマイクに、「Input2」を「SoundFlower(2ch)」に設定。
1. 「MainOutPut1」を「SoundFlower(64ch)」に設定、「AuxOutput1」を自分のイヤホンのデバイスに設定。
1. 「Input1」のMainとAux1のボタンを白選択に、「Input2」のAux1のボタンだけが赤選択になるように設定してください。

![Ladiocast設定](/images/blog/ladiocast.png)

図のような設定になります。図中の「Yeti Stereo Microphone」と表示されている箇所を自分のマイクのデバイスに、「Built-in Output」となっているところを自分のイヤホンのつながっているデバイスに設定してください。

### Twitch
1. もし無ければTwitchのアカウントを作成する。
1. Twitchにログインし、右上のアイコンから「アカウント設定」> 「チャンネルとビデオ」>「プライマリ配信キー」をコピー。※プライマリ配信キーがあれば誰でもそのアカウントで配信できてしまうため絶対人に教えないこと！
1. その他チャンネルの見た目をいじる（ここでは説明を割愛）。

### OBS Studio
実際にTwitchに配信を行うアプリケーションがOBS studioになります。OBSは非常に多彩な機能を持っているのですが、ここではライブ配信に最低限必要な項目についてのみ記載します。

1. 配信中に表示する画像を作成する。実際の収録を行う少し前から、表示しておく画像と配信中に表示する画像の２つを用意しておくと良いかもしれません。今回はKeynoteで以下のような画像を作りました。
![配信用画像](/images/blog/Image.jpeg)
![配信用画像2](/images/blog/Image3.jpeg)
1. 右下の「Controls」>「Stream」を選択。「Service」を「Twitch」に、「Server」を「Auto」に、「Stream Key」にTwitchの設定で取得した「プライマリ配信キー」をペースト※繰り返しになりすがプライマリ配信キーがあれば誰でもそのアカウントで配信できてしまうため絶対人に教えないようにしてください。
1. 左下のSenesから「+」を押して新規シーンを作成する。Podcast配信用の適当な名前をつける。
1. 左下のSourcesから「+」を押して「Audio Input Capture」を選択、Deviceを「SoundFlower(64ch)に設定。
1. 同様にSourcesに「Image」を選択、1.で作成した画像のパスを入力する。
1. よしなに画像のサイズを調節する。

## いざ配信！
1. Discordでちゃんと会話できるか、イヤホンで音が拾えているか確認。その際OBSのAudioCaptureのバーが動いていることを確認する。うまく行かないときはLadiocastを再起動するとうまくいくときがあります。
1. OBS右下のControlsからStart Streamingボタンを押せば配信開始！ 
1. 配信中でもImagesのパスを変更したら表示される画像が動的に変わるため、「XX時から配信します」のような画像を用意している場合、時間がきたらImageのパスを変更して収録しましょう！
1. Stop Streamingボタンで配信終了。

## 最後に

色々いじりながら設定した内容のメモなので、もし「こうすればもっと簡単にできるよ！」などの情報がありましたら是非教えて下さい！

Twitchで配信した内容は設定ページから音源としてダウンロードすることが可能です。Discordのノイズ削除、音量調整の機能が高性能なこともあり、結構良い音質でTwitch上で保存されているため、そのままそれらのファイルを配信に利用するのもアリだと思います。ダブルエンダー形式で収録を行う場合、ローカルでの録音もGarageBandなどで同時に行い、最終的にそちらを編集してPodcastとして配信することになります。

Twitch上の音源は不慮の事故の際のバックアップとしても活用できます。Twitchの設定によってはバックアップが保存されなかったり、一定時間で消去されてしまうのでここらへんは各自ご確認ください。
