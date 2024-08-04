label pear_exclusive_1:
    scene bg bedroom
    with wipeleft_scene
    play music t6
    mc "Phew..."
    "I guess I'm done."
    "I glance around the room."
    "That was a GREAT! I got the chance to show Pear my skill!"
    "Perhaps I should show him my codding skills?"
    "Or when I hardly draw things in my PC with mouse?"
    mc "Everyday, I imagine a future where I can be with you"
    mc "In my hand, is a pen that will write a poem of me and you!"
    mc "The ink flows down into a dark puddle"
    mc "Just move your hand, write a way into his heart!"
    "I sometimes randomly sing this part of Your Reality."
    "Monika is so impressive, isn't she?"
    "She is the president of a literature club, after all."
    show pear normal zorder 2 at f11
    p "[player]..."
    show pear normal zorder 2 at t11
    "Pear enters my room and hops to reach to me."
    mc "So Pear, are you a fan of books?"
    show pear smilaway zorder 2 at f11
    p "Yeah...sometimes."
    mc "Have you ever read \"Portrait of Markov\"?"
    show pear questioning zorder 2 at f11
    p "No, what's that?"
    show pear normal zorder 2 at t11
    mc "Basically, it's about this girl in high school who moves in with her long-lost younger sister..."
    mc "But as soon as she does so, her life gets really strange."
    mc "She gets targeted by these people who escaped from a human experiment prison..."
    mc "And while her life is in danger, she needs to desperately choose who to trust."
    mc "No matter what she does, she ends up destroying most of her relationships and her life starts to fall apart..."
    show pear stressed zorder 2 at f11
    p "That's dark..."
    show pear smiling
    p "I'd like to read it! Do you have it?"
    show pear <> zorder 2 at t11
    mc "In my PC."
    show pear questioning zorder 2 at f11
    p "Does it have a site?"
    show pear smiling zorder 2 at t11
    mc "Yeah! it's written by Dan Salvato."
    "And you know, who Dan Salvato is...hm?"
    mc "I have the book now..."
    "I grab that book from my desk."
    show pear zorder 2 at f11
    p "Anyways, let's read it now, shall we?"
    show pear closedeyeshappy zorder 2 at h11
    mc "Yeah!"
    hide pear
    scene read_p
    "I open the book then, Pear jumps on it to see it properly. "
    p "Mmm..."
    "{i}Let me read it for you.{/i}"
    jump book

label back:
    scene read_p
    show black zorder 4 with dissolve_cg
    $ currentpos = get_pos() + 2.0
    stop music fadeout 2.0
    show black onlayer front:
        alpha 0.0
        linear 2.0 alpha 1.0
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + "loop 4.618>bgm/3.ogg"
    play music t6
    $ style.say_dialogue = style.edited
    "and it was all we read."
    "Pear was very scared of that so he couldn't continue..."
    "Yeah... I totally forgot that Pear is not into those things."
    "Anyways...I go for writing things for script-ch2.rpy!"
    return
    
    
