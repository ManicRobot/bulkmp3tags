# bulkmp3tags
Edit audio tags of many files at once.

## Requirements
Python >= 3.6
Mutagen (install by typing pip install mutagen)
Some audio files

## Usage
Put bulkmp3tags.py in the folder with audio files you want to edit (or alternatively give the path as argument using -wd) and run it. BulkMP3Tags can handle many audio formats, including FLAC, MP3, OGG and many more.
At the beginning, you can make some values constant, which means, that when later editing the audio files, the constant values will be automatically assigned to each file without you needing to retype them again and again. This can be useful for albums, where usually stuff like the date, artist and album name don't change.
