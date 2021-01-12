# WM
WM is a video player that show it on the terminal as a text!

# usage
first, opencv must be installed:
```
$ pip install opencv-python
```
*note: use `pip3` to install for python3*

then, run like this:
```
$ python3 main.py INPUT [-o OUTPUT] [--width WIDTH] [--height HEIGHT]
```
where `INPUT` is the video file (e.g. **example/input.mkv**).

other arguments are optional. `OUTPUT` is the folder for ouput text files (default: `./output`). `WIDTH` and `HEIGHT` define the width and height of output (default: size of terminal, where program is running there).

# test
if you want to see a preview of it or test it, you can run this command:
```
$ python3 main.py example/input.mp4 -o example/output
```
