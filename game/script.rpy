# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define burnok = Character("Burnok")
define santos = Character("Dr. Santos")
define consing = Character("Lola Consing")
define marco = Character("Marco")
define nonoy = Character("Kuya Nonoy")
define melinda = Character("Ate Melinda")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show burnok talking

    # These display lines of dialogue.

    "The jeepney screeches to a halt. The smell of diesel hits first, followed by something thick, salty, and humid gust of wind."

    scene bg entrancetolapazmarket

    show burnok thinking

    "(Wiping sweat with a damp napkin)"

    burnok "Thirty-three degrees with eighty percent humidity. My body will short-circuit way before I even get a quote." 

    show template report at topright

    burnok "Just need three 'authentic' soundbites, a photo of a smiling cook, and I can get back to the hotel. Im already three hours behind my upload schedule."

    # This ends the game.

    return
