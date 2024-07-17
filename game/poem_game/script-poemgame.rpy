## script-poemgame.rpy

# This file contains the code to the DDLC poem game (now improved [finally...])
# Still commented a bit by Terra.

init python: 
     
    full_wordlist = {}

    class PoemWord:
        def __init__(self, o, a):
            self.oPoint = o
            self.aPoint = a
    
    with renpy.file("poem_game/poemwords.txt") as pf:
        for line in pf:
            line = line.decode("utf-8").strip()

            if line == '' or '#' in line:
                continue

            x = line.split(',')

            if len(x) >= 3 and x[1] != '' and x[2] != '':
                full_wordlist[x[0]] = PoemWord(int(x[1]), int(x[2]))

    glitch_word = PoemWord(0, 0)
    monika_word = PoemWord(0, 0)
                
    # This class handles Chibi Movement in a better way
    class ChibiTrans(object):
        def __init__(self):
            self.charTime = renpy.random.random() * 4 + 4
            self.charPos = 0
            self.charOffset = 0
            self.charZoom = 1

        def produce_random(self):
            return renpy.random.random() * 4 + 4

        def reset_trans(self):
            self.charTime = self.produce_random()
            self.charPos = 0
            self.charOffset = 0
            self.charZoom = 1

        def randomPauseTime(self, trans, st, at):
            if st > self.charTime:
                self.charTime = self.produce_random()
                return None
            return 0

        def randomMoveTime(self, trans, st, at):
            if st > .16:
                if self.charPos > 0:
                    self.charPos = renpy.random.randint(-1,0)
                elif self.charPos < 0:
                    self.charPos = renpy.random.randint(0,1)
                else:
                    self.charPos = renpy.random.randint(-1,1)
                if trans.xoffset * self.charPos > 5: self.charPos *= -1
                return None
            if self.charPos > 0:
                trans.xzoom = -1
            elif self.charPos < 0:
                trans.xzoom = 1
            trans.xoffset += .16 * 10 * self.charPos
            self.charOffset = trans.xoffset
            self.charZoom = trans.xzoom
            return 0
    
    # This dictionary stores every poemgame character and their points.
    chibis = {}

    # This class supers' ChibiTrans and is used to store poem point data.
    class Chibi(ChibiTrans):
        POEM_DISLIKE_THRESHOLD = 29
        POEM_LIKE_THRESHOLD = 45

        def __init__(self, name):
            if not isinstance(name, str):
                raise Exception("'name' argurment must be a string, not " + type(name))
                
            self.charPointTotal = 0
            self.appeal = 0
            super().__init__()
            chibis[name] = self

        def reset(self):
            self.charPointTotal = 0
            self.reset_trans()

        def add(self, point):
            self.charPointTotal += point
        
        def calculate_appeal(self):
            if self.charPointTotal < self.POEM_DISLIKE_THRESHOLD:
                return -1
            elif self.charPointTotal > self.POEM_LIKE_THRESHOLD:
                self.win = True
                return 1
            return 0

    seen_eyes_this_chapter = False

    # Declare Chibi variables for transforms and points (cept Monika), she only needs to move around.
    chibi_o = Chibi('orange')
    chibi_a = Chibi('apple')

    # Start of the poem game in python
    def poem_game_start():
        played_baa = False
        poemgame_glitch = False

        # Resets points of every character
        for c in chibis:
            chibis[c].reset()
        
        # Makes a copy of the full dictionary for editing purposes.
        wordList = full_wordlist.copy()

        # A way better while loop than Dan did
        progress = 1
        while progress <= 20:
            # This section grabs 10 random words and stores the word in a list.
            random_words = []
            for w in range(10):
                word = random.choice(list(wordList.keys()))
                random_words.append(word)
                # Remove the word once its picked and added from the local copy.
                del wordList[word]

            # Display the poem game
            poemword = renpy.call_screen("poem_test", words=random_words, progress=progress, poemgame_glitch=poemgame_glitch)
            # Checks if the word is in the game and not a unique Act 2-3 bugged word.
            if poemword in full_wordlist:
                t = full_wordlist[poemword]
            else:
                if persistent.playthrough == 2:
                    t = glitch_word
                else:
                    t = monika_word

            # If we are not in a bugged poem game state, do normal stuff, else do buggy stuff
            if not poemgame_glitch:
                if t.glitch: #This conditional controls what happens when the glitch word is selected.
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch], zorder=10)
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    # Act 1
                    if persistent.playthrough == 0:
                        if t.oPoint >= 3:
                            renpy.show("o_sticker hop")
                        if t.aPoint >= 3:
                            renpy.show("a_sticker hop")
                    else:
                        # Act 2
                        if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop") #1/10 chance for Monika's sticker to show.
                        elif t.nPoint > t.yPoint: renpy.show("n_sticker hop") #Since there's just Yuri and Natsuki in Act 2, whoever has the higher value for the word hops.
                        elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                            renpy.show("y_sticker hopg") #"y_sticker_2g.png". 1/100 chance to see it, if we haven't seen it already.
                            persistent.seen_sticker = True
                        elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop") #Yuri's cut arms sticker.
                        else: renpy.show("y_sticker hop")
            else:
                r = random.randint(0, 10) #1/10 chance to hear "baa", one time.
                if r == 0 and not played_baa:
                    renpy.play("gui/sfx/baa.ogg")
                    played_baa = True
                elif r <= 5: renpy.play(gui.activate_sound_glitch)

            # Adds points to the characters and progress by 1.
            chibi_o.charPointTotal += t.oPoint
            chibi_a.charPointTotal += t.aPoint
            progress += 1
    
    # End of the game
    def poem_game_finish():
        # Act 1
        if persistent.playthrough == 0:
            # For chapter 1, add 5 points to whomever we sided with
            if chapter == 1:
                chibis[ch1_choice].charPointTotal += 5

            poemwinner[chapter] = max(chibis, key=lambda c: chibis[c].charPointTotal)
        else:
            # Act 2
            if chibi_n.charPointTotal > chibi_y.charPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"

        # Add appeal point based on poem winner
        chibis[poemwinner[chapter]].appeal += 1

        # Set poem appeal
        o_poemappeal[chapter] = chibi_o.calculate_appeal()
        a_poemappeal[chapter] = chibi_a.calculate_appeal()

        # Poem winner always has appeal 1 (loves poem)
        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

