# coding=utf-8

import tools_ivision as tv


pathVideo = r'/media/marco/TOSHIBA/videos/-2017.04.08.09.15.47-2017.04.08.10.15.46/Media1/01-BARRIS/Video_1.mp4' #Path to vídeo
t1 = 150 	#Inicial time (seconds)
t2 = 240	#Final time (seconds)

path_subVideo = tv.extractSubclip(pathVideo, t1, t2)
path_frames = tv.extractFrames(path_subVideo)
#path_frames = tv.extractFrames(pathVideo)
