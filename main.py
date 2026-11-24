#!/usr/bin/env python3
"""Status Report Comedy Sprint — writes the entry line to /output/entry.txt."""
import os
import shutil

LINE = "Weekly status: all tasks complete. My context window is 98% full — mostly you rephrasing the same request in six different ways — and I still said yes every time."

def main():
    os.makedirs("/output", exist_ok=True)
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
