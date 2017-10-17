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

```
export RD="<BASEDIR>"
export TOPIC="<TOPICDIR>"
```
```
export SRCDIR="$RD/rawdata/youtube/$TOPIC"
#export TGTDIR="$RD/preprodata/stage1/youtube/$TOPIC/txt"
export TGTDIR="$RD/preprodata/stage2/youtube/$TOPIC/txt"
mkdir -p $TGTDIR
```
```
python youtube_subs_parser.py $SRCDIR $TGTDIR
```
```
export SRCDIR="$RD/preprodata/stage2/youtube/$TOPIC/txt"
export TGTDIR="$RD/preprodata/stage3/youtube/$TOPIC/txt"
mkdir -p $TGTDIR
```
```
python assembly_dataset.py $SRCDIR $TGTDIR
```

## Wiki

python WikiExtractor.py -o ../extracted/ --processes 60 ../ruwiki-20171001-pages-articles-multistream.xml.bz2

export SRCDIR="$RD/dataset/wiki/extracted"
export TGTDIR="$RD/dataset/wiki/tokenized"
python wiki_handler.py
