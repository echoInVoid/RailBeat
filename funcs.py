import json
import os
import logging as log

def readSongsList(path):
    if not os.path.isdir(path):
        log.warning("%s is not a dir.")
        return 0
    songs = os.listdir(path)
    for song in songs:
        if not os.path.isdir(path+'\\'+song):
            songs.remove(song)
    return songs

def readSong(path):
    if os.path.isdir(path):
        if os.path.isfile(path+"\\data.json"):
            with open(path+"\\data.json", 'r') as f:
                song = json.loads(f.read())
            try:
                song["name"]
                song["time"]
                song["createDate"]
                song["author"]
                song["highscore"]
                song["notes"]
            except KeyError:
                pass
            else:
                return song
    log.warning("Cannot read song path '%s' because it's broken!"%path)
    return {}
