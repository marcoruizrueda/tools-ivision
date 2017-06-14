Development setup
=================

* FFMPEG:

If you don't have ffmpeg installed, run the following command:

	$ sudo add-apt-repository ppa:jonathonf/ffmpeg-3
	
	Press [ENTER]
	
	$ sudo apt update && sudo apt install ffmpeg libav-tools x264 x265

For more details, author's site: http://ubuntuhandbook.org/index.php/2016/09/install-ffmpeg-3-1-ubuntu-16-04-ppa/

* INSTALLING DEPENDENCES

From the root of the repo, run the following command:

	$ pip install -r requirements/requirements.txt
