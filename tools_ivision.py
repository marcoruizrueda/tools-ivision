# coding=utf-8

#Dependences: sudo pip install sk-video moviepy ez_setup

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import skvideo.io
import os
import distutils.dir_util


def extractSubclip(pathVideo, t1, t2):
	"Extract subclip (shoot) from t1 to t2 (time in seconds)"	
	print("			_________Extracting subclip....")
	targetname = nameVideo(pathVideo, t1, t2)
	path_subVideo = os.path.dirname(os.path.abspath(pathVideo))
	path_subVideo = os.path.join(path_subVideo, targetname)
	
	ffmpeg_extract_subclip(pathVideo, t1, t2, path_subVideo)
	print("			_________Video created: %s"%targetname)
	return path_subVideo


def extractFrames(pathVideo):
	"Extract frames for video (saved in folder 'frames' in the same folder as the video)"
	print("			_________Extracting frames....")	
	path = os.path.dirname(pathVideo)
	path_frames = os.path.join(path,"frames")
	distutils.dir_util.mkpath(path_frames) #create folder 'frames'
	
	videogen = skvideo.io.vreader(pathVideo)
	f = 0
	for frame in videogen:
		f=f+1;		
		skvideo.io.vwrite(os.path.join(path_frames,"frame-%d%s"%(f,".png")), frame)
	print("			_________%d Frames created in: %s"%(f, path_frames))	
	return path_frames


def nameVideo(pathVideo, t1, t2):
	"Create name for the new video"	
	pathVideo = os.path.basename(pathVideo)	
	name,ext = os.path.splitext(pathVideo)
#	T1, T2 = [int(1000*t) for t in [t1, t2]]
        targetname = "%s_Sec%d-%d%s"%(name, t1, t1+t2, ext)
	return targetname


