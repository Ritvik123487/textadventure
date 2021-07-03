import time
import sys
import math



for char in """Hello, welcome to this text adventure game
""":
    sys.stdout.write(char)
    time.sleep(0.02)

time.sleep(1)
    
for char in """Please select from the given options
""":
    sys.stdout.write(char)
    time.sleep(0.02)

time.sleep(1)


for char in 'Would you like to be a male or female':
    sys.stdout.write(char)
    time.sleep(0.02)

gender = str(input(' '))

time.sleep(1)

for char in 'What is you name':
    sys.stdout.write(char)
    time.sleep(0.02)

name = str(input(' '))

for char in 'Background Information: You are a ' + gender + ' that is in prison for commiting murder. You have been accused of killing your innocent friend. The judge has sentenced you for life, without even giving you a chance to prove your innocence. You have long waited for the chance to break out of this prison, and now that chance has arrived. The prison warden is currently absent and will continue to be so for the next 5 days. You have resolved to break out in those 5 days.':
    sys.stdout.write(char)
    time.sleep(0.01)



for char in 'Press Enter to continue...':
    sys.stdout.write(char)
    time.sleep(0.02)

e = str(input(' '))


for char in 'Would you like to wake up, or continue sleeping ?':
    sys.stdout.write(char)
    time.sleep(0.02)

d1 = str(input(' '))
         
if d1 == 'wake up':

    for char in 'You get up and walk towards your cell door, during which you wake up your cell mate Sal':
        sys.stdout.write(char)
        time.sleep(0.02)

    for char in 'Will you greet Sal or not ?':
        sys.stdout.write(char)
        time.sleep(0.02)

    greeting = str(input(' '))

    if greeting == 'yes':

        for char in 'Sal says hello back':
            sys.stdout.write(char)
            time.sleep(0.02)

    else:

         for char in 'Sal says hello to you, which you respond to by saying hi':
             sys.stdout.write(char)
             time.sleep(0.02)
    

else:

    for char in 'You wake up one hour later instead':
        sys.stdout.write(char)
        time.sleep(0.02)
    
    for char in 'You get up and walk towards your cell door, during which you wake up your cell mate Sal':
            sys.stdout.write(char)
            time.sleep(0.02)

    for char in 'Will you greet Sal or not ?':
        sys.stdout.write(char)
        time.sleep(0.02)

    greeting = str(input(' '))

    if greeting == 'yes':

        for char in 'Sal says hello back':
            sys.stdout.write(char)
            time.sleep(0.02)

    else:

         for char in 'Sal says hello to you, which you respond to by saying hi':
            sys.stdout.write(char)
            time.sleep(0.02)

for char in 'Sal reminds you that it is breakfast time, thus you get ready for it':
    sys.stdout.write(char)
    time.sleep(0.02)

for char in 'Will you wear a dirty or clean shirt ?':
        sys.stdout.write(char)
        time.sleep(0.02)
            
shirt = str(input(' '))

for char in 'You wore a ' + shirt + ' shirt':
        sys.stdout.write(char)
        time.sleep(0.02)

for char in 'The gaurds open the cell doors and lead you to the cafteria. You notice that there is very little security whe  compared to when the warden is present':
        sys.stdout.write(char)
        time.sleep(0.02)

for char in 'You and Sal both reach the cafeteria and then stand in line for food':
        sys.stdout.write(char)
        time.sleep(0.02)

for char in 'The lunch lady asks you what you would like out of the options: mash potatoes, green peas, and/or bread':
    sys.stdout.write(char)
    time.sleep(0.02)

lunch = str(input(' '))

for char in 'You sit down with a plate of ' + lunch:
    sys.stdout.write(char)
    time.sleep(0.02)

for char in 'Will you talk to the sketchy guy sitting next to you':
    sys.stdout.write(char)
    time.sleep(0.02)

sketchy = str(input(' '))

