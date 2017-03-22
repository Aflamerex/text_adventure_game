# A game to call my own
from pygame import mixer
import random
import sys

check_for_second_playthrough_light = False
check_for_second_playthrough_dark = False
mixer.init()

def intro():
    global chara_hp
    global enemy_hp
    chara_hp = 100
    enemy_hp = 100
    check_calm_mind = False
    global cthulu_encounter_check
    cthulu_encounter_check = False
    global check_calm_mind
    check_calm_mind = False
    print "You're in a house you don't recognize"
    pause()
    print """
    It seems that it has a basement
    or you could go outside
    1.-Outside
    2.-basement
    """
    choice = raw_input("> ")
    if choice == "1":
        outside()
    elif choice == "2":
        basement()

print "Welcome to my game."
print "It's called the adventures of Lester."
print "enjoy!"

def win_condition():
    hp = 100
    enemy_hp = 100
    for enemy_hp in range(enemy_hp,atck):
        print "Health: %d" % enemy_hp
        print "Your Health: %d" % hp

def BOSSAI():
    global chara_hp
    global enemy_hp
    moves = random.randrange(0,2)
    if moves == 2:
        print "It attacks!"
        enatck = random.randrange(10,250)
        chara_hp -= enatck
        print "it hits you for %d" % enatck
    elif moves == 1:
        print "It attacks!"
        enatck = random.randrange(10,100)
        chara_hp -= enatck
        print "it hits you for %d" % enatck
    elif moves == 0:
        print "It unleashes a furious Attack!"
        enatck = random.randrange(250,500)
        chara_hp -= enatck
        print "it hits you for %d" % enatck

def enemyAI():
    global chara_hp
    global enemy_hp
    moves = random.randrange(0,3)
    if moves == 3:
        print "It attacks!"
        enatck = random.randrange(1,25)
        chara_hp -= enatck
        print "it hits you for %d" % enatck
    elif moves == 2:
        print "It's healing!"
        enatck = random.randrange(0,10)
        enemy_hp += enatck
        print "it heals itself for %d" % enatck
    elif moves == 1:
        print "It attacks!"
        enatck = random.randrange(1,10)
        chara_hp -= enatck
        print "it hits you for %d" % enatck
    elif moves == 0:
        print "It unleashes a furious Attack!"
        enatck = random.randrange(25,50)
        chara_hp -= enatck
        print "it hits you for %d" % enatck

def fights():
    global chara_hp
    global enemy_hp
    battling()

def battling():
    mixer.music.load('music\Alexander Ehlers - Doomed.mp3')
    mixer.music.play()
    global cthulu_encounter_check
    global enemy_hp
    global chara_hp
    print "You encounter something!"
    while enemy_hp > 0:
        if chara_hp <= 0:
            dead()
        if check_calm_mind == True:
            chara_hp += chara_hp/20
        print "Health: %d" % chara_hp
        print "Enemy Health:  %d" % enemy_hp
        print "what're you going to do?"
        print "1.-Attack."
        print "2.-Escape."
        print "3.-Magic."
        print "4.-Flail"

        choice = raw_input("> ")

        if choice == "1":
            print "you attack"
            atck = random.randrange(1,25)
            if atck == 25:
                print "Critical hit! you hit for %d" % atck
            else:
                print "You hit for %d" % atck
            enemy_hp -= atck
        elif choice == "2":
            print "There is no escape."
            print "A block hole emerges from your feet."
            print "it says: \n Coward."
            dead()
        elif choice == "3":
            print "You try to use magic and your hand explodes."
            print "Can't really control it."
            print "It leaves you unable to fight."
            dead()
        elif choice == "4":
            print "Flail is super effective!"
            print "Did 100 damage!"
            enemy_hp -= 100


        if enemy_hp <= 0:
            mixer.music.stop()
            print "You won!"
            if in_cthulu_room == True:
                cthulu_encounter()
            elif cthulu_encounter_check == True:
                endgame_dark()
        elif enemy_hp > 0 and cthulu_encounter_check == True:
            BOSSAI()
        elif enemy_hp > 0:
            enemyAI()

def dead():
    print "Good job dying!"
    print "\nWould you like to try again?"

    choice = raw_input("\n> ")

    if choice == "yes":
        intro()
    else:
        quit()


