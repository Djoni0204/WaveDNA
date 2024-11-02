from math import sin
from time import sleep
from colorama import Fore, init
import random

# Configuration parameters
character = '%'
colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.MAGENTA, Fore.CYAN]
wave_amplitude = 50
pass_count = 1  # Tracks the number of complete cycles
angle_increment = 0.05
angle = 1  # Initial angle for the sine wave

# Initialize colorama with autoreset to ensure colors reset after each line
init(autoreset=True)

while True:
    sleep(0.05) # Controls the animation speed
    angle += angle_increment
    pass_count += 1
    sinus_value = abs(sin(angle) * wave_amplitude)  # Ensure positive value for spacing

    # Calculate spacing between DNA strands
    inner_space = max(0, int(sinus_value - 2))  # Ensure non-negative space

    # Choose a random color for the inner part of the line
    random_color = random.choice(colors)
    
    # Alternate between full line and spaced pattern
    if pass_count % 2 == 0:
        # Full colored line, but edges remain default
        dna_line = character + character + random_color + character * (int(sinus_value) - 2) + Fore.RESET + character + character
    else:
        # Spaced pattern with colored middle, edges remain default
        dna_line = character * 2 + random_color + ' ' * inner_space + Fore.RESET + character * 2

    # Center the DNA line within a fixed width
    centered_line = dna_line.center(100, ' ')
    print(centered_line)


print("Hello World!")
