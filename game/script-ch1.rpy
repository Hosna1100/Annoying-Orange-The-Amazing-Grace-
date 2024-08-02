

label ch1_main:
    scene bg desk
    with dissolve_scene_half
    play music t4

    "Writing a poem sounds fun!"
    "Especially, when you are writing poem for cute fruits~"
    mc "{nw}AAAAAaaaaaaAAAA"
    mc "I love Apple!"
    "Oops. that was embarrassing..."
    "I hope they didn't hear my scream."
    scene desk2
    "It's really good that I can spend my time with the one I love."
    "And that is Apple."
    "I even love his name."
    "There's a fact about me: The first English word I've known even when I was born is Apple."
    "It's so easy, isn't it?"
    "Apple seems so adorable~"
    "I'll hug him after sharing my poems with them."
    "I glance at my bag."
    hide desk2
    show desk3 at cgfade
    "{b}APPLE????{/b}"
    scene bg desk
    "He quickly hides when I notice him."
    "Cute fruit~"
    "Anyways, let's head to the kitchen."
    "I hope I'll be able to impress Apple~"

    scene bg kitchen
    with dissolve_scene_half
    show orange glad zorder 3 at f31
    show apple glad zorder 2 at t32
    show pear normal zorder 1 at t33
    o "Hey [player]!"
    mc "Hi again, Orange!"
    "They brought Pear here too?"
    show pear at f33
    p "Orange, is this the human you were referring to?"
    show pear surprised at t33
    show orange happy at hf31
    o "Yeah! it is!"
    "I guess Apple noticed the poem in my hand."
    show orange normal at t31
    show apple at f32
    a "You wrote a poem?"
    show apple glad at t32
    mc "I told you I was going to write a poem! ahaha!"
    show apple normal at f32
    a "So..."

    $ nextscene = str(eval(poemwinner[0][0] + "_appeal" + poemwinner[0] + "_exclusive_"))
    call expression nextscene

    return
