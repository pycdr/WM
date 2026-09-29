from os import path as ospath
from cv2 import VideoCapture, cvtColor, COLOR_BGR2GRAY, resize, CAP_PROP_FRAME_COUNT, CAP_PROP_FPS

# ========================
# شخصیت‌های بصری
# ========================
CHAR_SETS = {
    'basic': ' .#',
    'classic': ' .:-=+*#@',
    'extended': " .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
    'shades': ' ░▒▓█',
    'block': ' █',
    'half_blocks': ' ▀▄█',
    'braille': ''.join(chr(0x2800 + i) for i in range(256)),
    'dots': ' .·•°∘○●',
    'geometric': ' .·•°oO0*+×X#@',
}

DEFAULT_CHARSET = 'classic'
d = CHAR_SETS[DEFAULT_CHARSET]

def char(number, charset=DEFAULT_CHARSET):
    number = max(0, min(255, int(number)))
    chars = CHAR_SETS.get(charset, d)
    return chars[number * (len(chars) - 1) // 255]

def text(array, charset=DEFAULT_CHARSET):
    out = ""
    for row in array:
        for y in row:
            out += char(y, charset)
        out += "\n"
    return out

def ctext(array, charset=DEFAULT_CHARSET):
    out = ""
    for row in array:
        for bgr in row:
            b, g, r = int(bgr[0]), int(bgr[1]), int(bgr[2])
            gray = (r + g + b) // 3
            ch = char(gray, charset)
            out += f"\033[38;2;{r};{g};{b}m{ch}"
        out += "\033[0m\n"
    return out

def convert(path, output, w, h, log, color, charset=DEFAULT_CHARSET):
    import os
    if not os.path.exists(output):
        os.makedirs(output)
    log.info("create VideoCapture object...")
    cap = VideoCapture(path)
    log.info("get details of video...")
    count = int(cap.get(CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(CAP_PROP_FPS)) or 24  # مقدار پیش‌فرض در صورت 0
    n = 1
    log.info("start convert loop")
    func = lambda arr: ctext(arr, charset) if color else text(arr, charset)
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            break
        if not color:
            frame = cvtColor(frame, COLOR_BGR2GRAY)
        out_frame = resize(frame, (w, h))
        txt = func(out_frame)
        with open(ospath.join(output, str(n)+".frm"), "w+") as f:
            f.write(txt)
        n += 1
        print(f"converting to text files: {n*100//max(count,1)}%", end='\r')
    log.info("converting finished. release VideoCapture")
    cap.release()
    return {
        "fps": fps,
        "count": max(n-1, 0)
    }

if __name__ == "__main__":
    from argparse import ArgumentParser
    from os import makedirs, get_terminal_size as size
    from os.path import exists
    
    parser = ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-o", "--out", required = False)
    parser.add_argument("--width", type = int, required = False)
    parser.add_argument("--height", type = int, required = False)
    parser.add_argument("--charset", choices=CHAR_SETS.keys(), default=DEFAULT_CHARSET)
    args = parser.parse_args()
    
    path = args.path
    out = args.out or "output"
    if not exists(out):
        makedirs(out)
    
    try:
        ts = size()
        width = args.width or ts.columns
        height = args.height or ts.lines - 1
    except OSError:
        width = args.width or 100
        height = args.height or 30
    
    from log import log
    convert(path, out, width, height, log, False, args.charset)