if sketchy == 'yes':
    
    for char in 'The sketchy guy introduces himself as Sam, and tells you that he is in jail for cracking  bank vaults':
    sys.stdout.write(char)
    time.sleep(0.02)

    for char in 'You introduce yourself, and tell him that you were framed, thus you are in prison':
    sys.stdout.write(char)
    time.sleep(0.02)

else:

    for char in 'You ignore the man sitting next to you. He later introduces himself as Sam, and tells you that he is in jail for cracking  bank vaults. He tells you this, and he wants to make friends in prison':
    sys.stdout.write(char)
    time.sleep(0.02)

    for char in 'You introduce yourself, and tell him that you were framed, thus you are in prison':
    sys.stdout.write(char)
    time.sleep(0.02)

for char in 'You, Sal and Sam get along, and become friends. Sam tells you that you can ask him for any favor if you ever need to. You thank Sam for his generous offer, and then return to your cell since breakfast is over':
    sys.stdout.write(char)
    time.sleep(0.02)


for char in 'You tell Sal about your aspiration to leave the prison in the coming days. He agrees to help however he can':
    sys.stdout.write(char)
    time.sleep(0.02)

for char in 'While sitting on your bed, you begin to think about ways to escape the prison. You think about either fighting your way through everything, or carefully escaping with a plan. Would you like to fight or plan to escape ?':
    sys.stdout.write(char)
    time.sleep(0.02)

plan = str(input(' '))
    
if plan == 'plan':

    for char in 'You have chosen to use a plan to free yourself from prison':
    sys.stdout.write(char)
    time.sleep(0.02)

else:

    for char in 'You have chosen to fight your way to freedom':
    sys.stdout.write(char)
    time.sleep(0.02)

