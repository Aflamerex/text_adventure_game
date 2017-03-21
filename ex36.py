# A game to call my own
import random
import sys

in_cthulu_room = True

check_for_second_playthrough_dark = False
check_for_second_playthrough_light = False


global hp
global enemy_hp
chara_hp = 100
hp = 100
enemy_hp = 100
check_calm_mind = False

print "Welcome to my game."
print "It's called the adventures of Lester."
print "enjoy!"

def win_condition():
    hp = 100
    enemy_hp = 100
    for enemy_hp in range(enemy_hp,atck):
        print "Health: %d" % enemy_hp
        print "Your Health: %d" % hp


def fights():
    battling(hp, enemy_hp)




def battling(hp,e_hp):
    global enemy_hp
    print "You encounter something!"
    while enemy_hp > 0:
        if check_calm_mind == True:
            hp += hp/8
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
            enemy_hp = -100

        if enemy_hp <= 0:
            print "You won!"
            if in_cthulu_room == True:
                cthulu_encounter()

        elif chara_hp <= 0:
            dead()

def dead():
    print "Good job dying!"
    quit()

def intro():
    print "You're in a house you don't recognize"
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

def basement():
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
    print "The being is indescribable, you try to speak."
    print "The only sound you're able to make is the sound of your Heavy breathing."
    print "As you continue on your head starts to hurt."
    print "What should you do?"
    print "1.-Calm yourself and continue slowly."
    print "2.-Bear with the pain anc continue with a steady pace."

    choice = raw_input("> ")

    if choice == "1":
        print "Walking slowly relaxes you slightly."
        print "Gained passive: Calm Mind"
        check_calm_mind = True
        cthulu_room_fight()
    elif choice == "2":
        print "Your head hurts so bad."
        print "you can't bear the pain."
        print "took 25 damage!"
        hp -= 25
        cthulu_room_fight()

def cthulu_room_fight():
    print "This corridor seems like it's losing color"
    print "Like the colors are fading."
    print "Then as the colors fade it eventually turned black."
    print "You hear something aproaching."
    print "You can't tell what it is but decide it's best to not find out."
    print "You decide to fight it!"
    fights()

def cthulu_encounter():
    enemy_hp = 10000
    print "After the battle all torches suddenly lighten up."
    print "You see the being that was in the decorations in that room."
    print "Your body is shaking."
    print "Your legs are trembling."
    print "Your mind is unable to comprehend this situation."
    print "The choice is yours fight or flee."
    print """
    1.-FIGHT
    2.-FLEE
    3.-TALK
    4.-NEGOTIATE"""

    choice = raw_input("> ")

    if choice == "fight":
        battling(hp, enemy_hp)
    elif choice == "flee":

def cthulu_run_escenario():
    


if check_for_second_playthrough_dark == False and check_for_second_playthrough_light == False:
    intro()
