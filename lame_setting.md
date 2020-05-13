GarageBandで作ったWAVをmp3にlameを使ってエンコードする。以下の設定で問題なさそうだ。

```sh
lame -b 96 -h 58.wav 58.mp3
LAME 3.100 64bits (http://lame.sf.net)
Resampling:  input 44.1 kHz  output 32 kHz
Using polyphase lowpass filter, transition band: 15097 Hz - 15484 Hz
Encoding /Users/mathilda/Downloads/ep57/ep58_edit - 2020:05:13 8.58.wav
```

- `-h`はhigh quality modeで[0-9]の値、defaultは4、high qualityだと2になる。0が最高品質。
- `-b`でbitrate

