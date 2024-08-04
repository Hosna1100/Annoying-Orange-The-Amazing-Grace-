label ch0_main:
    stop music fadeout 2.0
    scene bg kitchen
    $ renpy.movie_cutscene("rottenSmoothie.mp4")
    show orange evil zorder 2 at t21
    o "Hey Apple!"
    show apple mad zorder 2 at h22
    a "What?"
    hide apple
    hide orange
    $ renpy.movie_cutscene("rottenSmoothie_cutscene_noaudio.mp4")
    $ renpy.movie_cutscene("rottenSmoothiecontinue.mp4")
    show apple shocked zorder 2 at t22
    show orange evil zorder 2 at t21
    $ renpy.call_screen("dialog", "Not this time!", ok_action=Return())
    show black:
        alpha 0
        0.10
        linear 0.10 alpha 1
    $ pause(0.20)
    stop music
    play sound "sfx/fall2.ogg"
    "{i}Crash!{/i}"
    play music t8 fadeout 1.0
    scene cg kita
    $ quick_menu = False
    $ pause(0.0)
    $ quick_menu = True
    hide kita
    scene bg kitchen
    show apple shocked zorder 2 at t11
    a "E-eh....."
    show apple closedeyes zorder 2 at t11
    a "Phew!"
    a "That was close!"
    a 1 "And..."
    "I hope he won't show any pessimism toward what I did for him now, which was saving him from that knife."
    show apple kind zorder 2 at f11
    a "Thanks..."
    a "{nw}You saved me from that knife but--"
    mc "why won't we go deal with Orange first?"
    show apple glad zorder 2 at h11
    a "I was going to say that!"
    "we come along Orange to ask him why he wanted to kill Apple."
    show orange normal zorder 3 at t21
    a "Orange..."
    mc "Why did you wanted to kill Apple????"
    show orange sheepish zorder 3 at t21
    o "A-aww....."
    $ quick_menu = False
    show orange closedeyes zorder 3 at f21
    $ pause(0.0)
    $ quick_menu = True
    show orange normal zorder 3 at t21
    o "By the way, why you seem to care about him?"
    show apple normal zorder 2 at t22
    "Apple is quiet."
    "Is he waiting for me to answer Orange's question?"
    $ renpy.call_screen("dialog", "I hope it's not embarassing but I love Apple~", ok_action=Return())
    mc "Emm......"
    mc "..."
    mc "Don't make fun of us for it but I..."
    mc "ok. I love him."
    show apple embarrassed zorder 2 at f22
    play music t7
    mc "What's the matter with that??????"
    show orange sheepish zorder 3 at h21
    o "{nw}No problem with that! it's just--"
    mc "Just what??"
    mc "{nw}I mean that, He"
    mc "{nw}has"
    mc "{nw}to"
    mc "{nw}LIVE!"
    mc "He is important to me!"
    mc "And sorry."
    stop music fadeout 2.0
    show apple sad zorder 2 at t22
    "Apple's blush fades."
    a "For what?"
    a "{nw}You didn't do anything bad and--"
    play music t9
    mc "no, I mean that..."
    mc "It's my fault or better say we humans' fault to treat you fruits like that..."
    mc "By cutting and so on..."
    "All this guilt make tears gather in my eyes."
    mc "We were so selfish!"
    mc "We didn't care about any of y'all feelings..."
    "Evetually, I break down into tears."
    mc "We shouldn't have done that to any of you!"
    mc "Maybe if not all the people around the world would understand what I meant but..."
    mc "Even if not for them then, just for you, Apple..."
    "I wipe my tears."
    mc "Will you forgive me?"
    $ renpy.call_screen("dialog", "Hey! [currentuser]! did you read what I was sheepish about a few dialogs ago?? then, stop eating fruit if you are now and respect fruits instead of cutting them.", ok_action=Return())
    $ renpy.call_screen("dialog", "I know it's a little crazy of me to suggest but I just hate someone's death or suffer so, like Sayori says 'I just want people to be happy!'", ok_action=Return())
    $ renpy.call_screen("dialog", "I mean, like one of the mods title said, 'Time To Be An Epic Hero!'", ok_action=Return())
    a "ow....."
    a "[player]..."
    a "{nw}(Wait! how I know that name?)"
    a "..."
    a "We forgive you but..."
    show apple kind zorder 2 at f22
    a "We've never seen someone pitiful like you to care about us that much..."
    a "Thanks again..."
    mc "..."
    mc "..."
    stop music fadeout 2.0
    play music t6
    show apple normal zorder 2 at h22
    show orange normal zorder 3 at h21
    mc "I'll write a poem!"
    return
