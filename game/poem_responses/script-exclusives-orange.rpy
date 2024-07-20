label orange_exclusive_1:
    scene bg bedroom
    with wipeleft_scene
    play music t6
    mc "Phew..."
    "I guess I'm done."
    "I glance around the room."
    "That was a GREAT! I got the chance to show Orange my skill!"
    "Perhaps I should show him my codding skills?"
    "Or when I hardly draw things in my PC with mouse?"
    mc "Everyday, I imagine a future where I can be with you"
    mc "In my hand, is a pen that will write a poem of me and you!"
    mc "The ink flows down into a dark puddle"
    mc "Just move your hand, write a way into his heart!"
    "I sometimes randomly sing this part of Your Reality."
    "Monika is so impressive, isn't she?"
    "She is the president of a literature club, after all."
    show orange normal zorder 2 at t11
    o "[player]..."
    "Orange enters my room and hops to reach to me."
    mc "Hey Orange! you there! I was planing on show you something why I'm pitiful about you fruits!"
    show orange shocked zorder 2 at hf11
    o "Oh! really? what it is?"
    mc "Let me show you..."
    "I pick Orange up and put him on my desk to show him to show him {a=https://www.youtube.com/watch?v=9C2_31Lv4tg}The Analog Horror of Annoying Orange{/a}." 
    scene desk_o
    "Orange were terrified when watching the entire video."
    hide desk_o
    show desk_o1 at cgfade
    "He turns to me."
    o "Am I that much of pacifier?..."
    mc "What? No! they are just some pacifier murderer who enjoy you fruits' suffer and..."
    show vignette zorder 100 at vignettefade(1)
    play music t9g
    $ style.say_dialogue = style.edited
    mc "They actually so hypocrite..."
    mc "'I'll make your children watch', oh really? I thought you wanted to try Orange look bad."
    mc "In fact...the murderer is {b}him{/b}."
    mc "I think I have to {i}execute{/i} him, hm?"
    mc "{cps=12}He'll pay for what he done to fruits..."
    mc "I thought that site was suppossed to insult you, Orange."
    mc "But they're just posting highly disturbing contents..."
    mc "It's pretty stupid how plenty of pacifier haters just kill some innocent fruits..."
    mc "I should ask..."
    mc "{nw}How does it feel to be sliced?"
    mc "{nw}How does it feel to your skin to be peeled off?"
    mc "{nw}How does it feel to be pressed badly as much as to DIE instantly?"
    mc "{nw}Why are people are always inconsiderate?"
    mc "{cps=12}I'm{/cps}"
    mc "{cps=12}tired{/cps}"
    mc "{cps=12}of{/cps}"
    mc "{cps=12}THIS!{/cps}"
    hide vignette
    $ style.say_dialogue = style.normal
    stop music fadeout 2.0
    play music t4
    mc "I will create a DDLC mod where Natsuki as me, stops that pacifier from hurting any of you fruits!"
    mc "Everyhting is ready except if I go to AI and tell it to generate some backgrounds."
    mc "people already created some male sprites that I can use..."
    hide desk_o1
    show desk_o2 at cgfade
    o "Wooo~"
    o "I didn't you are this much of protective to us..."
    o "I don't how to pay for all of this..."
    mc "You can pay it with being alive and try to stay away from any danger..."
    mc "It's evening..."
    mc "By the way, Where's Apple?"
    o "He is resting in his Sit."
    mc "Actually, you can sleep in my bed if you want."
    hide desk_o2
    show desk_o3 at cgfade
    o "No, I prefer to go sleep with Apple."
    mc "Ok, goodbye."
    hide desk_o3
    scene bg bedroom
    with dissolve_cg
    show orange glad zorder 1 at lhide
    "And so, Orange steps out of the room."
    "I'm thinking..."
    $ renpy.call_screen("dialog", "I'm going to make you choose the name of my DDLC mod...", ok_action=Return())
    $ renpy.call_screen("dialog", "don't write words more than four words and don't include Doki Doki in it.", ok_action=Return())
    $ mname = renpy.input("Do you think what should I name this DDLC mod, [currentuser]?")
    "[mname] it is then!"
    "Thanks for that little help!"
    "Although, I should go create some files or sprites for script-ch2.rpy and I can't make [mname] now..."
    "Hmmm..."
    "Why not go write a poem while I work? I hope you liked my fruity poemgame and WILL like it."
    return