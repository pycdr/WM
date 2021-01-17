# WM
WM is a video player that show it on the terminal as a text!

# usage
first, be sure that you have `ffmpeg`, or install it (install guides for [windows](http://letmegooglethat.com/?q=how+to+install+ffmpeg+on+windows), [linux](http://letmegooglethat.com/?q=how+to+install+ffmpeg+on+linux) and [MacOS](http://letmegooglethat.com/?q=how+to+install+ffmpeg+on+MacOS))

then you should install its requirements:
```
$ pip3 install -r requirements.txt
```
\* note: 
- *use `pip3` to install for python3*
- *you may need to install `python3-opencv` with your package manager (e.g. `apt install python3-opencv`)*

then, run like this:
```
$ python3 main.py INPUT [-o OUTPUT] [--width WIDTH] [--height HEIGHT]
```
where `INPUT` is the video file (e.g. **example/input.mp4**).

other arguments are optional. `OUTPUT` is the folder for ouput text files and audio of the video (default: `./output`). `WIDTH` and `HEIGHT` define the width and height of output (default: size of terminal, where program is running there).

# test
if you want to see a preview of it or test it, you can run this command:
```
$ python3 main.py example/input.mp4 -o example/output
```
