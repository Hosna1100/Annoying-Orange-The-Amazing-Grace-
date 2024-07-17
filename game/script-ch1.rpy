

label ch1_main:
    scene bg desk
    with dissolve_scene_half
    play music t4

    "Writing a poem sounds fun!"
    "Especially, when you are writing poem for two cute fruits~"
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

    $ nextscene = str(eval(poemwinner[0][0] + "_appeal" + poemwinner[0] + "_exclusive_"))
    call expression nextscene

    return