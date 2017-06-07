# coding=utf-8

import tools_ivision as tv


pathVideo = r'/home/marco/Desktop/videos/Raly/raly.mp4' #Caminho do vídeo
t1 = 0 	#Tempo inicial (segundos)
t2 = t1 + 2	#Tempo final (segundos)

#path_subVideo = tv.extractSubclip(pathVideo, t1, t2)
#path_frames = tv.extractFrames(path_subVideo)
path_frames = tv.extractFrames(pathVideo)
