from math import sin
from time import sleep

# Configuration parameters
character = '*'
wave_amplitude = 50
pass_count = 1  # Tracks the number of complete cycles
angle_increment = 0.05
angle = 1  # Initial angle for the sine wave

while True:
    sleep(0.1)  # Controls the animation speed
    angle += angle_increment
    pass_count += 1
    sinus_value = sin(angle) * wave_amplitude
    
    # Ensure sinus_value is positive for consistent spacing
    if sinus_value < 0:
        sinus_value = abs(sinus_value)
    
    # Calculate spacing between DNA strands
    inner_space = sinus_value - 4
    
    # Alternate between full line and spaced pattern
    if pass_count % 2 == 0:
        dna_line = character * int(sinus_value)
    else:
        dna_line = character * 2 + ' ' * int(inner_space) + character * 2

    # Center the DNA line within a fixed width
    centered_line = dna_line.center(100, ' ')
    print(centered_line)

