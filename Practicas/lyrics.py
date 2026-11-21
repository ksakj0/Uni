import sys
import time
import random

colors = [
    '\033[1;91m', # red
    '\033[1;92m', # green
    '\033[1;93m', # yellow
    '\033[1;94m', # blue
    '\033[1;95m', # purple
    '\033[1;96m', # cyan
    '\033[1;97m', # white
]
reset = '\033[0m'

symbols = ['♪', '♫']

def print_lyrics():
    lines = [
        "Ojitos mentirosos, no me mires", 
        "Tu mirada tierna me enloquece",
        "Ese tu mirar se parece",
        "Al radiante sol que amanece",
        "",
        "",
        "Mienten, mienten tus ojitos",
        "Mira, mira tan bonitos",
        "Y mi corazon se hace pedacitos",
        "Y mi corazon se hace pedacitos",
        "Mienten, mienten tus ojitos",
        "Mira, mira tan bonitos",
        "Y mi corazon se hace pedacitos",
        "Y mi corazon se hace pedacitos",
        "",
    ]
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        symbol = random.choice(symbols)
        print(color, end='')
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.09)
        if line.strip() != "":
            print(f" {symbol}{reset}")
        else:
            print(reset)
        time.sleep(1.1)

if __name__ == "__main__":
    print_lyrics()  