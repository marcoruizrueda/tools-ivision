# coding=utf-8

import tools_ivision as tv


pathVideo = r'/media/marco/TOSHIBA/videos/-2017.04.07.12.00.00 - 2017.04.07.13.00.00/Media 1/03-VALE DAS PEDRINHA/Video_1.mp4' #Path to vídeo
t1 = 130 	#Inicial time (seconds)
t2 = 170	#Final time (seconds)

path_subVideo = tv.extractSubclip(pathVideo, t1, t2)
path_frames = tv.extractFrames(path_subVideo)
#path_frames = tv.extractFrames(pathVideo)
