print("""\u001b[31m
 █████╗ ██████╗  ██████╗  █████╗ ███████╗    ███████╗████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔════╝ ██╔══██╗██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
███████║██████╔╝██║  ███╗███████║███████╗    ███████╗   ██║   ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔══██║██╔══██╗██║   ██║██╔══██║╚════██║    ╚════██║   ██║   ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║  ██║██║  ██║╚██████╔╝██║  ██║███████║    ███████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\u001b[0m""")
print("")
print("A Python interactive story by Maarten De Pue")
print("Fair warning: Adult and Horror themes")
print("")
print("Special thanks to my personal nightmares and")
print("that sci-fi horror book I once read as a kid.")
print("--------------------------------------------------------------------------")
input("Press ENTER to start")

print("\nYou slam the button, and alarms start blaring.")
print('Red lights blink and a screen flashes, "CYCLING". Metal groans and your')
print("space suit feels like it inflates as the airlock evacuates all atmosphere.")
print("\nThen, the door opens and you gently, weightlessly glide forwards, into the vast")
print("emptiness of infinite space. You cling on to your ship while your suit's")
print("thruster control boots up, giving you time to survey your target:")
print("\nA tiny space station hangs nearby. Argas Station, a science post with,")
print("presumably at least, 2 scientists inside, forgotten by their bankrupt")
print("company. Instead of being relieved after their one-month shift, they have")
print("been trapped there for 4 years.")
print("\nIt is your job to assess their status, mental condition, and if possible,")
print("bring them both home. Their names are Doctor Verhelst and his intern,")
print("Lisa Anderson.")
print("------------------------------------------------------------------------")
x = input("Press ENTER to head out.")
if x != "":
    print("\nSo basic instructions are a problem already. Gotcha.")
print("\nYour suit has finished booting, and is ready to take you where you want")
print("to go. A small hop, and you are floating in nothingness.")
loc = "approach" # First location
inv = [] # Player inventory
game = True # Game is running and will recycle its locations
junk = ["Overalls","Personal Datapad","Game Computer","Microscope","Toothbrush","Loose Containers"] # junk floating in the central room
arrive = True # Player is arriving at location, will experience first impressions

# DOORS
door = False # Is the front door open?
innerdoor = False # Is the airlock door open?
foodcontainer = False # Was the food container opened?
meddoor = False # Is the Med Bay door open?
pad = False # Is the pad installed on its charger?
poster = False # Was the poster read and the code known?
crypto = False # Was the log read and crypto key downloaded? Is the Science Bay door open?
plants = "maintain" # State of the incubator
curtain = False



