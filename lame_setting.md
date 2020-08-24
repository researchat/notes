GarageBandで作ったWAVをmp3にlameを使ってエンコードする

```sh
lame -b 96 -h --resample 44.1 -q 2 --cbr -m m --noreplaygain ep69.wav 69.mp3
```
