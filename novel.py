#!/usr/bin/python3

import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

print('Good morning. Today is a wonderful day. The sun is shining, the birds are chirping, and you are in space.')
print('Unfortunately, while the day is certainly wonderful, you are in danger of becoming dead in a small amount of time.')
print('Right now, there are several things wrong with the space station you are on, and you have to try and fix them before you become spaced.')
print('As of this moment you are sitting at your desk, with nothing done at the moment, and three things within the station are in need of maintnence.')
print("You can either...")
print("(1) Get up and work on the maintnence of the corrupted CPU")
print("(2) Get up and go work on the pod bay doors")
print("(3) Get up and fix the Altitude Adjustment System")
print("(4) Stay here and play videogames.")
try:
    action = int(input('>>>'))
    if action == 1:
        print('You choose that it is best to get up and work on the corrupted cpu first, as the computer controls most of the ships systems.')
        print("As you get closer to the corrupted computer, you can see that some of the cords have been removed, maybe from you tripping over them last night while sleepwalking.")
        print("you decide that the best course of action is to just plug everything back in, and lo and behold, the computer is back online and fixing some errors.")
        print("With that out of the way, you can either...")
        print("(1) Go and go work on the pod bay doors")
        print("(2) Go and fix the Altitude Adjustment System")
        print("(3) Return to your quarters and play videogames.")
        action = int(input('>>>'))
        if action == 1:
            print("Next up, you go to take care of the pod bay doors.")
            print("While most regular doors are easy to use, relying on regular hinges and stuff, the pod bay doors are a bit more complicated")
            print("In this case the doors open like a camera lens, as to better allow the supply pods to drop  off food and equipment")
            print("Since the doors appear to be locked tight, you choose to simply unlock them. Luckily for you, they unlock fairly easily with a few button presses")
            print("With that out of the way, you can either...")
            print("(1) Go and fix the Altitude Adjustment System")
            print("(2) Return to your quarters and play videogames.")
            action = int(input('>>>'))
            if action == 1:
                print("Now to fix the Altitude Adjustment System...")
                print("While the adjustment system is usually a convoluted mess, it appears that the problem right now seems to be that it is powered off.")
                print("With the simple flip of a button, it is back online.")
                print("It was a rather simple task, a monkey could probably do it...though the monkey would also probably end up hurting itself with one of the many electrical cords hanging from the ceiling.")
                print("With that out of the way, you can spend the rest of your time playing videogames")
            elif action == 2:
                print("You decide to just spend the rest of your time playing videogames.")
                print("Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
                print("You are dead.")
                print("There are no retries")

        elif action == 2:
            print("Now to fix the Altitude Adjustment System...")
            print("While the adjustment system is usually a convoluted mess, it appears that the problem right now seems to be that it is powered off.")
            print("With the simple flip of a button, it is back online.")
            print("It was a rather simple task, a monkey could probably do it...though the monkey would also probably end up hurting itself with one of the many electrical cords hanging from the ceiling.")
            print("With that out of the way, you can either...")
            print("(1) Go and go work on the pod bay doors")
            print("(2) Return to your quarters and play videogames.")
            action = int(input('>>>'))
            if action == 1:
                print("Next up, you go to take care of the pod bay doors.")
                print("While most regular doors are easy to use, relying on regular hinges and stuff, the pod bay doors are a bit more complicated")
                print("In this case the doors open like a camera lens, as to better allow the supply pods to drop  off food and equipment")
                print("Since the doors appear to be locked tight, you choose to simply unlock them. Luckily for you, they unlock fairly easily with a few button presses")
                print("With that out of the way, you can spend the rest of your time playing videogames")
            elif action == 2:
                print("You decide to just spend the rest of your time playing videogames.")
                print("Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
                print("You are dead.")
                print("There are no retries")

        elif action == 3:
            print("You decide to just spend the rest of your time playing videogames.")
            print("Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
            print("You are dead.")
            print("There are no retries")
    elif action == 2:
        print("You choose that it is best to get up and work on the pod bay doors first")
        print("While most regular doors are easy to use, relying on regular hinges and stuff, the pod bay doors are a bit more complicated")
        print( "In this case the doors open like a camera lens, as to better allow the supply pods to drop  off food and equipment")
        print("Since the doors appear to be locked tight, you choose to simply unlock them. Luckily for you, they unlock fairly easily with a few button presses")
        print("With that out of the way, you can either...")
        print("(1) Go and fix the Corrupted CPU")
        print("(2) Go and fix the Altitude Adjustment System")
        print("(3) Return to your quarters and play videogames.")
        action = int(input('>>>'))
        if action == 1:
            print('You choose that it is best to get up and work on the corrupted cpu next.')
            print("As you get closer to the corrupted computer, you can see that some of the cords have been removed, maybe from you tripping over them last night while sleepwalking.")
            print("you decide that the best course of action is to just plug everything back in, and lo and behold, the computer is back online and fixing some errors.")
            print("With that out of the way, you can either...")
            print("(1) Go and fix the Altitude Adjustment System")
            print("(2) Return to your quarters and play videogames.")
            action = int(input('>>>'))

            if action == 1:
                print("Now to fix the Altitude Adjustment System...")
                print("While the adjustment system is usually a convoluted mess, it appears that the problem right now seems to be that it is powered off.")
                print("With the simple flip of a button, it is back online.")
                print("It was a rather simple task, a monkey could probably do it...though the monkey would also probably end up hurting itself with one of the many electrical cords hanging from the ceiling.")
                print("With that out of the way, you can go play videogames")


            elif action == 2:
                print("You decide to just spend the rest of your time playing videogames.")
                print(
                    "Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
                print("You are dead.")
                print("There are no retries")
        elif action == 2:
            print("Now to fix the Altitude Adjustment System...")
            print(
                "While the adjustment system is usually a convoluted mess, it appears that the problem right now seems to be that it is powered off.")
            print("With the simple flip of a button, it is back online.")
            print(
                "It was a rather simple task, a monkey could probably do it...though the monkey would also probably end up hurting itself with one of the many electrical cords hanging from the ceiling.")
            print("With that out of the way, you can either...")
            print("(1) Go and fix the Corrupted CPU")
            print("(2) Return to your quarters and play videogames.")
            action = int(input('>>>'))
            if action == 1:
                print('You choose that it is best to get up and work on the corrupted cpu next.')
                print(
                    "As you get closer to the corrupted computer, you can see that some of the cords have been removed, maybe from you tripping over them last night while sleepwalking.")
                print(
                    "you decide that the best course of action is to just plug everything back in, and lo and behold, the computer is back online and fixing some errors.")
                print("With that out of the way, you can either go back to your room and play videogames")
            elif action ==2:
                print("You decide to just spend the rest of your time playing videogames.")
                print(
                    "Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
                print("You are dead.")
                print("There are no retries")
        elif action  == 3:
            print("You decide to just spend the rest of your time playing videogames.")
            print(
                "Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
            print("You are dead.")
            print("There are no retries")




    elif action == 3:
        print("You decide to fix the Altitude Adjustment System first...")
        print("While the adjustment system is usually a convoluted mess, it appears that the problem right now seems to be that it is powered off.")
        print("With the simple flip of a button, it is back online.")
        print("It was a rather simple task, a monkey could probably do it...though the monkey would also probably end up hurting itself with one of the many electrical cords hanging from the ceiling.")
        print("With that out of the way, you can either...")
        print("(1) Get up and work on the maintnence of the corrupted CPU")
        print("(2) Get up and go work on the pod bay doors")
        print("(3) Stay here and play videogames.")
        action = int(input('>>>'))
        if action == 1:
            print(
                'You choose that it is best to get up and work on the corrupted cpu next, as the computer controls most of the ships systems.')
            print(
                "As you get closer to the corrupted computer, you can see that some of the cords have been removed, maybe from you tripping over them last night while sleepwalking.")
            print(
                "you decide that the best course of action is to just plug everything back in, and lo and behold, the computer is back online and fixing some errors.")
            print("With that out of the way, you can either...")
            print("(1) Go and go work on the pod bay doors")
            print("(2) Return to your quarters and play videogames.")
            action = int(input('>>>'))
            if action == 1:
                print("Next up, you go to take care of the pod bay doors.")
                print(
                    "While most regular doors are easy to use, relying on regular hinges and stuff, the pod bay doors are a bit more complicated")
                print(
                    "In this case the doors open like a camera lens, as to better allow the supply pods to drop  off food and equipment")
                print(
                    "Since the doors appear to be locked tight, you choose to simply unlock them. Luckily for you, they unlock fairly easily with a few button presses")
                print("With that out of the way, you can go back to your quarters and play videogames")


            elif action == 2:
                print("You decide to just spend the rest of your time playing videogames.")
                print(
                    "Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
                print("You are dead.")
                print("There are no retries")
        elif action == 2:
            print("Next up, you go to take care of the pod bay doors.")
            print(
                "While most regular doors are easy to use, relying on regular hinges and stuff, the pod bay doors are a bit more complicated")
            print(
                "In this case the doors open like a camera lens, as to better allow the supply pods to drop  off food and equipment")
            print(
                "Since the doors appear to be locked tight, you choose to simply unlock them. Luckily for you, they unlock fairly easily with a few button presses")
            print("With that out of the way, you can either...")
            print("(1) Get up and work on the maintnence of the corrupted CPU")
            print("(2) Stay here and play videogames.")
            action = int(input('>>>'))

            if action == 1:
                print(
                    'You choose that it is best to get up and work on the corrupted cpu next, as the computer controls most of the ships systems.')
                print(
                    "As you get closer to the corrupted computer, you can see that some of the cords have been removed, maybe from you tripping over them last night while sleepwalking.")
                print(
                    "you decide that the best course of action is to just plug everything back in, and lo and behold, the computer is back online and fixing some errors.")
                print("With that out of the way, you can go back to your quarters and play videogames")
            elif action == 2:
                print("You decide to just spend the rest of your time playing videogames.")
                print(
                    "Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
                print("You are dead.")
                print("There are no retries")
        elif action == 3:
            print("You decide to just spend the rest of your time playing videogames.")
            print(
                "Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
            print("You are dead.")
            print("There are no retries")


    elif action == 4:
        print("You decide to just spend the rest of your time playing videogames.")
        print("Unfortunately for you, the entire ship explodes due to a critical software error not being handled")
        print("You are dead.")
        print("There are no retries")



except ValueError:
    print('You begin to stumble at the surge of alien thoughts, and slowly fall to the ground, hitting your head on the hard metal floor. You are unconciouss, and bleeding. Within Ten minutes, the Station Implodes.')
    print('You are dead.')
    print('There are no retries')