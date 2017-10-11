# data_preprocessing_for_asi_bot
Data preparation tools for asi bot

## Retrieve youtube subtitles

Download youtube-dl

```
pip install youtube-dl
```

youtube-dl command is listed below. For example we may download only Russian non-automatic subtitles.

```
youtube-dl --write-sub  --sub-lang ru --skip-download https://www.youtube.com/<same_target>

```

```
pip install pysrt
```


chech enc
http://mindspill.net/computing/linux-notes/determine-and-change-file-character-encoding/
```
file -bi test.txt
```


for check encodding
https://chardet.readthedocs.io/en/latest/usage.html#example-using-the-detect-function
```
pip install chardet
```



```
python youtube_subs_parser.py $SRCDIR $TGTDIR
```
