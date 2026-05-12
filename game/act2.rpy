label act2_start:

    ## ACT 2 - STRUCTURE (MARKET AND COMMERCE)
    
    scene bg smallrestaurant
    with Dissolve(1.0)
    
    "The air conditioning is a godsend, but it feels sterile after the market."
    
    show belinda talking at left:
        xalign 0.25
    with dissolve
    
    belinda "We try to keep it consistent. A bowl here tastes the same as a bowl in the mall. That's what the usual patrons want."
    
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
    
    scene bg smallrestaurant2
    with Dissolve(1.0)
    
    "Neon lights. A sous-vide machine is humming in the corner. Marco is plating batchoy with a pair of tweezers."
    
    show marco at right
    with dissolve
    
    marco "People think I'm betraying the dish because I use a pork dashi base. But look at this crowd, Burnok. They're twenty-somethings. They'd never step foot in the wet market. Being trendy is how you pique their interest."
    
    show burnok at left
    with dissolve
    
    burnok "But if you change the base, is it still the same dish?"
    
    show marco thinking at right
    
    marco "(He stops, his tweezers hovering over a piece of chicharon.) I grew up in my Lolo's stall. I have his old cleaver in my kitchen. I just... I don't want us to be a 'heritage' museum. I want us to be relevant. Besides, time changes everything; it's an adapt or be stagnant in this flowing river of so-called life."
    
    "He looks at his phone. A new notification for a food vlog. He sighs, looking more tired than he did a minute ago."
    
    hide marco
    hide burnok
    with dissolve
    
    scene bg lapazmarketstall2
    with Dissolve(1.0)
    
    "I'm at a stall with a bright vinyl banner. There's a QR code for payments. The 'Special' is prominently displayed."
    
    "The bowl is porcelain, perfectly white. The garnish is arranged like a bouquet."
    
    show burnok thinking at center
    with dissolve
    
    burnok "It looks... Instagrammable. But where's the steam?"
    
    hide burnok
    with dissolve
    
    "I take a bite. It's sweet. Too sweet. I can't even get a hint of salt. The liver is missing that punch, replaced by extra sugar and MSG."
    
    show burnok at center
    with dissolve
    
    menu:
        "What should I think about this bowl?"
        
        "So... this is batchoy for people who are afraid of the market.":
            burnok "They've sanded down all the rough edges. It's a caricature of what Lola Consing makes."
            "It's efficient. It's clean. It's a product, not a process."
            
        "Is this the cost of 'accessibility' and 'cultural amalgamation'?":
            burnok "If the majority seems to like it, does it still belong to the taste of the people who used to create it?"
            "The flavor is standardized. The machine has won."
    
    hide burnok
    with dissolve
    
    "I have three versions of batchoy in my stomach, and none of them fully agree with each other."
    
    show burnok thinking at center
    with dissolve
    
    burnok "Lola Consing's feels like survival. Ted's feels like security. Marco's feels like an argument. And the tourist bowl feels like an apology for all three."
    
    "The economics make sense on paper. Supply, demand, price point, market share. But none of that explains why people get angry when the recipe changes. Why it feels personal."
    
    burnok "This isn't about the soup anymore. Maybe it never was."
    
    hide burnok
    with dissolve
    
    # Transition to Act 3
    scene bg black
    with Dissolve(1.5)
    
    "To be continued..."
    
    jump act3_start

    return