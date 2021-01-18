# WM
WM is a video player that show it on the terminal as a text!

# Installation
0. be sure that you have installed `python3` and `go`.
1. first, you have to install `ffmpeg` (install guides for [windows](http://letmegooglethat.com/?q=how+to+install+ffmpeg+on+windows), [linux](http://letmegooglethat.com/?q=how+to+install+ffmpeg+on+linux) and [MacOS](http://letmegooglethat.com/?q=how+to+install+ffmpeg+on+MacOS))
2. it uses `play` to run audio file, which is extraced from input video. if you are using ubuntu/debian, you can install with this ([source](https://askubuntu.com/questions/920539/how-do-you-play-a-sound-from-the-terminal])):
```
sudo apt install sox
sudo apt install libsox-fmt-mp3
```
3. if your `pip` version is less than **19.3**, you should update:
```
pip install --upgrade pip
```
4. then, you should install its requirements:
```
$ pip install -r requirements.txt
```

note: 
- use `pip3` to install for python3, if it makes problem.
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
