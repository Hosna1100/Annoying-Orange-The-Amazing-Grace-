## script-poemresponses.rpy
label poemresponse_start:
    # These variables set the amount of poems read by the player and disables
    # the skip transition.
    $ poemsread = 0

    $ skip_transition = False

    label poemresponse_loop:

        $ skip_poem = False

        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        
        # This if/else statement determines the wipeleft effect is applied to the
        # screen transition or not.
        if skip_transition:
            scene bg kitchen
        else:
            scene bg kitchen
            with wipeleft_scene
        $ skip_transition = False

        # This if statement checks if no music is playing to play Okay Everyone.
        if not renpy.music.get_playing():
            play music t5

    label poemresponse_start2:
        $ skip_poem = False
        
        # This if/else statement checks if we are in Act 2 to show Act 2 specific
        # poems.
        if persistent.playthrough == 2:
            $ pt = "2"
        else:
            $ pt = ""

        # This if/else statement determines what MC will say in the poem selection
        # menu depending on how many poems you have read.
        if poemsread == 0:
            $ menutext = "Who should I show my poem to first?"
        else:
            $ menutext = "Who should I show my poem to next?"

        ## Main Menu of the Poem Responses
        menu:
            "[menutext]"

            # These statements will show each character as a option to share your
            # poem with unless their conditions are met.

            # This will show Apple as a menu option IF you haven't shared your
            # poem to him and you are in Act 1.
            "Apple" if not a_readpoem and persistent.playthrough == 0:
                # This variable sets that you have read Sayori's poem.
                $ a_readpoem = True
                if chapter == 1 and poemsread == 0:
                    mc "...you, Apple!"
                # This call statement calls Sayori's poem response script.
                call poemresponse_apple

            # This will show Orange as a menu option IF you haven't shared your
            # poem to her.
            "Orange" if not o_readpoem:
                $ o_readpoem = True
                if chapter == 1 and poemsread == 0:
                    mc "Orange, of course!"
                    "It's probably only fair if I share my poem with him first."
                call poemresponse_orange

        # This variable increases the poems read by 1.
        $ poemsread += 1
        
        # This if/else statement checks if we have not yet read 3 poems for Act 2 
        # or if we are in Act 1 and haven't read 4 poems.
        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4):
            jump poemresponse_loop

    # These variables resets the read poem variables back to normal.
    $ a_readpoem = False
    $ o_readpoem = False
    $ poemsread = 0
    return

# These labels calls each characters' poem response result given how much they
# liked your poem.
label poemresponse_apple:
    scene bg kitchen
    show apple normal zorder 2 at t11
    with wipeleft_scene
    # This if/elif statement checks if Sayori's opinion of your poem was bad
    # or good.
    if a_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif a_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    
    # These variables sets the next scene chapter to be called based off the
    # chapter and poem opinion and calls it.
    $ nextscene = "ch" + pt + str(chapter) + "_a_" + poemopinion
    call expression nextscene
    
label poemresponse_orange:
    scene bg kitchen
    show orange normal zorder 2 at t11
    with wipeleft_scene
    
    if o_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif o_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"

    # These variables sets the next scene chapter to be called based off the
    # chapter and poem opinion and calls it.
    $ nextscene = "ch" + pt + str(chapter) + "_o_" + poemopinion
    call expression nextscene

## Poem Opinion Responses
# This is where the characters will react to how they liked your poem from
# good to bad.
label ch1_o_bad:
    o "..."
    mc "...?"
    o 2b "[player], you wrote this for Apple, right?."
    mc "W-What??"
    mc "How..."
    o 42c "Because you said you love him~"
    mc "Don't say that again!"
    o "his embarrassed expression was funny."
    mc "It was the first time he ever has blushed, hm?"
    o "Yeah!"
    mc "I think his pessimism is kind of..."
    mc "cute~"
    mc "By the way, have you ever blushed?"
    o "yes but I will NOT tell you who I blushed in front of!"
    mc "Actually, I know who is it."
    mc "but don't worry~ I won't tell anyone!"
    o  "..."
    o "Thanks."
    o "Nobody was supposed to know this secret."
    o "I wonder how the HELL you found that out."
    o "Hmmmm........"
    return

label ch1_o_good:
    o "..."
    mc "...?"
    o "hmmm...you wrote this for me, didn't you?"
    mc "Er..."
    mc "..."
    "Orange re-reads my poem."
    o "Obviously!"
    mc "Eh? is it that much of obvious...?"
    o "Yeah!"
    mc "Apple won't or DIDN'T like that..."
    o "Of course he doesn't like things that are in my style!"
    o "He is sometimes a BOMB of fire!"
    mc "..."
    mc "It's interesting how you have a plenty of good friends while I don't have any friends."
    mc "And I am..."
    mc "{nw}Depressed"
    o "Hehe"
    o "!"
    o "Wait what?"
    o "No friends?"
    mc "I have friends but they are all hypocrite and rude and disloyal and anything bad you can imagine!"
    o "Urk--"
    "Orange's retort gets caught in...hm?"
    o "Grrrr..."
    o "..."
    o "Perhaps if we fruits be good friends to you..."
    o "Then, it would be something that we can turn back to you because Er...we're sort of obligated so we should give you something in return because you seem protective toward us."
    mc "Pretty sure you never actually said that..."
    "I say that mostly to myself."
    "It's odd to see him be like this..."
    "But it's good that FINALLY, someone is loyal to me."
    return

label ch1_a_bad:
    a "..."
    a "..."
    a "[player]..."
    a "You wrote this poem for Orange? hehe. because it's obvious you look someone naughty like him."
    a "But I hope you won't end up be JUST LIKE him!"
    mc "Eh?!"
    mc "Well if I won't be able to impress you then, I won't be able to show you that"
    mc "{nw}I"
    mc "{nw}love"
    mc "{nw}you"
    show apple embarrassed zorder 2 at hf11
    a "E-eh...D-don't say that again!"
    "Can fruits even blush? Well, Apple's blush is making him cuter."
    mc "Er...well, sorry."
    mc "I'm actually serious about that!"
    a "See?"
    show Apple zorder 2 at d11
    a "Your making me more embarrassed!"
    mc "Yeah, sorry"
    show apple closedeyes zorder 2 at f11
    a "..."
    "I don't think we had a really good conversation..."
    "But he remembers me Natsuki because this both are acting like a REAL tsundere."
    return

label ch1_a_good:
    s 1n "..."
    s "...Oh my goodness!"
    s 4b "This is sooooo good, [player]!"
    mc "Eh?"
    s 4r "I love it~!"
    s "I had no idea you were such a good writer!"
    mc "Sayori..."
    mc "You must be seriously overreacting."
    mc "I'm not a good writer at all."
    mc "I honestly have no idea what I'm doing."
    s 1x "Well..."
    s "Maybe that's why!"
    s "Because I have no idea what I like, either!"
    s 1r "Ahahaha!"
    mc "Jeez..."
    mc "Are you sure you don't like it just because I wrote it?"
    s 1b "Eh?"
    s "Well, I'm sure that's part of it."
    s 1x "I think I understand you better than a lot of other people, you know?"
    s "So when I read your poem..."
    s "It's not just a poem..."
    s 4q "It's a [player] poem!"
    s "And that makes it feel extra special!"
    s "Like I can feel your feelings in it~"
    "Sayori hugs the sheet against her chest."
    mc "You're so weird, Sayori..."
    s "Ehehe..."
    return