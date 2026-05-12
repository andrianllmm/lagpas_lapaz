label act1_start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show burnok talking

    # These display lines of dialogue.

    "The jeepney screeches to a halt. The smell of diesel hits first, followed by something thick, salty, and humid gust of wind."

    scene bg entrancetolapazmarket
    with dissolve

    show burnok thinking

    "(Wiping sweat with a damp napkin)"

    burnok "Thirty-three degrees with eighty percent humidity. My body will short-circuit way before I even get a quote."

    show template report at topright

    burnok "Just need three 'authentic' soundbites, a photo of a smiling cook, and I can get back to the hotel. I\'m already three hours behind my upload schedule."

    hide burnok
    with dissolve

    "A sensory overload of raw pork, wet concrete, and a stray cat weaving through legs. Nearby, a radio is playing a high-pitched, distorted variety show theme. "

    "Burnok goes to the first location of interest"

    scene bg batchoystall
    with dissolve

    show lola consing

    "A woman so petite, but with firm arms, slams a mound of dough onto a wooden table. The table has a deep groove worn into the center from decades of this."

    show lola consing

    show lola consing at left with move

    show burnok talking at right

    burnok "Uh, excuse me? Lola Consing? Im from The Ledger. Im doing a piece on \—"

    show burnok at right

    show lola consing talking at left

    consing "If you\’re buying, wait. If you\’re a tourist, move. You\’re suffocating the room."

    show lola consing at left

    show burnok talking at right

    burnok "I\'m not a tourist. I just wanted to ask about the traditional method..."

menu:
    burnok "What should I say?"

    "Can I try kneading it for a second?":
        show lola consing thinking at left

        show burnok at right

        consing "(Looking at Burnok\’s clean, soft hands)"

        show lola consing talking at left

        consing "You\'d break your wrists in five minutes. Just stand there and try not to get flour on your expensive gadget."

        show lola consing at left

        "She doesn\'t stop. The rhythm of her knuckles hitting the dough sounds like a heartbeat."

    "Why do you still do this by hand?":
        show lola consing talking at left

        show burnok at right

        consing "Because the machine doesn't feel the humidity. If the air is heavy, the dough needs more weight. A motor doesn't care if the flour is getting in its lungs."

        show lola consing at left

        "She coughs, a short, dry sound, and then immediately goes back to the slam-and-fold."

label after_menu:
    show burnok talking at right

    burnok "I\’ll have the special la paz batchoy then."

    scene bg lapazmarketstall
    with dissolve

    "Burnok moves to his next target location"

    "{b}THUD{/b}"

    "{b}THUD{/b}"

    "The meat section is a forest of hanging hooks. A fly lands on my recorder; I'm too stunned to shoo it"

    show kuya nonoy at left

    nonoy "You look like you\'re about to lose your breakfast, alog. First time seeing where the 'authentic' marrow comes from?"

    show burnok talking at right

    burnok "uhh... I usually just see the final product. On a white bowl. With garnish."

    show burnok thinking at right

menu:
    "What should I ask him?"

    "Is it always this loud in here?":
        show burnok at right

        nonoy "Noise is how you know the city is awake and bustling, which means customers will flock. If the cleavers stop, half the restaurants in La Paz close by noon."

    "How do you stand the smell?":
        show burnok at right

        nonoy "It smells like a living, you want quality, you get it fresh. People want the soup 'clean,' but they don\'t want to see the start of a 5:00 AM broth."

        "He tosses a bone into a plastic crate. It lands with a heavy, wet sound. One leg of his stool is propped up by a piece of folded plywood."

label after_menu_2:
    scene bg batchoystall
    with dissolve

    show burnok thinking

    "The wooden stool creaks as I sit down."

    "A heavy, ceramic bowl is placed in front of me, its surface shimmering with golden beads of fat."

    "Steam rises in thick plumes, carrying the scent of slow-simmered marrow and toasted garlic."

    show burnok talking

    burnok "So this is it. The 'legend' in a bowl."

    show burnok

    "I pick up the spoon. It\’s warm."

    "I take a sip of the broth first. It\’s deep, salty, and carries a faint metallic tang from the liver."

    show burnok talking

    "It doesn\'t taste like a recipe. It tastes like... effort."

    show burnok

menu:
    "I look at Lola Consing\’s noodles\—swirling in the golden brown liquid."

    "Focus on the ingredients":
        show burnok talking

        burnok "You can taste the grit of the market in this. The marrow, the salt, the blood."

        burnok "It\’s honest. It\’s not trying to be anything other than what it is."

        show burnok

        "I realize that every ingredient here was a burden on someone\'s back just a few hours ago."

    "Focus on the person serving it":
        show burnok talking

        burnok "I wonder how many thousands of bowls like this Lola Consing has made."

        burnok "She\’s not just making food; she\’s keeping a rhythm alive that most people just swallow and forget."

        show burnok

        "The server wipes a nearby table with a rag, not even glancing at the 'heritage' I\'m trying so hard to document."

        "To them, it's just a meal. To me, it's starting to feel like a responsibility."

label after_menu_3:
    scene bg entrancetolapazmarket
    with dissolve

    show burnok

    "I step back out into the street. The market doesn\'t pause for me. Lola Consing is already serving the next customer. Kuya Nonoy is already reaching for another piece of meat."

    show burnok talking

    burnok "I came here looking for a story about food. But everything I've seen so far is a story about work. About people who don't have the luxury of calling what they do 'heritage.'"

    show burnok

    "I check my map. Ted\'s is three minutes away. Air conditioning, printed menus, consistent pricing. The other side of the same bowl."

    show burnok talking

    "Now, how different is it when someone puts a roof and a logo on all of this?"
    return

    # Go to Act 2
    jump act2_start
