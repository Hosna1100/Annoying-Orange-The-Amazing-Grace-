label book:
        define narrator = Character(None, kind=nvl)
            show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show expression Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    play music t6r
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {"default": [
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ("mod_assets/FATAL precision.ani", 0, 0),
                                    ]}

    "Irregular heartbeat. Heart palpitations. Arrhythmia."
    "I search and search, eyes scanning everything I can find on their symptoms."
    "What is this? Shortness of breath? Chest pain? Dizziness? No."
    "This is all wrong. Elyssa’s symptoms are nowhere near this simple."
    "I’ve seen it twice now, the screams of pain. Sickeningly pale skin."
    "Vomiting blood."
    "There is no other explanation, other than Reiner’s information was a complete and utter lie."
    "This can’t all be coincidence. It’s not possible."
    "I don’t know how much of this Reiner is behind."
    "But I do know this: There is something horribly wrong with this family."
    "And I accepted the invitation to become a part of it."
    "I can hear Elyssa’s screams through the walls now. I listen helplessly."
    "Reiner said he would be with her shortly. Is he in her room now?"
    "Why is the screaming even louder than before?"
    nvl clear
    jump back