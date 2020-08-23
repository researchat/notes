GarageBandで作ったWAVをmp3にlameを使ってエンコードする。以下の設定で問題なさそうだ。

```sh
lame -b 128 -h --resample 44.1 -q 2 --cbr -m m --noreplaygain ep69.wav 69.mp3
```

- `-h`はhigh quality modeで[0-9]の値、defaultは4、high qualityだと2になる。0が最高品質。
- `-b`でbitrate

