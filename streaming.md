# MacでTwitch + Discordでライブ配信する方法

## 必要なもの
- [OBS Studio](https://obsproject.com/ja)
- LadioCast (AppStoreで入手）
- [Discord](https://discordapp.com/)
- [Soundflower](https://github.com/mattingalls/Soundflower)

## 手順

### Discord
1. Discordの「ユーザー設定」>「音声・ビデオ」。「入力デバイス」を普段使用しているマイクに、「出力デバイス」をSoundFlower(2ch)に設定する。（SoundFlowerのチャンネルはこの後の設定で揃っていれば逆でもOK)

### LadioCast
1. 「Input1」を普段使用しているマイクに、「Input2」を「SoundFlower(2ch)」に設定。「MainOutPut1」を「SoundFlower(64ch)」に設定、「AuxOutput1」を自分のイヤホンのデバイスに設定。

### Twitch
1. もし無ければTwitchのアカウントを作成する。
1. Twitchにログインし、右上のアイコンから「アカウント設定」> 「チャンネルとビデオ」>「プライマリ配信キー」をコピー。※プライマリ配信キーがあれば誰でもそのアカウントで配信できてしまうため絶対人に教えないこと！
1. その他チャンネルの見た目をいじる（ここでは説明を割愛）。

### OBS Studio
1. 配信中に表示する画像を作成する。
1. 右下の「Controls」>「Stream」を選択。「Service」を「Twitch」に、「Server」を「Auto」に、「Stream Key」にTwitchの設定で取得した「プライマリ配信キー」をペースト。
1. 左下のSenesから「+」を押して新規シーンを作成する。適当な名前をつける。
1. 左下のSourcesから「+」を押して「Audio Input Capture」を選択、Deviceを「SoundFlower(64ch)に設定。
1. 同様にSourcesに「Image」を選択、配信中に表示したい画像のパスを選択する。
1. よしなに画像のサイズを調節する。
1. Discordでちゃんと会話できるか確認、その際OBSのAudioCaptureのバーが動いていることを確認する。
1. 右下のControlsからStart Streamingボタンを押せば配信開始！
