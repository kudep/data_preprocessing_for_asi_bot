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
