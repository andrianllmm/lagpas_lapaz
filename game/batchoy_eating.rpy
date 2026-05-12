default batchoy_state = "full"

image batchoy_full = "images/batchoyfull.png"
image batchoy_half = "images/batchoyhalf.png"
image batchoy_empty = "images/batchoyempty.png"

init python:

    def eat_batchoy():

        global batchoy_state

        if batchoy_state == "full":
            batchoy_state = "half"

        elif batchoy_state == "half":
            batchoy_state = "empty"


screen batchoy_eating():

    modal True

    if batchoy_state == "full":

        text "Click the bowl to eat it":
            xalign 0.5
            yalign 0.9

        imagebutton:
            idle "batchoy_full"
            hover "batchoy_full"

            action Function(eat_batchoy)

            xpos 0.5
            ypos 0.55
            anchor (0.5, 0.5)

    elif batchoy_state == "half":

        imagebutton:
            idle "batchoy_half"
            hover "batchoy_half"

            action Function(eat_batchoy)

            xpos 0.5
            ypos 0.55
            anchor (0.5, 0.5)

    else:

        add "batchoy_empty":
            xpos 0.5
            ypos 0.55
            anchor (0.5, 0.5)

        text "Click anywhere to continue":
            xalign 0.5
            yalign 0.9

        button:
            background None
            xfill True
            yfill True

            action Return()