if plan == 'plan':
    

    for char in 'You get out of bed, and tell Sal that you will make a plan for the both of us to get out':
    sys.stdout.write(char)
    time.sleep(0.02)

    for char in 'Sal once again tells you that he will support you':
    sys.stdout.write(char)
    time.sleep(0.02)

    for char in 'You continue to plan your escape':
    sys.stdout.write(char)
    time.sleep(0.02)

    for char in 'Will you use the help of Sam to escape prison':
    sys.stdout.write(char)
    time.sleep(0.02)

    sam = str(input(''))

    #Plan for escape
           
    if sam == 'yes' and 'Yes':
        
        for char in 'You decide that you will escape by sitting in the luandry cart that leaves every Tuesday, which is TODAY !':
            sys.stdout.write(char)
            time.sleep(0.02)

        for char in 'Once it is lunch time, you and Sal meet up with Sam':
            sys.stdout.write(char)
            time.sleep(0.02)
        
        for char in 'You explain to Sam what your plan is, and he agrees to meet you in the laundry room':
            sys.stdout.write(char)
            time.sleep(0.02)
        
        for char in 'Sal asks Sam how he plns to do this, but he decides not to tell. You and Sal just trust him to get to the room':
            sys.stdout.write(char)
            time.sleep(0.02)
        
        for char in 'Near the end of lunch, Sam begins to pick a fight with the guy sitting behind him. This fight begins to draw the attention of the gaurd standing near by':
            sys.stdout.write(char)
            time.sleep(0.02)
        
        interfere = str(input('Do you want to stop Sam or no ? ' ))

        for char in 'Do you want to stop Sam or no ?':
            sys.stdout.write(char)
            time.sleep(0.02)

        interfere = str(input(' '))
                        
        if interfere == 'yes' and 'Yes':
            
            for char in 'You go and get up to stop Sam from fighting, but he pushes you down with a surprising amount of strength':
                sys.stdout.write(char)
                time.sleep(0.02)
            
            for char in 'The gaurd arrives and breaks apart the fight using some violence. He declares that Sam will be sent to the laundry room to do the laundry tody as a punishment for distrubing lunch time':
                sys.stdout.write(char)
                time.sleep(0.02)

            for char in 'The gaurd then dismisses everyone back to their cells':
                sys.stdout.write(char)
                time.sleep(0.02)

        else:
            
            for char in 'The gaurd arrives and breaks apart the fight using some violence. He declares that Sam will be sent to the laundry room to do the laundry tody as a punishment for distrubing lunch time':
                sys.stdout.write(char)
                time.sleep(0.02)

            for char in 'The gaurd then dismisses everyone back to their cells':
                sys.stdout.write(char)
                time.sleep(0.02)

        for char in 'When you arrive at your cell, you and Sal ty to make a plan to meet Sam in the laundry room':
                sys.stdout.write(char)
                time.sleep(0.02)

        for char in 'You decide to start a loud and physical fight between yourselves to get sent to the laundry room as punishment':
            sys.stdout.write(char)
            time.sleep(0.02)

        for char in 'Do you want to hit Sal first ? ':
            sys.stdout.write(char)
            time.sleep(0.02)

        attack = str(input(' '))

        if attack == 'Yes' and 'yes':

            for char in 'You punch Sal and loudly yell':
                sys.stdout.write(char)
                time.sleep(0.02)
                      
        else:

            for char in 'Sal punches you and loudly yell':
                sys.stdout.write(char)
                time.sleep(0.02)

        for char in 'You and Sal continue to fight untill the gaurd arrives and breaks you apart':
            sys.stdout.write(char)
            time.sleep(0.02)
        
        for char in 'He tells you that he will send you outside as a punishment':
            sys.stdout.write(char)
            time.sleep(0.02)
        
        #You can add a part here that asks if you want to hit the gaurd and run to the laundry room
        print('To make the gaurd send you and Sal to the laundry room, you gently say "At least he did not send us to the laundry room, I hate it there"')
        time.sleep(3)
        print('This makes the gaurd change his mind abut the punishment, and thus sends you to the laundry rooom')
        time.sleep(2)
        print('Once you arrive at the laundry room, you see Sal')
        time.sleep(1)
        greet2 = str(input('Will you say hi to Sam or no ? '))
                      
        if greet2 == 'Yes' and 'yes':
            time.sleep(1)
            print('You greet Sam and thank him for meeting you here')

        else:
            time.sleep(1)
            print('You tell Sam that we should do this as fast as possible')

        time.sleep(1)
        print('After everyone settles down, you begin to explain your plan')
        time.sleep(2)
        print('The plan is of the following: Sam is to load the laundry cart when you and Sal are inside. Next he is to leave the cart outside as he is suppoed to do so for the laundry truck to come pick it up. That is when you and Sal escape')
        time.sleep(5)
        print('Everyone agrees with the plan, and it starts to be executed')
        time.sleep(1)
        print('Sam loads the cart as planned, and begins to roll the cart outside')
        time.sleep(2)
        print('At the entrance, there is a surprise inspection. A gaurd comes next to the cart and says he is going to search the cart')
        time.sleep(3)
        attack3 = str(input('Will you jump out and punch the gaurd'))
        if attack3 == 'Yes' and 'yes':
            time.sleep(1)
            print('You suddenly jump out of the cart and punch the gaurd square in the face')
            time.sleep(1)
            print('The gaurd blacks out instantly after the hit')

        else:
            print('Just as the gaurd touches the clothing on the cart, Sam kicks the gaurd hard in the chest, causing the gaurd to black out')
            time.sleep(3)
            print('The gaurd blacks out instantly after the hit')

        time.sleep(1)
        print('Sam rolls the cart outside, and tells you and Sal to get out')
        time.sleep(1)
        print('Once you do so, you thank Sam for his help')
        time.sleep(1)
        print('He tells you it was not a big deal, then goes back inside to get back to his cell. Thus leaving you and Sal outisde near and old truck')
        time.sleep(3)
        print = ('You find and pick up a metal bar that you see leaning against the truck')
        time.sleep(2)
        kill = str(input('Would you like to kill Sal by hitting him with the rod ? '))
        if kill == 'yes' and 'Yes':
            print('You hit Sal with the rod, since you did not want to have any liabilities')
            time.sleep(1)
            print('Sal drops on the ground and tells you that he is afraid to die, and thus you hold him in your arms till he breathes his last')
            time.sleep(1)
            print('You drop Sals limpless body, and get into the truck. You hot wire it and drive towards the gate')
            time.sleep(1)
            print('You notice the gaurd in the watch tower aiming his sniper at your wheels')
            time.sleep(1)
            w = str(input('Do you want to jump out of the truck and make a run for it ?'))

            if w == 'Yes' and 'yes':
                print('You jump out of the truck and make it out of the prison')
                time.sleep(1)
                print('YOU HAVE ESCAPED THE PRISON !')

            else:
                print('The wheels of the trucl are shot down, and the truck crashes into a pile of barrels that were close by')
                time.sleep(1)
                d = str(input('Will you get out of the truck or remian inside ?'))

                if d == 'Get out' and 'get out':
                    print('The moment you get out of the truck, you are shot in the head and die')
                    time.sleep(1)
                    print('YOU HAVE LOST THE GAME')

                else:
                    print('You remain in the truck and get shot in the head by the sniper')
                    time.sleep(1)
                    print('YOU HAVE LOST THE GAME')

        else:
            print('You drop he pole that you were holding in your hand, and tell Sal that the only options to escape are by using the truck or by running on foot')
            time.sleep(1)
            print('Sal tells you that it is your choice to choose what to do, as it was your plan to begin with')
            z = str(input('Do you want to use the truck to escape or will you run on foot'))

            if z == 'Truck' and 'truck' and 'By truck' and 'by truck':
                print('You get in the truck with Sal, who hot wires the truck')
                time.sleep(1)
                print('The gaurds think that you are the laundry people, thus they let you go')
                time.sleep(1)
                print('YOU HAVE ESCAPED THE PRISON !')

            else:
                print('You and Sal make a run for the prison gate, but a gaurd in the watch tower sees you running')
                time.sleep(1)
                print('The gaurd starts to take aim with his sniper')
                time.sleep(1)
                hold = str(input('Will you put Sal in front of you, so that he dies instead of you'))

                if hold == 'yes' and 'Yes':
                    print('You grab Sal and and out him in the way of the sniper and the bullet')
                    time.sleep(1)
                    print('As soon as you do, the sniper takes his shot and kills Sal')
                    time.sleep(1)
                    print('This leaves you enough time run out of the prison')
                    time.sleep(1)
                    print('YOU HAVE ESCAPED THE PRISON !')

                else:
                    print('The sniper takes his shot and kills you, but this gives Sal enought time to escape the prison')
                    time.sleep(1)
                    print('YOU HAVE LOST THE GAME')

                    

  
       
    else:
        #Without the help of Sam for the luandry plan
        print('You chose not to use Sam for your escape plan')
        time.sleep(1)
        print('You tell Sal that you have decided the plan of action')
        time.sleep(2)
        print('You tell him that the plan if to kill the near by gaurds and steal thier uniforms')
        time.sleep(2)
        print('Sal tells you that there are two gaurds approaching the cell as they are going to their weekly check up')
        time.sleep(3)
        fight = str(input('Will you start a fake fight wiht Sal to lure the gaurds inside the cell'))

        if fight == 'Yes' and 'yes':
            print('You pretend to fight Sal by punching him lightly and yelling loudly')

        else:
            print('Sal starts to fake being sick to lure the gaurds')

        time.sleep(1)
        print('All this yelling makes the gaurds come into to the cell')
        time.sleep(1)
        print('Immdiately after they do so, you and Sal attack the gaurds and strip them of thier cloths once they blacked out')
        time.sleep(3)
        print('There are no gaurds monitering the cell camera due to the absence of the prison warden')
        time.sleep(3)
        print('You and Sal out on the unifroms and start to walk out of the prison')
        time.sleep(1)
        print('Once you make it outside, a gaurd asks for your IDs')
        q = str(input('Will you attack the gaurd or check your pockets for the ID ? '))
        
        if q == 'attack' and 'Attack':
            print('You hit the gaurd thus making him black out')
            time.sleep(1)
            print('A sniper sees you amd thus takes aim wiht his gun')
            Sal = str(input('Will put Sal in front of you, so you do not get hit by the bullet'))
             
            if Sal == 'yes' and 'yes':
                print('You grab Sal and and out him in the way of the sniper and the bullet')
                time.sleep(1)
                print('As soon as you do, the sniper takes his shot and kills Sal')
                time.sleep(1)
                print('This leaves you enough time run to a near by truck, which you hot wire')
                time.sleep(2)
                print('Youy then begine to drive the truck towards the prison gate')
                time.sleep(3)
                print('You notice the gaurd in the watch tower aiming his sniper at your wheels')
                time.sleep(1)
                w = str(input('Do you want to jump out of the truck and make a run for it ?'))

                if w == 'Yes' and 'yes':
                    print('You jump out of the truck and make it out of the prison')
                    time.sleep(1)
                    print('YOU HAVE ESCAPED THE PRISON !')

                else:
                    print('The wheels of the trucl are shot down, and the truck crashes into a pile of barrels that were close by')
                    time.sleep(1)
                    d = str(input('Will you get out of the truck or remian inside ?'))

                    if d == 'Get out' and 'get out':
                        print('The moment you get out of the truck, you are shot in the head and die')
                        time.sleep(1)
                        print('YOU HAVE LOST THE GAME')

                    else:
                        print('You remain in the truck and get shot in the head by the sniper')
                        time.sleep(1)
                        print('YOU HAVE LOST THE GAME')
                        
            else:
                print('The sniper takes his shot and kills you, but this gives Sal enought time to escape the prison')
                time.sleep(1)
                print('YOU HAVE LOST THE GAME')
                    

        else:
            print('You check your pocket for your ID card, and hand it to him')
            time.sleep(1)
            print('The gaurd then allows for you and Sal to leave the prison area')
            time.sleep(1)
            print('YOU HAVE ESCAPED THE PRISON')
            
              
