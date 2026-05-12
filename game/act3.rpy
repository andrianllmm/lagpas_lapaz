label act3_start:
    scene bg fancyroom
    with dissolve

    show santos
    with dissolve

    burnokint "Dr. Santos sips his coffee, looking at me over thick glasses."

    show santos talking
    with dissolve

    santos "You\’re looking for the 'true' origin? Chinese traders, butchers in the 30s, Teodorico Lepura, who learned the recipe from a Chinese merchant."

    show santos at left with move
    with dissolve

    show burnok talking at right with move
    with dissolve

    burnok "I just want to know why people get to have the ability to change the recipe, a mock to the authentic and original soup."

    show burnok
    with dissolve

    show santos talking
    with dissolve

    santos "Because it’s not about the soup, Burnok. It\’s the Superstructure. The stories we tell ourselves to feel like we belong to a place."

    show burnok thinking
    with dissolve

menu: 
    burnok "What should I ask next?"

    "So the 'myth' is more important than the ingredients?":
        show santos talking
        with dissolve

        santos "Exactly. Heritage is a tool. We use it to assert who we are in a world that wants to make us all the same."

    "Does the 'Ilonggo Identity' depend on a bowl of noodles?":
        show santos talking
        with dissolve

        santos "It’s a symbol. When you eat batchoy, you aren\’t just consuming calories, you\’re consuming history, pride, and social status."

label act3_continuation:
    scene bg lapazplaza
    with dissolve

    "The plaza is packed. Long, plastic tables. The sound of a hundred spoons clinking against ceramic."

    show lola consing happy at left
    with dissolve

    show marco at right
    with dissolve

    burnokint "I see Lola Consing sitting on a bench, rubbing her wrist. "
    extend "Marco is standing by a pillar, watching a group of kids eat a traditional bowl."

    hide lola consing happy
    hide marco
    with dissolve

    show burnok thinking
    with dissolve

    burnok "Come on, turn on... just one more..."

    show burnok thinking
    with dissolve

    burnokint "The battery for my recorder finally dies... what an exhausting day."
    "The steam from a nearby table hits my face."

    "A toddler at the next table drops his spoon. It clangs on the floor. His mother wipes it on her shirt and hands it back. No one is talking about 'heritage.' They're just eating."

    scene bg moodyroom
    with dissolve

    show burnok thinking
    with dissolve

    burnokint "The cursor on my laptop is a heartbeat. "
    extend "Blink. "
    extend "Blink."

    show burnok talking
    with dissolve

    burnok "I could write the 'Love and Tradition' piece. It\’s what the editor wants. It\’s easy. It\’ll get the clicks."

    burnokint "I look at the photo I took of Lola Consing\’s hands. The flour under her fingernails. The SSS posters in Ted\’s. Marco\’s face when he talked about his Lolo."

    show burnok thinking
    with dissolve

    menu:
        burnok "One story. But which one is the truth?"

        "Write about labor":
            jump ending_labor

        "Write about economics":
            jump ending_economics

        "Write about identity":
            jump ending_identity
