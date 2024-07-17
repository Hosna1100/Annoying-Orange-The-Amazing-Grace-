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
    n "..."
    mc "...?"
    n 1t "...Okay, well let's start with the things I don't like!"
    n "First of all, um..."
    mc "..."
    "Natsuki re-reads my poem."
    n 4c "N-Never mind. I don't feel like giving you my opinion."
    mc "Eh? Then what's the point of sharing in the first place?"
    mc "I wrote this when I could have been doing other things."
    n 4r "Uu..."
    mc "In fact, remember how I said I wanted to read your poems?"
    mc "That's what I had in mind when writing this."
    mc "I want to help you feel comfortable enough to share yours."
    mc "Like Monika said."
    n 4x "Uuuu...!"
    n 1h "Well I would be more comfortable sharing my poem if yours was really bad!"
    n 1w "You were supposed to show me some dumb poem and make me go 'Hah, well it's not that great but let me show you what real literature looks like!'"
    n 1h "And you went and ruined it!"
    n "I hope you're happy!"
    mc "..."
    mc "...So, in other words, you're saying you liked it?"
    n 1o "Urk--"
    "Natsuki's retort gets caught in her throat."
    n 1x "Uuuuuuuuu...You're so...!"
    n "You just...you...don't understand anything, do you?"
    n 5q "I already told you that, you don't have to go announcing it to the world like you're all self-important!"
    mc "Pretty sure you never actually said that..."
    "I say that mostly to myself."
    "Natsuki must really hate me or something."
    "I can't figure out if it's a win or a loss that she liked my poem."
    mc "In any case... You still need to show me yours, right?"
    n 5s "Gr... Fine, I guess."
    n "Only because Monika will make me if I don't."
    return

label ch1_a_bad:
    s 1b "..."
    s "...Wow!"
    s "[player]..."
    s 4r "Your poem is really bad!"
    s "Ahahaha!"
    mc "Eh?!"
    s 4a "It's fine, it's fine~"
    s "It's your first time."
    s "Besides..."
    label ch1_a_shared:
        s 1a "I'm really happy just that you wrote one."
        s "It just reminds me of how you're really a part of the club now~"
        "(Not to mention the fact that I'm standing in front of you in the clubroom...?)"
        mc "Er...well, of course."
        mc "I'm not really into it yet, but that doesn't mean I'll break my promise."
        s 1d "See?"
        s "It's like I said before, [player]..."
        s "Deep down, you're not selfish at all, you know?"
        s "Trying new things like this for other people..."
        s 2q "That's something that only really good people do!"
        mc "Thanks...Sayori."
        "...I'm not sure if Sayori sees the full picture of my motive here."
        "Then again..."
        "I can't deny that she's part of the reason I joined."
        "Knowing how much this means to her and all..."
        s 1x "Yeah."
        s "And I'm gonna make sure you have lots of fun here, okay?"
        s "That will be my way of thanking you~"
        mc "Alright, I'm going to hold you to that, then."
        s 4r "Yay~!"
        s "Now, you'll read my poem too, right?"
        s 1y "Don't worry, I'm really bad at this."
        s "Ehehe..."
        mc "We'll see about that."
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