#!/usr/bin/env python3
import argparse
import sys
import os
import atexit
from os import system, makedirs, remove, get_terminal_size as size
from os.path import exists, join
from shutil import which

from log import log
from generator import convert, CHAR_SETS
from sound import getaudio, Audio


def check_dependencies():
    missing = []
    if not which("ffmpeg"):
        missing.append("ffmpeg")
    if not which("go") and not which("wm_reader"):
        missing.append("go")
    if not which("play"):
        missing.append("play")
    if missing:
        log.error(f"Missing: {', '.join(missing)}")
        sys.exit(1)


def main():
    check_dependencies()

    parser = argparse.ArgumentParser(description="WM - Terminal Video Player")
    parser.add_argument("path", help="Path to input video file")
    parser.add_argument("-o", "--out", default="output", help="Output directory (default: ./output)")
    parser.add_argument("--width", type=int, help="Override terminal width")
    parser.add_argument("--height", type=int, help="Override terminal height")
    parser.add_argument("-c", "--color", action="store_true", help="Enable color output")
    parser.add_argument("-s", "--save", action="store_true", help="Do not delete temporary frames after playback")
    parser.add_argument("--charset", choices=CHAR_SETS.keys(), default="classic", help="Character set for rendering")
    args = parser.parse_args()

    log.info("start main process and importing")

    input_path = args.path
    out = args.out

    if not exists(input_path):
        log.error(f"Input file not found: {input_path}")
        sys.exit(1)

    if not exists(out):
        makedirs(out)
    else:
        log.warning("output path is existing. text files will be overwritten.")

    log.info("set width and height of output...")
    try:
        ts = size()
        width = args.width or ts.columns
        height = args.height or ts.lines - 1
    except OSError:
        width = args.width or 100
        height = args.height or 30

    log.info("start convert process")
    details = convert(input_path, out, width, height, log, args.color, args.charset)
    fps = details["fps"]

    log.info("extracting audio...")
    audio_path = join(out, "sound.mp3")
    getaudio(input_path, audio_path, log)
    log.info("extracted. make Audio object")
    audio = Audio(audio_path)
    log.info("start sound player and texts reader process...")

    audio.start()

    # Wait a moment for audio to initialize
    import time
    time.sleep(0.3)

    # Try to use compiled binary first, then fall back to go run
    reader_bin = which("wm_reader")
    if reader_bin:
        system(f'"{reader_bin}" {fps} "{out}" {int(args.color)}')
    else:
        system(f'go run reader.go {fps} "{out}" {int(args.color)}')

    if not args.save:
        log.info("removing files...")
        if exists(audio_path):
            remove(audio_path)
        for x in range(1, details["count"] + 1):
            frm_path = join(out, str(x) + ".frm")
            if exists(frm_path):
                remove(frm_path)

    log.info("done!")


if __name__ == "__main__":
    main()
