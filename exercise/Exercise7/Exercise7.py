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

def logEvent(event,filename):
    logFilename = f"{filename}_log.txt"
    nowTime = datetime.datetime.now()
    logTime = nowTime.strftime("%m-%d-%Y, %-I:%M:%S %p")
    
    with open(logFilename,'a') as logFile:
        logFile.write(f"[ {logTime} ] - {event}\n")

def get_work_time():
    return datetime.datetime.now().strftime('%H:%M:%S')

def reminder_water():
    global t_water
    global water_to_drink

    timeWaitWater = drink_water_interval  * 60
    delta = datetime.datetime.now() -t_water
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
        t_water = datetime.datetime.now()
        

def remind_eyes():
    global t_eyes
    timeWaitEyes = eye_exercise_interval * 60
    delta = datetime.datetime.now() -t_eyes 

    if delta.seconds == timeWaitEyes:
        playAudio(eyes)
        while 1:
            user_input = input("Enter EyDone To stop alarm: ")
            if user_input == "EyDone":
                pygame.mixer.music.stop()
                break
        logEvent('Eye Exercise done', 'eyes')
        t_eyes = datetime.datetime.now()
    
def remind_physical_exercise():
    global t_physical
    timeWaitExer = physical_exercise_interval * 60
    delta = datetime.datetime.now() - t_physical

    if delta.seconds == timeWaitExer:
        playAudio(physical)
        while 1:
            user_input = input("Enter ExDone To stop alarm: ")
            if user_input == "ExDone":
                pygame.mixer.music.stop()
                t = datetime.datetime.now()
                break
        logEvent('Eye Exercise done', 'eyes')
        t_physical = datetime.datetime.now()


work_time = get_work_time()

t_water = datetime.datetime.now()
t_physical = datetime.datetime.now()
t_eyes = datetime.datetime.now()

while work_time > '09:00:00' and  work_time < '17:00:00' :

    reminder_water()
    remind_eyes()
    remind_physical_exercise()

    work_time = get_work_time()


