#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio
  
import pygame
import datetime

# audio files
eyes = './eyes.mp3'
water = './water.mp3'
physical = './physical.mp3'

eye_exercise_interval = 20
drink_water_interval = 30
physical_exercise_interval = 45

water_to_drink = 3.5

def playAudio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1)
    # while pygame.mixer.music.get_busy(): 
    #     pygame.time.Clock().tick(10)
    # pygame.mixer.music.pause()

def logEvent(event,filename):
    logFilename = f"{filename}_log.txt"
    nowTime = datetime.datetime.now()
    logTime = nowTime.strftime("%m-%d-%Y, %-I:%M:%S %p")
    
    with open(logFilename,'a') as logFile:
        logFile.write(f"[ {logTime} ] - {event}\n")

def get_work_time():
    return datetime.datetime.now().strftime('%H:%M:%S')

def reminder():
    # t = datetime.datetime.now()
    global t
    global water_to_drink

    timeWaitWater = eye_exercise_interval  * 60
    timeWaitEyes = drink_water_interval * 60
    timeWaitExer = physical_exercise_interval * 50
    delta = datetime.datetime.now() -t 
    user_input = ""

    if delta.seconds  == timeWaitWater and water_to_drink != 0 :
        playAudio(water)
        while 1:
            user_input = input("Enter Drank To stop alarm: ")
            if user_input == "Drank":
                pygame.mixer.music.stop()
                water_to_drink -= 0.25
                break
        logEvent('Drank water', 'water')
        
    elif delta.seconds == timeWaitEyes:
        playAudio(eyes)
        while 1:
            user_input = input("Enter EyDone To stop alarm: ")
            if user_input == "EyDone":
                pygame.mixer.music.stop()
                break
        logEvent('Eye Exercise done', 'eyes')

    elif delta.seconds == timeWaitExer:
        playAudio(physical)
        while 1:
            user_input = input("Enter ExDone To stop alarm: ")
            if user_input == "ExDone":
                pygame.mixer.music.stop()
                t = datetime.datetime.now()
                break
        logEvent('Eye Exercise done', 'eyes')
    

work_time = get_work_time()

t = datetime.datetime.now()

while work_time > '09:00:00' and  work_time < '17:00:00' :

    reminder()

    # t = datetime.datetime.now()
    work_time = get_work_time()


