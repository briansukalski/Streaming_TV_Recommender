import time
import sys

#Delays time between characters while printing to allow messages to be more easily read while printing
def scroll_print(msg):
    for i in msg:
        if i == "\n":
            time.sleep(0.25)
        elif i == "_":
            time.sleep(0.2)
        else:
            time.sleep(0.01)
        sys.stdout.write(i)
        sys.stdout.flush()

def scroll_input(msg):
    scroll_print(msg)
    return input("\n")