while game == True:
# APPROACH
    while loc == "approach":
        print("\nSuspended between your space ship and Argas Station, you contemplate where to go.")
        action = input("\nWhat do you do?\n(Check, Move, Examine Ship, Examine Station, Examine Suit)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        if action.lower() == "examine ship":
            print("\nYou turn and admire your space ship. She ain't much, but damnit, she's yours.")
            print("A bit of a rust bucket, to be honest. But she flies and she gets the job done.")
            print("And so should you.")
        elif action.lower() == "examine station":
            print("\nArgas station is modular. Five smaller rooms surround a central; cylindric hall:")
            print("The mess room, the sleeping quarter, the med bay and the science bay.")
            print("And pointed at you, the airlock. All tiny, even for a space station. Being locked")
            print("in there must have consequences on your mental health...")
        elif action.lower() == "examine suit":
            print("\nYour space suit is relatively new and in decent shape. No leaks, and all the bells")
            print("and whistles you'd expect: Little maneuvering thrusters, enough oxygen to last a day,")
            print("basic tools, you name it. Even something your old suit didn't have: A piece of velcro")
            print("stuck inside your helmet to scratch your itchy nose.")
            print("They sold you the suit on that feature alone, honestly.")
            if inv.count("Screwdriver") == 0:
                print("\nYou notice that you still have a screwdriver in a pocket from your last repair job. Cool.")
                inv.append("Screwdriver")
        elif action.lower() == "check":
            print("\nYour suit is in good condition and has enough oxygen left.")
            print("The micro-gravity is giving you a slight headache.")
            print("\nYou are carrying the following items:")
            if len(inv) == 0:
                print("Nothing. Nada.")
            else:
                for x in inv:
                    print(x)
        elif action.lower() == "move":
            dir = input("\nWhere do you want to go?\n(Stay, Approach Station)\n\u001b[31m----------------------------------\n>\u001b[0m ")
            if dir.lower() == "stay":
                print("\nYou change your mind.")
            elif dir.lower() == "approach station":
                loc = "door"
                arrive = True
            else:
                print("Yeah no, that's not valid. Try again.")
        else:
            print("Yeah no, that's not valid. Try again.")
# DOOR
    while loc == "door":
        if arrive == True:
            print("\nYou arrive outside the station airlock. All is quiet, no radio chatter coming")
            print("from the space station.")
            arrive = False
        if door == False:
            print("""\nThe round, metal door is shut tight, there are no handles to be found. Only a
tiny window. A terminal beside the door has a screen blinking, "PRESENT KEY".""")
        else:
            print("\nThe station is open to you now, door wide. You can tell that the airlock is damaged")
            print("on the inside, and there is a human body floating there with no helmet on.")
            print("The green screen on the terminal indicates that it is now safe to enter.")
        if "Badge" in inv and door == False:
            print("You realize you have something on you that may function as a key.")
            action = input("\nWhat do you do?\n(Check, Move, Examine Door, Examine Terminal, Present Badge)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        elif inv.count("Badge") == 0 and door == False:
            print("You don't have anything of the sort on you.")
            action = input("\nWhat do you do?\n(Check, Move, Examine Door, Examine Terminal)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        elif "Badge" in inv and door == True:
            action = input("\nWhat do you do?\n(Check, Move, Examine Door, Examine Terminal)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        if action.lower() == "check":
            print("\nYour suit is in good condition and has enough oxygen left.")
            print("The micro-gravity is giving you a slight headache.")
            print("\nYou are carrying the following items:")
            if len(inv) == 0:
                print("Nothing. Nada.")
            else:
                for x in inv:
                    print(x)
        elif action.lower() == "examine door":
            print("""\nThis is a bog standard airlock door. You tried docking your ship to it before but 
the station did not respond to your request. There are no protrusions to speak of.""")
            if door == False:
                print("""Peering through the window, you see the inside of the airlock. Your eyes take a second
to adjust to the dim light, but suddenly you realize there is a silhouette floating
around in there.
A human silhouette. They are not wearing a helmet, and they are not moving.""")
            else:
                print("""It is wide open now, and it appears that the other side of the door is damaged, 
showing clear markings of being struck by a blunt object. Luckily, it seems like the window was spared.""")
        elif action.lower() == "examine terminal":
            print("""\nThis terminal is little more than a small screen, a flat surface underneath,
and the eye of a proximity sensor. The screen only blinks alive if you come close enough.""")
            if "Badge" in inv:
                if door == False:
                    print("The flat surface looks scratched. You are probably supposed to press something against it.")
                    print("Like the badge you found earlier.")
                else:
                    print("The screen flickers green at you, indicating that it is safe to enter the airlock.")
            else:
                print("Odd for a station to have a lock like this. The company seemed concerned about")
                print("corporate espionage.")
        elif action.lower() == "move":
            if door == False:
                dir = input("\nWhere do you want to go?\n(Return to Ship, Station Exterior, Stay)\n\u001b[31m----------------------------------\n>\u001b[0m ")
            else:
                dir = input("\nWhere do you want to go?\n(Return to Ship, Station Exterior, Enter Airlock, Stay)\n\u001b[31m----------------------------------\n>\u001b[0m ")
            if dir.lower() == "return to ship":
                loc = "approach"
                arrive = True
            elif dir.lower() == "station exterior":
                loc = "exterior"
                arrive = True
            elif dir.lower() == "stay":
                print("\nYou turn back around.")
            elif dir.lower() == "enter airlock":
                if door == True:
                    loc = "airlock"
                    arrive = True
                else:
                    print("You bonk your helmet up against the door, breaking the glass.")
                    print("It shatters and you feel the air rush past your face. Your mouth is forced open as your lungs collapse fully. Your vision")
                    print("goes blurry from your bulging eyes. Space is not as cold as you'd expect. At least, not yet. You contemplate this while")
                    print("feeling the spit on your tongue begin to boil as you lose consciousness. You die seconds later, the words ringing in your ears...")
                    print("-That's what you get for trying to break my game...-")
                    loc = "null"
                    game = False
                    action = "null"
            else:
                print("Yeah no, that's not valid. Try again.")
        elif action.lower() == "present badge" or action.lower() == "present key":
            if "Badge" in inv:
                print("""\nYou press your hand, with the badge in a glove pocket, up against the surface of the terminal. 
The screen turns green, and the door immediately begins opening. You realize that anyone inside 
the station will get a warning now, and be aware of your presence.
The door slowly swings outward, presenting you with the inside of the airlock.""")
                door = True
            else:
                print("\nYou realize you are not carrying a key of any kind.")
                print("You look a little stupid for even checking, to be honest.")
        else:
            print("Yeah no, that's not valid. Try again.")
# EXTERIOR
    while loc == "exterior":
        if arrive == True:
            print("""\nSkillfully, you steer yourself around the exterior of the space station. The metal hull
looks pristine as ever, with less damage than one might expect from spending years in deep space.
One hull plate is out of place, however. It is twisted to the side, revealing some electric
circuitry underneath. On the other side of the station, a strange red blob clings to the hull.
There is a second window, on the opposite side from the airlock.""")
            arrive = False
        print("\nYou come to a halt, a dozen meters away from the station. From here, you can see")
        print("the open panel, along with the strange blob and the window on the far side.")
        action = input("\nWhat do you do?\n(Check, Move, Examine Panel, Examine Blob, Examine Window)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        if action.lower() == "move":
            dir = input("\nWhere do you want to go?\n(Return to Ship, Station Door, Stay)\n\u001b[31m----------------------------------\n>\u001b[0m ")
            if dir.lower() == "return to ship":
                loc = "approach"
                arrive = True
            elif dir.lower() == "station door":
                loc = "door"
                arrive = True
            elif dir.lower() == "stay":
                print("\nYou turn back to your vantage point outside the station.")
                loc = "exterior"
            else:
                print("Yeah no, that's not valid. Try again.")
        elif action.lower() == "check":
            print("\nYour suit is in good condition and has enough oxygen left.")
            print("The micro-gravity is giving you a slight headache.")
            print("\nYou are carrying the following items:")
            if len(inv) == 0:
                print("Nothing. Nada.")
            else:
                for x in inv:
                    print(x)
        elif action.lower() == "examine panel":
            print("""\nWho ever opened this panel up, sure did a number on it. The metal is bent, and a
few switches are damaged from blunt force. For a human to have done this, they would need to display
quite a feat of aggression, not what you'd expect from a scientist. 
This could not have been a mere accident, though.""")
        elif action.lower() == "examine window":
            print("""\nYou peer through the window. A few lights are on inside, creating ghostly shadows
with the cloud of items floating around. You recognize a personal datapad, an article of clothing,
a hand-held game computer. No signs of life, however.""")
        elif action.lower() == "examine blob":
            approach = True
            while action.lower() == "examine blob":
                if approach == True:
                    print("""\nYou float over to the strange, figureless clump and examine it up close.
It appears to be made of a blue fabric, and you spot the company logo on it. It is soaked with
a deep red, almost black liquid, which froze solid and mostly sublimated from exposure 
to the vacuum.""")
                    approach = False
                print("\nYou peer closer at this clump of fabric, you think you might be able to")
                print("pry it open.")
                blobaction = input("\nWhat to do you do?\n(Check, Leave, Open Fabric)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                if blobaction.lower() == "check":
                    print("\nYour suit is in good condition and has enough oxygen left.")
                    print("The micro-gravity is giving you a slight headache.")
                    print("\nYou are carrying the following items:")
                    if len(inv) == 0:
                        print("Nothing. Nada.")
                    else:
                        for x in inv:
                            print(x)
                elif blobaction.lower() == "leave":
                    action = "null"
                    print("\nYou turn back, leaving this clump for what it is.")
                elif blobaction.lower() == "open fabric":
                    approach = True
                    while blobaction.lower() == "open fabric":
                        if approach == True:
                            print("""\nYour gloves make it difficult, but you pry the layers of the fabric apart. Tiny crystals of the
liquid caught in the fibers break off and ping your helmet. Layer by layer, you open up the package
until you suddenly realize what is inside.

Out of the clump now protrudes a little foot.""")
                            approach = False
                        print("""\nThis is a baby. It must be so small. Wrapped in a company's overalls and cast into the void of space.
The little leg is frozen solid and has an unusual shape. And it is tiny, even for a newborn.""")
                        if inv.count("Badge") == 0:
                            print("""Right by the leg, in a pocket of the uniform, you can see a RFID badge, again with the company logo.
You could grab it, continue examining the child, or turn away.""")
                            blobaction2 = input("\nWhat do you do?\n(Take Badge, Unwrap Clump, Leave)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                        else: blobaction2 = input("\nWhat do you do?\n(Unwrap Clump, Leave)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                        if blobaction2.lower() == "leave":
                            blobaction2 = "null"
                            blobaction = "null"
                            action = "null"
                            print("You turn away quickly.")
                        elif blobaction2.lower() == "take badge":
                            if inv.count("Badge") == 0:
                                inv.append("Badge")
                                print("\nYou take the badge and put it in a glove pocket.")
                            else:
                                print("\nIt would appear you already took that badge.\nThat's weird.")
                        elif blobaction2.lower() == "unwrap clump":
                            print("""\nWith trembling hands, you continue prying the clothing from the little body.
It is even smaller than you thought, and gives you the impression that this was a premature birth.
As the limbs come into view, you can tell that they are misshapen. The joints have grown close to the
torso, making its arms and legs too short. 
But when the head appears, the full extent of the child's handicap becomes clear.

The face is underdeveloped. Where its eyes, nose and mouth should be, there is only a gaping cavity.
The shape of the skull could never have contained a functional brain, and it seems fused to the spine
at a wrong angle.

You realize this is a stillbron child, but you don't know what could have caused this extreme 
growth defect. 

You feel compelled to cover the child in its wrappings again, and need a moment to collect yourself
after doing so.""")
                            blobaction = "open fabric"
                        else:
                            print("Yeah no, that's not valid. Try again.")
                else:
                    print("Yeah no, that's not valid. Try again.")
        else:
                    print("Yeah no, that's not valid. Try again.")
# AIRLOCK
    while loc == "airlock":
        if arrive == True:
            print("""\nYou enter the tiny airlock, gently bumping into the body 
floating here. It shows no reaction, other than drifting gently to the side. 
Something terrible must have happened here, this place is a mess.""")
            arrive = False
        if innerdoor == False:
            print("""\nSparks fly around you from damaged infrastructure. The inside door is closed
and this person hovering here doesn't show any intention to let you in. To top it off, 
the interface terminal is super broken.""")
        else:
            print("""Sparks fly around you from damaged infrastructure. The inside door is open now,
presenting you the inside of Argas Station. You finally made it in. Lights are on inside and items float about,
but to examine them from up close you'd have to go further inside.""")
        action = input("\nWhat do you do?\n(Check, Move, Examine Body, Examine Airlock, Examine Terminal, Examine Door)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        if action.lower() == "check":
            print("\nYour suit is in good condition and has enough oxygen left.")
            print("The micro-gravity is giving you a slight headache.")
            print("\nYou are carrying the following items:")
            if len(inv) == 0:
                print("Nothing. Nada.")
            else:
                for x in inv:
                    print(x)
        elif action.lower() == "move":
            if innerdoor == False:
                dir = input("Where do you want to go?\n(Exit)\n\u001b[31m----------------------------------\n>\u001b[0m ")
            else:
                dir = input("Where do you want to go?\n(Enter Station, Exit)\n\u001b[31m----------------------------------\n>\u001b[0m ")
            if dir.lower() == "exit":
                loc = "door"
                arrive = True
            if dir.lower() == "enter station":
                loc = "center"
                arrive = True
            else:
                print("Yeah no, that's not valid. Try again.")
        elif action.lower() == "examine body":
            arrive = True
            while action  == "examine body":
                if arrive == True:
                    arrive = False
                    print("""\nYou give the body a gentle nudge and it spins in mid-air, giving you a chance 
to examine it thoroughly.
Its gloves are torn and battered. Perhaps this person was in panic during his last few 
moments? Their space suit seems intact otherwise, until the body turns towards you. 
You can see that the helmet is not fully attached. It seems likely that exposure to 
the vaccuum was their cause of death. The sun shield is down, so you can't see 
the person's face until you remove the helmet.""")
                print("""\nThe dead body continues spinning slowly. You could examine the damage, 
search their pockets, or see what's under the helmet.""")

                    # SEARCHING THE BODY

                bodaction = input("\nWhat do you do?\n(Leave, Examine Damage, Search Pockets, Open Helmet)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                if bodaction.lower() == "leave":
                    bodaction = "Null"
                    action = "Null"
                    print("\nYou stop the body from spinning, and leave them to their business.")
                elif bodaction.lower() == "examine damage":
                    print("""\nYou take a closer look at the gloves. Both the palm and the back are torn, 
but the damage concentrates near the knuckles. Was this person hitting things? Combined with 
the damage in this airlock, it seems likely.""")
                elif bodaction.lower() == "search pockets":
                    print("""\nYou know this brand of space suit, and you know where to find the pockets. 
In a forearm pouch, you find an RFID badge. Upon closer inspection, you see that it is 
identical to the one you already have, so you leave it where it is.

Hastily stuffed in a front pocket, you find a compad. It appears to have been used as a hammer 
or a breaching tool, giving you a hundred reflections of yourself as you stare at 
the shattered screen.
Repairing this would take hours in a specialized shop, if at all possible. You decide to 
put it back, and take it to your ship on your way out.""")
                elif bodaction.lower() == "open helmet":
                    print("""\nYou steel yourself and pry the helmet open. It is fully detached and gives 
with very little resistance.
You immediately recognize Doctor Verhelst, despite the scruffy beard. His handsome face is
contorted in an expression of rage. Teeth clenched, eyes wide. His last moments were spent 
in extreme anger.

Discoloration near his lips tell you that he was alive when exposed to the vaccuum.
It seems very likely that this is what killed him, but who unclasped his helmet 
remains a mystery. The airlock had no pressure when you came in, so if someone else 
did it, they are unlikely to be inside the station as going in would pressurize the lock.
So either his assailant left, or... He did it himself.

Either way, You'll have to take the body with you on the way out. Luckily, your ship has 
a walk-in freezer just for this purpose.

You put the helmet back, you don't like the feeling of being stared at.""")
                else:
                    print("Yeah no, that's not valid. Try again.")
        elif action.lower() == "examine airlock":
            print("""\nThe damage inside the airlock is extensive, and concentrated around the
inner door. Things were torn loose and used to smash other things. Screens shattered, cables
torn out. 
What a mess.""")
        elif action.lower() == "examine door":
            print("""\nLuckily this door is made strong, because someone spared no effort trying to
get inside. Handles are bent, glass is damaged but luckily not broken. 
Through the window, you can see that the lights are on. Random items float 
about. You recognize a personal datapad, some clothing, a hand-held game computer.

None of the emergency handles budge. You notice that they are bent the way 
you want to pull them, suggesting that someone before you tried to do the same 
as you... With a bit more effort.
So it is not the damage that is blocking them, it must be the inside "anti-pirate" 
locking mechanism. Someone there wanted to keep Doctor Verhelst out?

The only way to get this door open, is to convince the computer system that 
you're one of the good guys.""")
        elif action.lower() == "examine terminal":
            arrive = True
            while action.lower() == "examine terminal":
                if arrive == True:
                    print("""\nYou take a closer look at the terminal to see if you can get this thing 
to work. It is in pieces, but after reconnecting the broken screen you find floating nearby
and forcing a reset, you manage to get some life back into the terminal.""")
                print("""You know this security system. It's almost primitive: It requires a 4-digit code.
You get a few tries, after which the system resets.""")
                if "Screwdriver" in inv and innerdoor == False:
                    print("\nYou realize you have a screwdriver somewhere. Maybe you could use that to pry")
                    print("this box apart and short-circuit the authentification chip.")
                    keyaction = input("\nWhat do you do?\n(Leave, Crack Code, Open Terminal)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                elif innerdoor == False:
                        keyaction = input("\nWhat do you do?\n(Leave, Crack Code)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                else:
                    keyaction = input("\nWhat do you do?\n(Leave)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                if keyaction.lower() == "leave":
                    if innerdoor == False:
                        print("\nYou give up like the quitter that you are.")
                    else:
                        print("Feeling victorious, you leave the broken terminal alone.")
                    keyaction = "Null"
                    action = "Null"
                elif keyaction.lower() == "crack code":
                    
                    # CODE CRACKING GAME GOES HERE

                    innerdoor = True
                    action = "null"
                    print("\nCode crackening happens. Your companion greatly approves and promps a declaration of love for you.")
                    print("Romance in games is stupid, the only exception being Judy in Cyberpunk because she's a ")
                    print("relatively well-rounded character.")
                    print("")
                    print("Anyway where were we? Ah yes, the code is cracked. Congrats.")
                    print("""The terminal reacts immediately, flashing green before dying completely, not unlike your
former partner. 
The outer door slams shut and a jet of air hits you in the face, drawing small ice crystals
on the glass of your helmet.

The hiss of equalizing pressure slowly becomes audible as the airlock fills up. The turbulence
jostles you around a bit, before fading out. Computers make a final check, and then the inner
door clangs as bolts are withdrawn.

Slowly, ominously, the door swings open. The space station is finally open to you now.""")
                elif keyaction.lower() == "open terminal":
                    if "Screwdriver" in inv:
                        innerdoor = True
                        action = "null"
                        print("""With some difficulty, you eventually manage to unscrew the front plate and pry apart the
inner housing. Once inside, you have no problem finding the authentication chip.
With a bit of copper wire you pluck from the free-floating debris, you connect pin
4 and 9 like you learned from your former partner. Rest in Peace, James. 

The terminal reacts immediately, flashing green before dying completely, not unlike your
former partner. 
The outer door slams shut and a jet of air hits you in the face, drawing small ice crystals
on the glass of your helmet.

The hiss of equalizing pressure slowly becomes audible as the airlock fills up. The turbulence
jostles you around a bit, before fading out. Computers make a final check, and then the inner
door clangs as bolts are withdrawn.

Slowly, ominously, the door swings open. The space station is finally open to you now.""")
                    else:
                        keyaction = "null"
                        action = "null"
                        dir = "null"
                        loc = "null"
                        game = False
                        print("You put your fingers where they shouldn't be and electrocute yourself. Fan fucking tastic. I hope you're happy.")
                        print("It takes a full 2 minutes for you to die, during which you break your teeth from clenching your jaw,")
                        print('soil yourself in 4 different ways, manage to pray the word "mommy" and deeply contemplate that one time')
                        print("you made a complete fool of yourself in front of your crush.")
                        print("")
                        print("The next rescue crew, infinitely smarter than you and able to finish this game without trying to be")
                        print("a fucking smartass, only finds your charred remains and is left to wonder who could be so fucking stupid.")
                        print("")
                        print("That's you. You are stupid.")
                        print("Like your dad said when you were born,")
                        print('"Better luck next time."')
                else:
                    print("Yeah no, that's not valid. Try again.")
        else:
            print("Yeah no, that's not valid. Try again.")
# CENTER HUB
    while loc == "center":
        if arrive == True:
            arrive = False
            print("""\nYou squeeze yourself through the door and into the central hub area.
Per habit, you press the button beside the airlock door and it closes. The lock
itself stays pressurized. You could probably safely take off your helmet now, but that is considered 
bad form. You never know what might happen during an investigation, and you don't want to be caught 
without protection.

It is eerily quiet here. Even when you call out, you get no response other than the whirring of
autonomous systems.
This place is kept clean by the station robots, but it's still quite a chaos in here.""")
        print("""\nItems float about, blocking your vision somewhat. Electronics, equipment, 
containers loose from their usual fixed position.
A space-Roomba navigates the walls, expertly cleaning every surface it can reach.

There are five exits here, each with their own closed door.""")
        action = input("\nWhat do you do?\n(Check, Move, Examine Doors, Examine Items, Examine Robots)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        if action.lower() == "check":
            print("\nYour suit is in good condition and has enough oxygen left.")
            print("The micro-gravity is giving you a slight headache.")
            print("\nYou are carrying the following items:")
            if len(inv) == 0:
                print("Nothing. Nada.")
            else:
                for x in inv:
                    print(x)
        elif action.lower() == "examine items":
            arrive = True
            look = True
            while action.lower() == "examine items":
                if arrive == True:
                    arrive = False
                    print("""\nTools and equipment of all kinds float about or stick to a wall. It seems that
the cleaning robots don't have tidying up as part of their programming. 

The items themselves are pretty much what you'd expect from a poorly kept science station. You spot about 
a dozen of them: Small lab equipment, personal hygiene products, electronics. It's not like you can step
on them or trip over anything, so letting them float where they are is an easy, albeit unprofessional,
solution.""")
                if look == True:
                    look = False
                    print("\nYou browse through the items drifting past.")
                    print("Among them, you find:\n")
                    for x in junk:
                        print(x)
                print("\nYou scan over the items in the room.")
                print("Not all of these are of interest to you, or are worth taking.")
                print("Is there anything you wish to examine more closely?")
                junkaction = input("\nGive item you want to examine, (Look) or (Leave)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                if junkaction.lower() == "leave":
                    action = "null"
                    print("\nYou leave the items for what they are, and turn your attention to your surroundings.")
                elif junkaction.lower() == "look":
                    look = True
                elif "overalls" in junkaction.lower():
                    print("""\nThese overalls are company standard, like the ones you found outside. Other than the usual
company logo, these also have a nametag: ANDERSON. This is the intern that you're looking for, 
good to know she could still be around.

The pockets are empty, the fabric looks a little dirty. These appear like they have been worn for
a little too long.""")
                elif "game computer" in junkaction.lower():                    # COMPUTER GAME HERE?
                    print("""\nThis little gaming device seems to have been well used, the corners and buttons 
are worn down. One of the buttons is missing, in fact, rendering this console useless.

It still turns on however, playing a little jingle and displaying the title:

    .----. .---.  .--.  .----. .----.                 
    { {__ {_   _}/ {} \ | {}  }{ {__                   
    .-._} } | | /  /\  \| .-. \.-._} }                 
    `----'  `-' `-'  `-'`-' `-'`----'                
    .-. . .-..-. .---. .-. .-. .----. .-. .-. .---.    
    | |/ \| || |{_   _}| {_} |/  {}  \| { } |{_   _}   
    |  .'.  || |  | |  | { } |\  {}  /| {_} |  | |     
    `-'   `-'`-'  `-'  `-' `-' `----' `-----'  `-'     
    .-. .-..-. .-..-.   .-..----. .----..----.         
    |  `| || { } ||  `.'  || {}  }| {_  | {}  }        
    | |\  || {_} || |\ /| || {}  }| {__ | .-. \        
    `-' `-'`-----'`-' ` `-'`----' `----'`-' `-'  by Kevin Crawford    
        
        press "A" to continue.

It just so happens, the A button is missing. Oh, well.
You turn off the computer and let it drift from your hands, the promise of leisure unfulfilled.""")
                elif "microscope" in junkaction.lower():
                    print("""\nThis optical microscope of a prehistoric but still very functional design, is part of any standard
equipment of any laboratory. It is such a status symbol that even social research labs have one, kept on
display like a trophy. 

You bring up the ocular to your eye, clinking it against the glass of your helmet. Good thing nobody saw that.
It does not seem like a good idea to remove your helmet for something this trivial though, so you 
decide against it.

You let the microscope free, and it chooses to waft away from you slowly.

Godspeed, microscope. Godspeed.""")
                elif "toothbrush" in junkaction.lower():
                    print("""\nYou pluck the electric toothbrush from the air and hold it up for examination.
It has been a while since you have seen one of these, most people just use a UV brush. Still, some
claim that it affects their taste and still choose to waste their time physically rubbing their chompers.

This one seems unfit for the job though, the brushes are worn down to the head. You can easily replace them,
but you'd need to have more heads delivered and this station hasn't had a resupply in years.

You release the toothbrush and it floats past a window. The image reminds you of a historical 
domumentary, "2001".""")
                elif "containers" in junkaction.lower():
                    print("""\nThese containers are laced with velcro and belong in specific places against the walls, but
are now floating freely. Some are even open, showing their empty insides.""")
                    if "Cloud of Plastic Food Packets" in junk:
                        print("\nYou feel no ambition to open any of the closed boxes, after that fiasco with the food packets.")
                    else:
                        junk.append("Cloud of Plastic Food Packets")
                        print("""\nYou open a few, they are filled with random junk. One of them feels heaver as you spin it towards you and
when you open it, hundreds of empty food packets come flying out. You quickly close the container but not 
before the room fills with bits of plastic. 

Watching the cloud expand, you secretly hope deep down, that you won't find anyone here on the station so
you won't be made to clean up this mess.

You decide to leave the other boxes alone.""")
                elif "packets" in junkaction.lower() or "plastic" in junkaction.lower() or "food" in junkaction.lower():
                    if "Cloud of Plastic Food Packets" in junk:
                        print("""\nHeavens, what a mess. Hundres of little plastic bags float about and make visibility even worse than
before. Cleaning this up would take forever, so you set your mind to work making up a "It was like this when
I got here" excuse, instead.

You pluck a few of the packets from the air and read their labels. "Graze Dane with Baccon(tm)", 
"Vegetarian Ham and Onvar Peaches", and an off-brand packet that simply reads, "Working Class".""")
                    else:
                        print("\nWhat is this you speak of? I have no idea what you're on about, no sir.")
                elif "datapad" in junkaction.lower():
                    if "Personal Datapad" in junk:
                        inv.append("Datapad")
                        junk.remove("Personal Datapad")
                        print("""\nYou chase after the datapad and catch it from its trajectory. This too looks old and worn as you
turn it in your hands, not to mention quite dated. You find the power button but when you press it,
nothing happens.
It doesn't look broken, though. Perhaps the batteries are just dead?

You pocket the datapad for later. The information on here could prove quite valuable.""")
                    elif "Datapad" in inv:
                        print("\nYou are already carrying the personal datapad. Its batteries are dead.")
                    elif pad == True:
                        print("\nYou left the datapad on its charger in the sleeping quarter.")
                else:
                    print("Yeah no, that's not valid. Try again.")
        elif action.lower() == "examine robots":
            print("""\nSeveral robots are present here, either at work or "asleep" in their dock.
The Wall Roomba probably only ever stops to charge, otherwise biding its time with roaming 
all available surfaces, hunting for any chemical compound out of place.

The technical assistant and medical assistant are asleep in their lockers, awaiting a signal 
from the station that they are needed. The tech bot will wake up from either a technical 
emergency or by request from a human, but med bots usually only come out when there is a 
medical situation. 
The manufacturer made it this way after it was revealed that humans tend to grow addicted to medical attention
if it is available 24/7.""")
        elif action.lower() == "examine doors":
            arrive = True
            while action.lower() == "examine doors":
                if arrive == True:
                    arrive = False
                    print("""\nFive exits lead away from the room where you are in.
Firstly, there is the airlock. The door is closed but you know the lock is pressurized, 
so you can leave that way whenever you feel like.

The glowing labels above the other four doorways confirm what you aready knew from your briefing.
They read:
SLEEPING QUARTER, MED BAY, MESS ROOM, SCIENCE BAY.""")
                print("""\nYou glance over the exits here.
They are all closed, for safety reasons. They each have a small window that you
could check.""")
                dooraction = input("\nGive the door window you want to look through, \nor (Look, Move, Leave)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                if dooraction.lower() == "look":
                    arrive = True
                    print("\nYou regard the doors again.")
                elif dooraction.lower() == "leave":
                    print("\nYou turn your attention elsewhere.")
                    action = "null"
                elif dooraction.lower() == "move":
                    action = "move"
                elif "sleeping" in dooraction.lower():
                    print("""\nYou approach the sleeping quarter door.
Yikes, a bit of a mess in there. First thing you notice are the numerous personal items
hovering about. The beds, which are little more than horizontal sleeping bags, are in
bad shape. 
The hygiene station is hidden behind a panel.""")
                elif "mess" in dooraction.lower():
                    print("""\nYou approach the mess hall door.
The lights are off in there. They couldn't all be broken at once, so this room is probably
not used very much. Lights are generally kept on for safety reasons.
Touching your helmet to the glass, you can make out the blinking red light of a broken 
machine, but not much else.""")
                elif "med" in dooraction.lower():
                    print("""\nYou approach the med bay door.
This is the only room so far that doesn't have random items flying around. Your guess is
that they are plucked from the air by the medbot in the back, like a spider catching flies.

There isn't much to see otherwise, as the entire med station is hidden behind a panel, for
privacy reasons.""")
                elif "science" in dooraction.lower():
                    print("""\n You approach the science bay door. Even before you get there, you can see the light
beaming from the window. This module is from a different manufacturer, secured with a 
combination lock more advanced than the others. Cracking this requires tools you don't 
have on hand...

This room is considerably larger than the others, somewhat matching the central area in size.
It is dominated by the incubator in the center, which is in essence a big tubular light 
source with a tunnel around it. The inside if the tunnel is dotted with little green 
plants, growing towards the central light. The display of color and life is a breath of 
fresh air in this cramped metal box.""")
                else:
                    print("Yeah no, that's not valid. Try again.")
        else:
            if action.lower() != "move":
                print("Yeah no, that's not valid. Try again.")
        if action.lower() == "move":
            while action == "move":
                dir = input("\nWhere do you want to go?\n(Stay, Airlock, Sleeping Quarter, Mess Room, Med Bay, Science Bay)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                if dir.lower() == "stay":
                    print("\nYou change your mind.")
                    action = "null"
                elif dir.lower() == "airlock":
                    loc = "airlock"
                    action = "null"
                    arrive = True
                elif "sleeping" in dir.lower():
                    loc = "sleeping quarter"
                    action = "null"
                    arrive = True
                elif "mess" in dir.lower():
                    loc = "mess room"
                    action = "null"
                    arrive = True
                elif "med" in dir.lower():
                    if meddoor == False:
                        print("\nYou try the door, but it does not react. You try again, same result.")
                        print("The entrance appears to be locked from the other side. That's very")
                        print("unusual.")
                    else:
                        loc = "medbay"
                        action = "null"
                        arrive = True
                elif "science" in dir.lower():
                    if crypto == True:
                        loc = "science bay"
                        action = "null"
                        arrive = True
                    else:
                        print("""\nThis module is from a different manufacturer and the code lock is quite 
unique. Breaking this lock requires tools and expertise you don't have, and it is keeping 
this door closed until you find a way to convince it otherwise.""")
                else:
                    print("Yeah no, that's not valid. Try again.")
# SLEEPING QUARTER
    while loc == "sleeping quarter":
        if arrive == True:
            arrive = False
            if "Cloud of Plastic Food Packets" in junk:
                print("\nGod Damn It, some of those pood packets got with your through the door.")
                print("They're going to end up fucking everywhere.")
            print("""\nYou open the door, swim through the doorway and close it behind you. 
Wow, this bedroom reminds you of your own when you were a teenager. Only without a parent
around to make you clean up. You can't help but feel a sting of shame for the scientists,
they probably never intended for anyone to find their sleeping quarter in this state.

While there is no gravity here, the beds are still organized like bunk beds, in case this
module would be used as part of a station with artificial gravity.
Sleeping bags drift loosely, attached with one point only. They have been robotically cleaned
but are so worn down, that their filling is mostly missing. Sheets dance around you like ghosts.""")
        print("""\nA few screens dot the walls near the beds for entertainment and communications, but most 
screens are broken. The surface around them are specked with pictures and small notes.
The hygiene station, complete with zero-grav toilet sits on the opposite side of the room,
somewhat hidden behind a privacy panel.""")
        if "Datapad" in inv:
            print("""\nThere is a magnetic recharge station here. You could probably use that to charge
the personal datapad you found earlier.""")
            action = input("\nWhat do you do?\n(Check, Move, Examine Beds, Examine Hygiene Station, Charge Datapad)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        elif pad == False:
            action = input("\nWhat do you do?\n(Check, Move, Examine Beds, Examine Hygiene station)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        else:
            action = input("\nWhat do you do?\n(Check, Move, Examine Beds, Examine Hygiene station, Examine Datapad)\n\u001b[31m----------------------------------\n>\u001b[0m ")
        if action.lower() == "check":
            print("\nYour suit is in good condition and has enough oxygen left.")
            print("The micro-gravity is giving you a slight headache.")
            print("\nYou are carrying the following items:")
            if len(inv) == 0:
                print("Nothing. Nada.")
            else:
                for x in inv:
                    print(x)
        elif action.lower() == "move":
            print("\nWhere do you want to go?")
            dir = input("(Stay, Central Hub)\n\u001b[31m----------------------------------\n>\u001b[0m ")
            if dir.lower() == "stay":
                print("\nYou change your mind about leaving.")
            if dir.lower() == "central hub":
                loc = "center"
                arrive = True
            else:
                print("Yeah no, that's not valid. Try again.")
        elif "beds" in action.lower():
            arrive = True
            while action.lower() == "examine beds":
                if arrive == True:
                    arrive = False
                    print("""\nTwo sleeping bags waft towards you. Pressing them aside, you take a closer look at the
two cubicles. Here these two forgotten scientists slept for months, one panel removed from endless
void. 

Each recess is decorated like a shrine, a homage to the life of a person before they were
imprisoned by the endless nothing. Pictures, notes, scribbles and small items are taped
to every surface.""")
                print("""\nYou could invastigate each bed further. The top bunk belongs to intern Lisa Anderson,
while the bottom bunk belongs to Doctor Verhelst.""")
                bedaction = input("\nWhich bed do you want to take a closer look at?\n(Leave, Top, Bottom)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                if bedaction.lower() == "leave":
                    print("\nYou turn away from the beds.") 
                    action = "null"
                elif bedaction.lower() == "bottom":
                    print("""\nThis bed belongs to Doctor Verhelst, the lead scientist of the project. 
It would appear that the Doctor didn't have too many emotional attachments to his home planet.
There are a few photographs to be found, most of which depict him, dressed in academic regalia,
and an elderly woman that looks somewhat like him.
In one shot, they are both smiling from ear to ear as he holds up a diploma. In others, 
he is celebrating with other men and women his age. 
The rest are snapshots of the old woman from before. One of them is hastily scribbled on:
"Miss You"

It is not the only thing that has writing on it. Some notes are chemical formulae or little
reminders, but others clearly show concerning mental issues. 
"WHY DOES SHE LIE", repeated a few times. "Fuck Off" and "Help Us" in varying sizes and colors.
The writing continues off the sticky notes and onto the wall panels.
"Keep It Together" above his own head, a message to himself. And his name, "JAMES VERHELST",
over and over.

The screen of the entertainment unit is completely shattered, but you try to turn it on 
anyway. Sounds of pornographic material blast out the speakers. The volume knob is broken.
In a haste, you turn off the unit and decide to leave the bunk alone.""")
                elif bedaction.lower() == "top":
                    print("""\nThis is Lisa's bed, the intern that joined the project a little later.
She sure loved taking photos, as the bunk is a homage to all the people in her life,
but mostly, perhaps unintentionally, herself.
You could sort them by date and see her grow up from a young teenager, traveling with her family,
to her graduation in a cheap university and even her first few jobs as a lab assistant.
She looks happy in every single one of them.

Furthermore, her diploma hangs suspended in a broken frame, and a few notes with motivational
quotes speck the wall. A few of them, like "Just Stay Fucking Focused" raise a few questions
but you notice nothing too unhinged.

The entertainment unit is in decent shape, except the buttons are broken clean off. Quite
the design flaw, come to think of it.
You decide to leave it as is, and withdraw from the bunk.""")
                else:
                    print("Yeah no, that's not valid. Try again.")
        elif "hygiene" in action.lower():
            print("""\nYou turn the panel and the hygiene station comes into view. The sight of it reminds 
you of your engineer friend who explained, in superlatives, how such a station is easily 
the most expensive thing to make on a standard space station.

Granted, it is well designed. A complicated automaton of hoses and nozzles makes it 
convenient for people with all anatomies to relieve themselves, and the washing station is 
well-adjusted to zero-gravity use. 
Showering would spray water around, so the solution was a combination of making use of 
water's cohesion strength, together with strategic suction nozzles to remove stray water.
Actually that one suction nozzle reminds you of that other engineer friend. You chuckle
as you remember how he limped for days.

Two hoses are missing, but otherwise this station seems intact. You know that the waste 
materials were either recycled or used as fertilizer for the plants in the science bay.
A stroke of luck. You shudder to think what would have happened if a system like this 
would start backing up.

You put the thought out of your mind and turn away.""")
        elif "charge" in action.lower():
# THE DATAPAD IS STUCK TO THE WALL HERE BECAUSE I DON'T KNOW HOW 
# TO CARRY ITS FUNCTIONALITY INTO OTHER ROOMS.
            if "Datapad" in inv:
                inv.remove("Datapad")
                pad = True
                action = "examine datapad"
                print("""\nYou pull up the datapad and hold it up against the charger.
Magnets engage and secure the pad against the wall. After a second, the screen springs
to life.""")
        else:
            if action.lower() != "examine datapad" or pad == False:
                print("Yeah no, that's not valid. Try again.")
        if action.lower() == "examine datapad" and pad == True:
            arrive = True
            while action.lower() == "examine datapad":
                if arrive == True:
                    arrive = False
                    print("""\nThe pad plays a soft jingle as the company logo animates on the screen, booting straight
to its operating system. 
You spend several minutes going through the files. It was used in a strictly professional
manner, full of scientific data and dry notes. The last entries were written a good two
months ago, indicating that the work continued well past the time of their theoretical 
departure. A departure that never came, until today.

Only one file jumps out at you from the rest: An old log entry that was imported by a 
cloud service.""")
                print("""\nYou stare at the screen, and the one single file of interest.""")
                if poster == True:
                    action2 = input("\nWhat do you do?\n(Leave, Open Log, Fix Log 2501)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                else: 
                    action2 = input("\nWhat do you do?\n(Leave, Open Log)\n\u001b[31m----------------------------------\n>\u001b[0m ")
                if action2.lower() == "leave":
                    action = "null"
                    print("""\nAn indicator shows that the pad's battery is broken, so you leave it hanging from its
magnetic charger.""")
                elif "fix" in action2.lower:
                    if poster == True:
                        crypto = True
                        print("""\nUsing the search function, you locate the file easily. It takes some novice level 
trickery to change the file type, before you open the appearing text file.

----------
There is nothing left.
It has been months. Years?
The only thing I know for certain now is that life will never be the same again. But
people have to know.

If you are reading this, pray for us.

We tried to make the best of it, at first. We grew closer even though I could tell 
John's health was declining. His sanity.

We got careless, nothing mattered anymore. I got pregnant. And only then did we 
realize that the med bot was not prepared for that.
We both knew the baby could never survive, but that didn't keep us from hoping. When 
Mindy was born, months before her time, the effects of zero-gravity on a developing
fetus became clear. She lived no longer than mere seconds.

I couldn't bring myself to just... Dispose of her. We wrapped her in a blanket and 
pushed her off into deep space, but...
The gravity of the space station pulled her back. She is on the outside of the hull now.""")
                        input("\nPress ENTER to continue.")
                        print("""\nI think that's when John finally broke. He became violent. Aggressive towards me. I was
sure he would kill me.
So while he was out trying to fix external comms, I locked the hatch. I didn't want to
hurt him, but I was too afraid to let him back in.
I would have let him in if he would just calm down so we could talk, but he wouldn't. 
After destroying the airlock, he opened his helmet in a fit of rage. He did not survive.

I am alone now. Everything is broken. If I could, I would just let go and end it, 
but those damned emergency bots manage to bring me back every time.

I don't want to be saved anymore.
There is nothing left of me. I want to sleep.

Take this log to the authorities. Ungemot execs must pay for what they've done.
May any God out there, fogive our sins, plenty as they are.
----------

This explains a few things. The scientists' mental breakdown was slow and destructive.
You know Doctor Verhelst is dead, but maybe there is a chance to find Anderson after all.
She'd need years of therapy, but maybe she can be saved.
Maybe you could still find some solace for her.
                    
There is a crypto key attached to the file, giving you access to any locked computer
on the station. Using the Near-Field Communication function, you download it into your 
suit computer.""")
                    else:
                        print("\nFix what, you weirdo?")
                elif action2.lower() == "open log":
                    print("""\nYou open the log file.
                
----------
  //    Hello, Marissa!
 ('>
 /rr    I can't believe it!
*\))_   I know, I am so incredibly lucky to be finally working in the field (by which I
mean space) along with Dr Verhalst. The influence of Hawking radiation on plants in
0-G has been really popular in the science community lately, and here I am, little Lisa,
aboard the hype train! Choo, choo!

But don't worry babe, your time will come. Who knows, maybe we can go up into space together
one day! Team Marilisa, tog-DATA CORRUPTED-
----------

It's odd for a pad like this to have its data corrupted. Looks like someone might have 
taken it out into space at some point, or subjected it to EM radiation.
You close the log and search a bit further, but find only data files from the science bay.""")
                else:
                    print("Yeah no, that's not valid. Try again.")
# MESS ROOM
    while loc == "mess room":
        if arrive == True:
            arrive = False
            if messlight == False:
                print("""As the door opens, you are welcomed by pitch darkness. As you float in and your eyes
get a chance to adjust to the light, you get a better feel of the place.

Light pours in through the open door, casting an ominous shape over the rows of containers
lining the walls.""")
            else:
                print("""The light is on, though one of the fixtures flickers in protest.
Now you know why they turned it off in the first place: The glitch is visible all through
the station.""")            
            print("""\nYou won't find a table or chairs here, in the absence of gravity they serve no purpose.
Instead, astronauts can use loops to hook their feet into to hang still, and magnetic catches
to hang their meal from while figuring out the sauce packet.

Hundreds of standard-size containers cover all walls. They arrived here with the mess room 
module, containing vast amounts of spare parts, and years worth of food rations. At least 
the scientists were unlikely to run out of those, or this mission would have been a 
guaranteed double corpse retrieval.

The vaccuum cleaner, essential to any mess room to hoover up stray crumbs and sauce, hangs
crookedly from its attachments, indicating its brokenness to no one with a tiny blinking light.""")
        print("""\nThis room seems seldom used, and for little more than a storage room. 
There are a few boxes missing on one side of the room, with an old-fashioned paper poster
in their place with a university logo on it. It is torn almost completely across.""")
        print("\nWhat do you do?")
        if messlight == True:
            action = input("(Check, Move, Examine Containers, Examine Poster, Turn Off Light)\n\u001b[31m----------------------------------\n> \u001b[0m")
        else:
            action = input("(Check, Move, Examine Containers, Examine Poster, Turn On Light)\n\u001b[31m----------------------------------\n> \u001b[0m")
        if action.lower() == "check":
            print("\nYour suit is in good condition and has enough oxygen left.")
            print("The micro-gravity is giving you a slight headache.")
            print("\nYou are carrying the following items:")
            if len(inv) == 0:
                print("Nothing. Nada.")
            else:
                for x in inv:
                    print(x)
        elif action.lower() == "move":
            dir = input("\nWhere do you want to go?\n(Stay, Central Hub)\n\u001b[31m----------------------------------\n> \u001b[0m")
            if dir.lower() == "stay":
                print("\nYou change your mind and stay in this room.")
            elif dir.lower() == "central hub":
                loc = "center"
            else:
                print("Yeah no, that's not valid. Try again.")
        elif "poster" in action.lower():
            if messlight == False:
                print("""\nYou take a closer look at the poster. Emblazoned in the middle, a lion proudly holds up
a shield, inscribed with all sorts of iconography. A tear streaks through the lion's hind
leg, almost reaching the bottom corner. It separates the university's credo in half, and
even while holding up the loose piece, it is difficult to read it in this dim light.
"Something Something Ramus".

The poster makes for a chilling sight. Not only did someone go through the aggressive motion
of tearing it almost clean in half, but also chose to leave it like this. It projects a
feeling of desparation to you, and of mental dysfunction.
These feelings echo inside you as you leave the poster alone.""")
            else:
                poster = True
                print("""\nYou take a closer look at the poster. Emblazoned in the middle, a lion proudly holds up
a shield, inscribed with all sorts of iconography. The tear in the paper streaks through 
the lion's hind leg, almost reaching the bottom corner.

You hold up the loose corner and read "In Veritate Speramus" under the coat of arms. But,
more intriguingly, you spot black marker ink soaked through the paper.

You fold back the top half of the poster, and uncover scribbling on the other side.
    "IF U READ THIS IT MAY BE TOO LATE
    PPL MUST KNOW WHAT HAPPENED
    FIND 2501.DAT
    CHANGE SUFFIX TO .TXT" """)
            if "Datapad" in inv:
                print("\nCould this be referring to the contents of the datapad you are carrying?")
                print("Or would there be some other data logging device around somewhere?")
            elif pad == True:
                print("\nCould this be referring to the contents of the datapad in the sleeping quarter?")
            else:
                print("\nThere must be a data logging device around somewhere...")
            print("\nYou leave the poster alone, repeating the data number to yourself.")
            print("Two Five Zero One. Two Five Zero One. Two Five...")
            print("You check again.")
            print("...Zero One. Two Five Zero One.")
        elif "container" in action.lower():
            print("""\nVelcro holds containers in place on every wall, including floor and ceiling, if there
was such a thing in zero-g. There must be a few hundred of them. 

They have seals that show if they have been opened or not, and you would guess about
half of them never were. Their labels reveal their content: Mostly food and consumables.
These boxes were in place when the room was attached. If storage runs out, the whole
section is replaced with a new one. For two scientists, a room like this should last
about a decade.""")
            if messlight == True:
                print("""\nYou dare open a few with broken seals, and find them filled with trash and random
items. Things from broken latches to empty food packets. A soldering iron. Some clear
goop that you don't want to identify.""")
            else:
                print("""\nYou open a few of the containers with broken seals, and find them filled with trash
and random items. It is hard to see exactly what they are in this darkness.""")
            if "Little Wooden Doll" in inv:
                print("\nYou close the containers back up and leave them to their boxiness.")
            else:
                inv.append("Little Wooden Doll")
                print("""\nAs you close them up and turn back, a little wooden doll taps against your visor.
"For My Angel", it says on the butt. "From Mom".
You decide to pocket the little doll.""")
        elif "turn on" in action.lower():
            if messlight == False:
                messlight = True
                print("""\nYou switch on the light. Once your eyes adjust, you notice one of the fixtures 
flickering. It's quite obnoxious. This game could have used an epilepsy warning.""")
            else:
                print("\nYou reach for the light switch, before realizing it is already on.")
                print("You're the one who switched it on, remember?")
        elif "turn off" in action.lower():
            if messlight == True:
                messlight = False
                print("""\nYou reach and turn off the light. It's much harder to see properly now, but at least
the flickering stopped.""")
            else: print("""\nYou struggle to find the light switch in the dark. 
Because the light is already off. Make sense?""")
        else:
            print("Yeah no, that's not valid. Try again.")
# SCIENCE BAY
    while loc == "science bay":
        if arrive == True:
            arrive = False
            print("""After activating the NFC on the back of your glove, you hold it up to the keypad. It accepts
your command and unlocks the door for you. 

Floating in, you can tell this module is of a different make than the rest of the station.
Its quality standard is noticably higher, with proper sound dampening and lighter color
schemes.

The room is dominated by the machine in the middle: An incubator, in the shape of a tunnel
with a tube light running through the center. Growing towards that light, neatly arranged
along the inside of the tunnel, little plants sit happily.""")
        print("""\nThe thick walls of the incubator housing the little plants are lined with computer touchscreens. 
A few small gardening tools hang from magnets near them. Aside from a few pieces of trash, 
the room is otherwise empty.""")
        action = input("\nWhat do you do?\n(Check, Move, Examine Incubator, Examine Screens, Examine Tools)\n\u001b[31m----------------------------------\n> \u001b[0m")
        if action.lower() == "check":
            print("\nYour suit is in good condition and has enough oxygen left.")
            print("The micro-gravity is giving you a slight headache.")
            print("\nYou are carrying the following items:")
            if len(inv) == 0:
                print("Nothing. Nada.")
            else:
                for x in inv:
                    print(x)
        elif action.lower() == "move":
            dir = input("\nWhere do you want to go?\n(Stay, Central Hub)\n\u001b[31m----------------------------------\n> \u001b[0m")
            if dir.lower() == "stay":
                print("\nYou change your mind and decide to stay.")
            elif dir.lower == "central hub":
                loc = "center"
                arrive = True
            else:
                print("\nyeah no, that's not valid. Try again.")
        elif "incubator" in action.lower():
            print("""\nDozens, hundreds of little plants surround the central tube light, surrounding you with
green leaves if you put your head inside. They instill a sense of peace in you, a sense 
of hope. They seem blissfully unaware of the destruction and suffering around them,
content with the basics that this incubator provides: Light and sustenance.

You stop yourself from anthropomorphizing further and continue examining the machine. 
Thick walls hide hundreds of small tubes and wires, and the base contains a sewage processing
plant that is connected to the bathroom on the other side of the station. Thank the stars 
that nothing malfunctioned here in all those years.""")
        elif "screens" in action.lower():
            arrive = True
            while "screens" in action.lower():
                if arrive == True:
                    arrive = False
                    print("""\nThe screens spring to life as you approach them.""")
                    print("""\nSensor readings are indicated on a visual rendering of the little plant, from its 
photosynthesis to its root development. Apparently the incubator currently houses Wassilweskija 
plants. You repeat that name ten times fast to see if you can.

It would appear that the cosmic microwave background radiation does indeed have a detrimental
effect on growth, and that the incubator needs to compensate. Interesting.

As you skim through the settings of the machine, you find a few of them that you actually
understand:
"GROW - MAINTAIN - TERMINATE"
and below,
"EMERGENCY POWER CYCLE"

That's odd. 
You don't see a relay in the room powerful enough to cut power safely. But that
would mean the incubator is connected to the main reactor, and cycling would momentarily
cut power for the whole station. 
That can't be very safe, but then again, the flashing button does say "Emergency"...""")
                else:
                    print("""\nThe screens provide you with a wealth of information about the plants, though
you are no botanist and understand very little.

"GROW - MAINTAIN - TERMINATE" are words you get.
"EMERGENCY POWER CYCLE" makes sense too, though you suspect that might affect the whole
of Argas Station...""")
                action2 = input("\nWhat do you do?\n(Look, Leave), Set incubator to (Grow, Maintain, Terminate) or (Cycle Power)\n\u001b[31m----------------------------------\n> \u001b[0m")
                if action2.lower() == "look":
                    print("\nYou read over the screens again.")
                elif action2.lower() == "leave":
                    action = "null"
                    print("\nYou turn away from the screens.")
                elif "grow" in action2.lower():
                    if plants != "grow":
                        plants = "grow"
                        print("""\nYou change the setting. 

The diagram confirms what you already know: This will increase the sustenance flow, causing
the plants to grow. Whether they will kill themselves competing for light or overgrow the
whole room or station, is up to your fantasy.""")
                    else:
                        print("You get an error bleep. The incubator is already set this way.")
                elif "maintain" in action2.lower():
                    if plants != "maintain":
                        plants = "maintain"
                        print("""\nYou change the setting.

The screens show a regulated flow of sustenance to the plants, showing that they will
get just enough to stay as they currently are.""")
                    else:
                        print("You get an error bleep. The incubator is already set this way.")
                elif "terminate" in action2.lower():
                    if plants != "terminate":
                        plants = "terminate"
                        print("""\nYou change the setting.

Parts of the diagram on the screen go black. The sustenance flow is now cut off and you
know that unless you restore it soon, all plants will eventually die.
How you feel about that, it up to you to decide.""")
                    else:
                        print("You get an error bleep. The incubator is already set this way.")
                elif "cycle" in action2.lower():
                    print("""\nYou press the ominous red button. The screen goes completely black, but for a
warning message in the middle.""")
                    action3 = input("\n\u001b[31mARE YOU SURE? (YES/NO)\n----------------------------------\n> \u001b[0m")
                    if action3.lower() == "no":
                        print("""\nYou hit the "NO" square and after a short moment, the screen goes back to normal.""")
                    elif action3.lower() == "yes":
                        action = "null"
                        print("""\nYou press the "YES" on the left and for a brief moment, nothing happens.

Then, with a bang loud enough for you to hear through your helmet, a relay somewhere disengages
and everything goes dark. The incubator, its screens, the lights in the station, all
turn off. 
Even the background noise that your brain had been filtering out, gives way to an endless 
silence, your heartbeat the only audible element left. 

Only now do you realize that, unless the power switches back on automatically, you may
be trapped in this station.
You realize that you are holding your breath.

Just as you turn your head to search for any indication of progress, another bang sounds
and the lights go back on. Light floods the room once again and you hear all sorts of 
devices rebooting.""")
                        if meddoor == False:
                            meddoor = True
                            print("""But one sound you recognize easily: Bolt latches are opening. Somewhere in the station,
a magnetic door lock just opened. 

The med bay was the only door still locked.""")
                    else:
                        print("\nyeah no, that's not valid. Try again.")
                else:
                    print("\nyeah no, that's not valid. Try again.")
        elif "tools" in action.lower():

            print("""\nA big magnet on the side of the incubator holds a set of comically small gardening
tools. They are needed in case a plant needs to be moved with the doll-sized spade or some
leaves need clipping with the universe's smallest shears. """)
            if "Tiny Screwdriver" not in inv:
                inv.append("Tiny Screwdriver")
                print("""\nThere is even a miniature screwdriver among them, you can't for the life of you figure
out what it's good for. You decide to keep it, adding it to the arsenal in your chest
pocket.""")
        else:
            print("\nyeah no, that's not valid. Try again.")
#MED BAY
    while loc == "med bay":
        if arrive == True:
            arrive = False
            print("""\nThe door is open. 
The power outage cycled the magnetic bolts and the lock "forgot" that it was supposed to
stay engaged. This honestly looks like a gross security oversight, but given your situation,
not one you intend to fuss about. 

It is quiet as you enter. The door was locked from the inside, so it's almost certain
someone is in here with you. The eerie silence makes you suspect the worst.
            
This room is impeccably clean compared to the others. You know that, other than the space-
Roomba cleaning the walls, the medbot would also pluck drifing items from the air, as they
could pose a safety hazard during procedures.""")
        print("""\nYou find yourself in a "prep" area, with a hygiene station and a closet 
for the emergency bot, which would activate in case of an emergency. 

The curtain to the operations table is closed, obscuring your view. A note hangs pinned
to it.""")
        action = input("What do you do?\n(Check, Move, Examine Robot, Read Note, Open Curtain)\n\u001b[31m----------------------------------\n> \u001b[0m")
        if action.lower() == "check":
            print("\nYour suit is in good condition and has enough oxygen left.")
            print("The micro-gravity is giving you a slight headache.")
            print("\nYou are carrying the following items:")
            if len(inv) == 0:
                print("Nothing. Nada.")
            else:
                for x in inv:
                    print(x)
        elif action == "Move":
            dir = input("Where do you want to go?\n(Stay, Central Hub)")
            if dir.lower() == "stay":
                print("\nYou change your mind and turn back.")
            elif dir.lower() == "central hub":
                loc = "center"
                arrive = True
        elif "robot" in action.lower():
            print("""\nThe closet sits firmly closed, not made to be opened by anything other than highly specialized
tools. As part of their insurance contract, Ungemot made damn sure these robots, and their
closets, are tamper-proof. 

This robot only comes out in case of emergency, when the station detects failing vitals
in its residents. Many a victim of some accident found themselves waking up on the operations
table, without ever seeing the bot that saved them. 
As a result, they get all sorts of nicknames, like "Guardian Angel" or "Superbot". In this
case, Lisa referred to it as "That Damned Emergency Bot" in her log.

You can only imagine how much you'd hate your saviour if you want nothing more than to
die.""")
        elif "note" in action.lower():
            print("""\nYou float over to the curtain and pluck the note from it.
            
----------
"I have finally been able to hack the medbot enough to convince it to aid me
in what I want most. I am leaving.

Who ever reads this, don't tell my family what happened."
----------

The note is signed "Lisa" and there is a time and date written below. You check your watch, 
it was written... 
Two months ago.
You are two months too late. Or, are you?""")
        elif "curtain" in action.lower():
            print("""\nYou steel yourself, and pull the curtain aside.

Two beautiful blue eyes stare through your visor and into yours. A mouth hangs open in
a silent scream within a grotesque explosion of flesh and skin.

The smiling face on the pictures has transformed into a demonic display of anatomical
symmetry, features completely uncovered, skin folded open and pinned to either side like 
red butterfly wings.

Before you can begin to comprehend, your eyes drift and force the image of a completely
dissected body into your memory cortex. No body part was left untouched, every available
surface cut into with surgical precision, opened, and prepared for display on a vertical
table.

Organs were removed and suspended next to the body, as if you could put them back and
breathe life into this horror again.

As you begin to turn away, you catch a monitor showing you a diagram of the body, as if
the bot  wants to show pride in what it did. But the machine-like repetition of the scene
on the screen isn't what draws your intention, instead it is the word above it:

AUTOPSY MODE

Somehow, Lisa Anderson, intern of Argas Station, had convinced the med bot that she was
already dead, and gave it the order to dissect her for examination...
And it did.
While she was alive.

The station spins around you as the realization hits.""")

            input("\nWhat to you do?\n(Wake Up)\n\u001b[31m----------------------------------\n> \u001b[0m")
            print("""\nYour helmet is off and vomit covers surfaces around you. Judging from the space Roomba
working away, you have been in this position for a good minute. The cramps in your stomach
haven't let up, and your convulsing legs kick through the contents of your stomach floating
freely.

Then, a click beside you. Clear as day now that your helmet is off. The whirring of servos.
From the corner of your eye, you see movement. The robotic arm of the medbot begins to 
move, reaching forward over the table towards you.

You reach for something to pull yourself away, but there is nothing in reach. You are floating
freely, suspended in the air. 

The manipulator claw opens and passes your legs. Even your kicks are feeble without something
to brace against. Just as you are about to cry out for help, well aware that you are the
only person alive within millions of kilometers, the claw closes around the rim of your 
helmet.

The med bot, despite your attempts to stop it, expertly snatches your helmet from the air
and pulls it closer for a quick scan. It is just cleaning up, you realize. Free-floating
objects pose a hazard in here.""")
            input("\nWhat do you do?\n(Take Helmet)\n\u001b[31m----------------------------------\n> \u001b[0m")
            print("""\nThat helmet is your life line.
            
Now that you finallly found your footing, you grab at the helmet without thinking. The
claw, about to put it in a cupboard of sorts, opens immediately and lets you take the
helmet, before folding back into its place.

You close the curtain and exit the med bay, putting on your helmet and checking twice if
it is properly secured. In a daze, you cycle the airlock and evacuate Argas Station.""")
            input("\nWhat do you do?\n(Board Ship)\n\u001b[31m----------------------------------\n> \u001b[0m")
            print("""\nA screen shows Argas Station getting smaller as you accellerate your ship. Artificial
gravity finally pulls the blood from your pounding head. 

So this is the fate the befell the scientists. You wonder how you are going to put this
experience into words for the report. Ungemot will notify their respective families. Lisa's
final wish will not be repected. It only fits her fortune all too well.

Could they ever have suspected? When they entered the station, preparing for their research.
Could they have known that this was possible? How it would end?

As the station disappears from sensor range, the feeling of loneliness comes to rest on
you like the promise of death's cold hand. You think of all the people who met similar
fates, who were never discovered. Who died in the infinite emptiness without the slightest
meaning or consequence. All it takes is a faulty engine.

You cast a glance on your meters.
Maybe... Maybe it's time for a career change.""")
            input("\n(Press ENTER to continue)")
            loc = "null"
            game = False
        else:
                print("Yeah no, that's not valid. Try again.")

print("""\n\n ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
 
 Thank you so much for playing.
 If you know where to find me,
 I appreciate your feedback on
 the story and code.""")