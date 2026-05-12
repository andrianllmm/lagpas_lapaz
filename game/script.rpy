# The script of the game goes in this file.

# The game starts here.

label start:

    # Go to Act 1
    jump act1_start

transform slide_from_right:
    topright
    xoffset 640
    linear 0.5 xoffset 0

transform full:
    size (1920, 1080)
    fit "cover"
    align (0.5, 0.5)  # Add this to ensure cropping from center