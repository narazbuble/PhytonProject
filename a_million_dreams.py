import time
import sys
from colorama import init, Fore

init()

def a_million_dreams():
    lirik = [
        "'Cause every night I lie in bed",
        "The brightest colors fill my head",
        "A million dreams are keeping me awake",
        "I think of what the world could be",
        "A vision of the one I see",
        "A million dreams is all it's gonna take",
        "A million dreams for the world we're gonna make."
    ]

    delay_per_line = [2.0, 2.0, 6.0, 2.0, 2.0, 4.0, 3.0]  
    
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.WHITE, Fore.BLUE]

    for i in range(len(lirik)):
        color = colors[i % len(colors)]
        for char in lirik[i]:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(0.02)
        print(Fore.RESET)   
        time.sleep(delay_per_line[i])

a_million_dreams()