def basement():
    mixer.music.load('music\Alexander Ehlers - Warped.mp3')
    mixer.music.play(-1)
    print "You enter the basement"
    print "Torches surround you, water drips from the stalagmites above you."
    print "You don't feel safe here."

    choice = raw_input("Continue?\n> ")

    if choice == "yes":
        cavern()
    elif choice == "no":
        intro()

def cavern():
    print "Slowly the basement transform into a cavern."
    print "The torches guide you and you appear to be in the entrance of a room."
    print "However your body trembles as you approach it."

    choice = raw_input("Continue?\n > ")

    if choice == "yes":
        cthulu_room()
    elif choice == "no":
        basement()

def cthulu_room():
    global hp
    print "You are now in a room filled to the brim with decorations of a being."
    print "This being is indescribable, you try to speak..."
    pause()
    print "The only sound you're able to make is the sound of your Heavy breathing."
    print "As you continue on your head starts to hurt."
    pause()
    print "What should you do?"
    print """
        1.-Calm yourself and continue slowly.
        2.-Bear with the pain and continue with a steady pace.
        """

    choice = raw_input("> ")

    if choice == "1":
        print "Walking slowly relaxes you slightly."
        print "Gained passive: Calm Mind"
        pause()
        global check_calm_mind
        check_calm_mind = True
        global in_cthulu_room
        in_cthulu_room = True
        cthulu_room_fight()
    elif choice == "2":
        print "Your head hurts so bad."
        print "you can't bear the pain."
        print "took 25 damage!"
        pause()
        hp -= 25
        global in_cthulu_room
        in_cthulu_room = True
        cthulu_room_fight()

def cthulu_room_fight():
    print "This corridor seems like it's losing color"
    print "Like the colors are fading."
    print "Then as the colors fade it eventually turned black."
    pause()
    print "You hear something aproaching."
    print "You can't tell what it is but decide it's best to not find out."
    print "You decide to fight it!"
    pause()
    fights()

def cthulu_encounter():
    mixer.music.load('music\Alexander Ehlers - Warped.mp3')
    mixer.music.play(-1)
    global enemy_hp
    chara_hp = 200
    enemy_hp = 10000
    global hp
    print "After the battle all torches suddenly lighten up."
    print "You see the being that was in the decorations in that room."
    print "Your body is shaking."
    pause()
    print "Your legs are trembling."
    print "Your mind is unable to comprehend this situation."
    print "The choice is yours fight or flee."
    pause()
    print """
    1.-FIGHT
    2.-FLEE
    3.-TALK
    4.-NEGOTIATE"""

    choice = raw_input("> ")

    if choice == "1":
        global cthulu_encounter_check
        cthulu_encounter_check = True
        in_cthulu_room = False
        battling()
    elif choice == "2":
        chance = random.randrange(0,100)
        if chance > 50:
            print "You run with all your might."
            print "All resistance is futile."
            print "Cthulu flies and tortures you as you run."
            pause()
            print "Your body starts melting."
            print "Only your bones remain, which are being devoured by this strange being."
            pause()
            dead()
        elif chance < 25:
            cthulu_run_escenario()
    elif choice == "3":
        print "You start talking to him."
        print "He apreciates your kindness and bravery."
        print "He ask what do you want to talk about."
        pause()
        print """
        1.-My life.
        2.-What about you?
        """

        choice = raw_input("> ")

        if choice == "1":
            print "He doesn't like your arrogance and slight flamboyance."
            battling(hp, enemy_hp)
        elif choice == "2":
            print "He seems pleased."
            print "He tells you about his adventures."
            pause()
            print "All of them horrify you, but you listen anyway."
            print "After some hours, he bids you farewell."
            pause()
            endgame_dark()

def endgame_dark():
    print "While you go outside the cavern, your head starts ringing."
    print "You hear a voice."
    pause()
    print "It tells you to put your hand up."
    print "you oblige."
    pause()
    print "The skies turn black."
    print "Lightning starts striking your being, but you feel nothing."
    print "You feel...powerfull"
    pause()
    check_for_second_playthrough_dark = True

def pause():
    raw_input("\nPress <enter> to continue\n")

def cthulu_run_escenario():
    print "you have succesfully ran against a being of unimaginable power."
    print "I hope you can tell this story."
    print "Or write a book or something."
    print "What should you do Henry?"



if check_for_second_playthrough_dark == False and check_for_second_playthrough_light == False:
    intro()