else:
    #Fighting plan
    print('You get up and tell Sal that we are going to have to beat some gaurds up to get out of prison')
    time.sleep(3)
    print('Sal tells you that the best way to start the fight would be at lunch time, which happened to start now')
    time.sleep(2)
    print('You and Sal both walk to the lunch room, where you boldly make the announcment to everyone: We do not deserve to be stuck here. Lets beat up these loser gaurds and get the HELL out of here')
    time.sleep(7)
    print('Everyone cheers and agrees with this statement')
    time.sleep(1)
    print('As an answer to your speach, a large man slits the neck of the near by gaurd, which encourages others to start the fight')
    time.sleep(1)
    d = str(input('Will you tell everyone to stop and wait ? '))
            
    if d == 'no' and 'No':
        print('You yell everbody let go and run this place over')

    
    else:
        print('You yell and tell people to stop so that we can attack after a plan is made, but people are too excited to care about what you said')

    time.sleep(3)
    print('The large man rams the door, causing it to fall to the ground')
    time.sleep(2)
    #The starting of the attack
    
    print('This then motivates the others to rush out and begin to attack the gaurds, thus creating an unstopable riot')
    time.sleep(3)
    print('The stationary gaurds are instatly run over by the havoc')
    time.sleep(2)
    y = str(input('Will you begin your plan to escape ? '))

    if y == 'yes' and 'Yes':
        print('You take Sal by the arm, and force him outside, where you begin to dash to the door')
        time.sleep(4)
        print('You rush to the prison door, and then find a truck near by')
        time.sleep(2)
        print('You tell Sal to jump into the truck, which he does so')
        time.sleep(2)
        h = str(input('Will you hotwire the car to start it up ? '))

        if h == 'Yes' and 'yes':
            #Got into the truck
            print('You hotwire the car and start driving towards the prison door')
            time.sleep(2)
            print('You see a sniper aiming at your wheels')
            s = str(input('Will you jump out of the truck ? '))

            if s == 'Yes' and 'yes':
                print('You jump out just as the sniper shoots the truck')
                time.sleep(2)
                print('The truck then crashes, killing Sal in the accident')
                time.sleep(2)
                print('This gives you enough time to escape the prison area')
                time.sleep(2)
                print('YOU HAVE ESCAPED THE PRISON')

            else:
                print('You have chosen not to jump out of the truck')
                time.sleep(2)
                print('Your wheels ar shot, thus you begin to sprial towards your doom')
                time.sleep(2)
                print('When you crash, you realize that you are somehow still alive')
                time.sleep(3)
                print('A gaurd approaches your truck and opnes the door')
                time.sleep(1.5)
                n = str(input('Will you hit the gaurd with the broken stick shift next to you ? '))

                if n == 'yes' and 'Yes':
                    print('You hit the gaurd with the stick and nock him out')
                    time.sleep(2)
                    j = str(input('Will you get out of the truck ? '))

                    if j == 'yes' and 'Yes':
                        print('You get out of the truck and dash for the exit')
                        time.sleep(2)
                        print('YOU HAVE ESCAPED THE PRISON')

                    else:
                        print('The truck blows up, killing you in the explosion')
                        time.sleep(2)
                        print('YOU HAVE LOST THE GAME')
                            
                else:
                    print('You try to explain yourself to the gaurd, but he shoots you')
                    time.sleep(2)
                    print('YOU HAVE LOST THE GAME')
                    
        else:
            #Do not hotwire car
            print('Sal finds the keys in the truck and turns the truck on')
            time.sleep(2)
            print('You see a sniper aiming at your wheels')
            s = str(input('Will you jump out of the truck ? '))

            if s == 'Yes' and 'yes':
                print('You jump out just as the sniper shoots the truck')
                time.sleep(2)
                print('The truck then crashes, killing Sal in the accident')
                time.sleep(2)
                print('This gives you enough time to escape the prison area')
                time.sleep(2)
                print('YOU HAVE ESCAPED THE PRISON')

            else:
                print('You have chosen not to jump out of the truck')
                time.sleep(2)
                print('Your wheels ar shot, thus you begin to sprial towards your doom')
                time.sleep(2)
                print('When you crash, you realize that you are somehow still alive')
                time.sleep(3)
                print('A gaurd approaches your truck and opnes the door')
                time.sleep(1.5)
                n = str(input('Will you hit the gaurd with the broken stick shift next to you ? '))

                if n == 'yes' and 'Yes':
                    print('You hit the gaurd with the stick and nock him out')
                    time.sleep(2)
                    j = str(input('Will you get out of the truck ? '))

                    if j == 'yes' and 'Yes':
                        print('You get out of the truck and dash for the exit')
                        time.sleep(2)
                        print('YOU HAVE ESCAPED THE PRISON')

                    else:
                        print('The truck blows up, killing you in the explosion')
                        time.sleep(2)
                        print('YOU HAVE LOST THE GAME')
                            
                else:
                    print('You try to explain yourself to the gaurd, but he shoots you')
                    time.sleep(2)
                    print('YOU HAVE LOST THE GAME')
        
            
    else:
        #Plan for not running
        print("You take Sal and join in on the fighting")
        time.sleep(2)
        print('As soon as you do, a gaurd notices you from the speech')
        time.sleep(2)
        print('He immdiately shoots you in the heart, out of sheer spite')
        time.sleep(2)
        e = str(input('Will you kill the gaurd with the pole you found near you ? '))

        if e == 'yes' and 'Yes':
            print('You stab the gaurd with the pole, amd die as well from bleeding')
            time.sleep(3.5)
            print('YOU LOSE THE GAME')

        else:
            print('You die from bleeding')
            time.sleep(2)
            print('YOU LOSE THE GAME')
            #End of game

        
                


    

    
    

        
        
    
    
         
