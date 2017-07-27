import os
import re
from pydub import AudioSegment
import easygui as eg

#REQUIRES:
#http://ffmpeg.zeranoe.com/builds/

msg="WAV file origin"
title="My WAVs"
default="D:\Users\gcz\Music"
wav_path = eg.diropenbox(msg, title, default)

msg="MP3 file destination"
title="My MP3s"
default= wav_path
mp3_path = eg.diropenbox(msg, title, default)

br = "256k"
files = os.listdir(wav_path)
i = 1
for f in files:
    tag_dict = {'artist': 'Michel Thomas', 'album': 'CD08', 'comments': 'Aulas de Portugues'}
    if re.match('.*\.wav$', f):
        sound = AudioSegment.from_file(os.path.join(wav_path,f))
        print os.path.join(mp3_path,'.'.join([f[:-4],'mp3']))
        #sound.export(os.path.join(mp3_path,'.'.join([f[:-4],'mp3'])), format="mp3", tags=tag_dict)
        sound.export(os.path.join(mp3_path,'_'.join([tag_dict['artist'], tag_dict['album'], str(i),'.mp3'])), format="mp3", tags=tag_dict)
        i+=1
