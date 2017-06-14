# coding=utf-8

import tools_ivision as tv


pathVideo = r'/media/marco/TOSHIBA/videos/2017.04.08.08.00.00 - 2017.04.08.10.00.00/Media 1/02-MERCADO DO RIO VERMELHO/Video_1.mp4' #Path to vídeo
t1 = 2426 	#Inicial time (seconds)
t2 = 2475	#Final time (seconds)

path_subVideo = tv.extractSubclip(pathVideo, t1, t2)
path_frames = tv.extractFrames(path_subVideo)
#path_frames = tv.extractFrames(pathVideo)
