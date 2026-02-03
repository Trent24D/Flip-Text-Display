# main.py
import time
import sys
from flip_panel import flip_panel as FlipPanel

FPS = 30
FRAME_DELAY = 1 / FPS

def main():
    start = "aaaaaaaa"
    target = "nextstop"
    target = input("Enter hidden text to be debugged: ")

    start = start.lower()
    target = target.lower()

    width = max(len(start), len(target))
    start = start.ljust(width)
    target = target.ljust(width)

    panels = [
        FlipPanel(s, t, 3.0)
        for s, t in zip(start, target)
    ]

    while True:
        now = time.monotonic()

        for panel in panels:
            panel.update(now)

        sys.stdout.write("\r")
        sys.stdout.write("".join(panel.char() for panel in panels))
        sys.stdout.flush()

        if all(panel.done() for panel in panels):
            break

        time.sleep(FRAME_DELAY)

    print()  # newline when finished

if __name__ == "__main__":
    main()
