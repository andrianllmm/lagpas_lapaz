label act2_start:

    ## ACT 2 - STRUCTURE (MARKET AND COMMERCE)
    
    scene bg smallrestaurant2
    with Dissolve(1.0)
    
    "Burnok now enters a restaurant. The air conditioning is a godsend, but it feels sterile after the market."
    "So this is TED's..."
    show belinda talking at left:
        xalign 0.25
    with dissolve
    
    belinda "Welcome to TED's. We try to keep it consistent, A bowl here tastes the same as a bowl in the market. That's what the usual patrons want."
    
    menu:
        "What should I ask Ate Belinda?"
        
        "Does that mean you lose the 'grit' of the original?":
            show belinda talking at left:
                xalign 0.25
            
            belinda "Grit doesn't come with a health permit, 'noy. Staff here have SSS, PhilHealth, and clean uniforms. That's what 'original' means to the people who make it."
            
        "The prices are almost double what they are in the market.":
            show belinda talking at left:
                xalign 0.25
            
            belinda "You're paying for the floor being mopped every thirty minutes. You're paying so you don't have to sweat into your soup. Is that a crime?"
            
            "She adjusts her visor, looking proud of the polished stainless steel counters."
    
    hide belinda talking
    with dissolve
    
    scene bg smallrestaurant
    with Dissolve(1.0)
    "After several steps he visits the modern stall within the area"
    "Neon lights. A sous-vide machine is humming in the corner."
    show marco at center
    with dissolve 
    "Marco is plating batchoy with a pair of tweezers."
    show marco talking
    marco "People think I'm betraying the dish because I use a pork dashi base."
    show burnok thinking at left
    with dissolve
    show marco talking at right with move:
        xalign 0.75
    marco "But look at this crowd, Burnok."
    extend " They're twenty-somethings."
    extend " They'd never step foot in the wet market. Being trendy is how you pique their interest."
    
    show burnok thinking at left
    with dissolve
    
    burnok "But if you change the base, is it still the same dish?"
    
    show marco thinking
    
    "He stops, his tweezers still hovering over a piece of chicharon."
    show marco talking
    marco "I grew up in my Lolo's stall. I have his old cleaver in my kitchen. I just..."
    extend " I don't want us to be a 'heritage' museum. I want us to be relevant. Besides, time changes everything, it's an adapt or be stagnant in this flowing river of so-called life."
    
    show marco thinking
    "He looks at his phone. A new notification for a food vlog. He sighs, looking more tired than he did a minute ago."
    
    hide marco
    with dissolve
    hide burnok
    with dissolve
    scene bg black
    with dissolve
    scene bg moodyroom
    with Dissolve(2.0)
    play music "audio/umib_012.ogg" loop
    
    burnokint"I'm at a stall for tourists with a bright vinyl banner. There's a QR code for payments and the 'Special' is prominently displayed..."
    
    burnokint "This porcelain bowl here, perfectly white. All the garnish is arranged like a bouquet."
    
    show burnok thinking at center
    with dissolve
    
    burnok "It looks... Instagrammable. But where's the steam?"
    
    hide burnok
    with dissolve
    
    burnokint "I take a bite of the batchoy. It's sweet. Too sweet. I can't even get a hint of salt."
    extend " The liver is missing that punch, replaced by extra sugar and MSG."
    
    show burnok at center
    with dissolve
    
    menu:
        burnokint "What should I think about this bowl?"
        
        "So... this is batchoy for people who are afraid of the market.":
            burnok "They've sanded down all the rough edges. It's a caricature of what the batchoy at the wet market makes."
            "It's efficient. It's clean. It's a product, not a process."
            
        "Is this the cost of 'accessibility' and 'cultural amalgamation'?":
            burnok "If the majority seems to like it, does it still belong to the taste of the people who used to create it?"
            "The flavor is standardized. The machine has won."
    
    hide burnok
    with dissolve
    
    burnokint"I have three versions of batchoy in my stomach, and none of them fully agree with each other."
    
    show burnok thinking at center
    with dissolve
    
    burnok "This bowl for tourists feels like a compromise, batchoy that apologizes for smelling like a wet market."
    burnok "Marco's is an argument, that tradition has to change or die."
    burnok "TED's is security, clean, consistent, air-conditioned. A bowl that won't offend anyone."
    burnok "And Lola Consing's stall..."
    extend " wait."
    hide burnok
    with dissolve
    scene bg black
    with dissolve
    burnokint "I don't actually know who runs the original batchoy stall."
    extend" The first one I've been to."
    burnokint "I got a name. Lola Consing. But she just makes the noodles. She's not the one serving the soup."
    burnokint "So who actually owns the original batchoy?"
    scene bg moodyroom
    with Dissolve(2.0)
    show burnok thinking at center
    with dissolve
    
    $ renpy.pause()
    burnok "I've been here for hours, and I don't even know that much."
    burnok "..."
    
    burnok "Well... The economics make sense on paper."
    extend " Supply, demand, price point, market share. But none of that explains why people get angry when the recipe changes."
    extend " Why it feels personal."
    
    burnok "This isn't about the soup anymore. Maybe it never was."
    
    hide burnok
    with dissolve
    stop music fadeout 2.0
    # Transition to Act 3
    scene bg black
    with Dissolve(1.5)
    
    jump act3_start

    return