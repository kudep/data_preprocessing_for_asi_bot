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
## Parsing and pretreatment subtitles

Parsing is performed by the pysrt module.
```
pip install pysrt
```

Addition information about encoding is shown [here](http://mindspill.net/computing/linux-notes/determine-and-change-file-character-encoding/).
For example:
```
file -bi test.txt
```
Addition information about chardet is shown [here](https://chardet.readthedocs.io/en/latest/usage.html#example-using-the-detect-function). Installation:

```
pip install chardet
```

Start parsing and pretreatment subtitles:

```
python youtube_subs_parser.py $SRCDIR $TGTDIR
```
