import sys
import time

def type_text(text, delay_ms=30):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_ms / 1000.0) 

def dot_generate(word):
    for i in range(4):
                dots = "." * i
                print(f"\r{word}{dots}   ", end='', flush=True)
                time.sleep(0.5)
    time.sleep(0.5)