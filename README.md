# WM
WM is a video player that show it on the terminal as a text!

# Installation
0. be sure that you have installed `python3` and `go`.
1. first, you have to install `ffmpeg` (install guides for [windows](http://letmegooglethat.com/?q=how+to+install+ffmpeg+on+windows), [linux](http://letmegooglethat.com/?q=how+to+install+ffmpeg+on+linux) and [MacOS](http://letmegooglethat.com/?q=how+to+install+ffmpeg+on+MacOS))

2. then, you should install its requirements:
```
$ pip3 install -r requirements.txt
```

note: 
- if you are using linux, you will have `pygobject`. if there's any issue with that (e.g. `no module named gi`), it may need some other dependencies for your OS. read [its document](https://pygobject.readthedocs.io/en/latest/getting_started.html). also [this link](https://askubuntu.com/questions/80448/what-would-cause-the-gi-module-to-be-missing-from-python) can be helpful too (thank to @lnxpy).
- use `pip3` to install for python3
- you may need to install `python3-opencv` with your package manager (e.g. `apt install python3-opencv`)

# Usage

you can run like this:
```
$ python3 main.py INPUT [-o OUTPUT] [--width WIDTH] [--height HEIGHT]
```
where `INPUT` is the video file (e.g. **example/input.mp4**).

other arguments are optional. `OUTPUT` is the folder for ouput text files and audio of the video (default: `./output`).
`WIDTH` and `HEIGHT` define the width and height of output (default: size of terminal, where program is running there).

# Test / Example
if you want to see a preview of it or test it, you can run this command:
```
$ python3 main.py example/input.mp4 -o example/output
```
# Issue
if you see any problem in the program, you can tell us in the **Issues** part of this repository.
it is better to send the content of the `report.log` file, too!