screen poem_test(words, progress, poemgame_glitch):
    default numWords = 20
    
    if progress is not None:
        fixed:
            xpos 810
            
            python:
                if persistent.playthrough == 2 and chapter == 2:
                    pstring = ""
                    for i in range(progress):
                        pstring += "1"
                else:
                    pstring = str(progress)

            text pstring + "/" + str(numWords):
                style "poemgame_text"
                ypos 80

        # Two fixed areas for the two sections of poemgame we have
        fixed:
            xpos 440
            ypos 160

            viewport:
                has vbox
                spacing 56

                for i in range(5):
                    if persistent.playthrough == 3:
                        python:
                            s = list("Monika")
                            for k in range(6): # This gives random corruption effects to the "Monika" words.
                                if random.randint(0, 4) == 0:
                                    s[k] = ' '
                                elif random.randint(0, 4) == 0:
                                    s[k] = random.choice(nonunicode)
                            wordString = "".join(s)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        python:
                            wordString = glitchtext(80) # This gives a chance for a random word in Act 2 to be the glitched word.
                    else:
                        python:
                            wordString = words[i]

                    textbutton wordString:
                        action Return(wordString)
                        text_style "poemgame_text"

        fixed:
            xpos 680
            ypos 160

            viewport:
                has vbox
                spacing 56

                for i in range(5):
                    if persistent.playthrough == 3:
                        python:
                            s = list("Monika")
                            for k in range(6): # This gives random corruption effects to the "Monika" words.
                                if random.randint(0, 4) == 0:
                                    s[k] = ' '
                                elif random.randint(0, 4) == 0:
                                    s[k] = random.choice(nonunicode)
                            wordString = "".join(s)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        python:
                            wordString = glitchtext(80) # This gives a chance for a random word in Act 2 to be the glitched word.
                    else:
                        python:
                            wordString = words[5+i]

                    textbutton wordString:
                        action Return(wordString)
                        text_style "poemgame_text"

label poem(transition=True):
    stop music fadeout 2.0

    if persistent.playthrough == 3: #Takes us to the glitched notebook if we're in Just Monika Mode.
        scene bg notebook-glitch
    else:
        scene bg notebook
    
    if persistent.playthrough == 3: 
        show m_sticker at sticker_mid #Just Monika.
    else:
        if persistent.playthrough == 0:
            show o_sticker at sticker_left 
        show a_sticker at sticker_mid 
        if persistent.playthrough == 2 and chapter == 2:
            show y_sticker_cut at sticker_right #Replace Yuri's sticker with the "cut arms" sticker..
        else:
            show y_sticker at sticker_right #Yuri's sticker
        if persistent.playthrough == 2 and chapter == 2:
            show m_sticker at sticker_m_glitch #Monika's sticker
        
    if transition:
        with dissolve_scene_full

    if persistent.playthrough == 3:
        play music ghostmenu #Change the music in Just Monika.
    else:
        play music t4

    $ config.allow_skipping = False
    $ allow_skipping = False

    if persistent.playthrough == 0 and chapter == 0: #Shows the below dialogue the first time the minigame is played.
        call screen dialog("It's time to write a poem!\n\nPick words you think your favorite fruit\nwill like. Something good might happen with\none of this two who may like your poem the most!", ok_action=Return())
        
    $ poem_game_start()
    $ poem_game_finish()

    # Call the new poem eye scare label if we are in Act 2 and we yet seen eyes
    if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
        call poem_eye_scare

    $ config.allow_skipping = True
    $ allow_skipping = True

    stop music fadeout 2.0
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return

## Scare code moved as it's own label
label poem_eye_scare:
    $ seen_eyes_this_chapter = True
    $ quick_menu = False
    play sound "sfx/eyes.ogg"
    $ persistent.seen_eyes = True
    stop music
    scene black with None
    show bg eyes_move
    pause 1.2
    hide bg eyes_move
    show bg eyes
    pause 0.5
    hide bg eyes
    show bg eyes_move
    pause 1.25
    hide bg eyes with None
    $ quick_menu = True
    return

############ Image definitions start here. #############
image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
        
image bg eyes:
    "images/bg/eyes.png"

image o_sticker:
    "poem_game/poemgame/o_sticker_1.png"
    xoffset chibi_o.charOffset xzoom chibi_o.charZoom
    block:
        function chibi_o.randomPauseTime
        parallel:
            sticker_move_a
        parallel:
            function chibi_o.randomMoveTime
        repeat

image a_sticker:
    "poem_game/poemgame/a_sticker_1.png"
    xoffset chibi_a.charOffset xzoom chibi_a.charZoom
    block:
        function chibi_a.randomPauseTime
        parallel:
            sticker_move_a
        parallel:
            function chibi_a.randomMoveTime
        repeat

image o_sticker hop:
    "poem_game/poemgame/o_sticker_2.png"
    xoffset chibi_o.charOffset xzoom chibi_o.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "o_sticker"

image a_sticker hop:
    "poem_game/poemgame/a_sticker_2.png"
    xoffset chibi_a.charOffset xzoom chibi_a.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "a_sticker"

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
