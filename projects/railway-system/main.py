import os
from pydub import AudioSegment
import pandas as pd
from gtts import gTTS

def textToSpeech(text,filename):
    pass


def mergeAudios(audios):
    pass


def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    
    # 1 - Generate Kripya dheyan dijiyee
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export('1_hindi.mp3',format="mp3")

    # 2 is from-city

    # 3 - Generate Se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export('3_hindi.mp3',format="mp3")

    # 4 is via-city

    # 5 - Generate ke raste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export('5_hindi.mp3',format="mp3")
    
    # 6 - is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_hindi.mp3',format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export('9_hindi.mp3',format="mp3")

    # 10 is platform number

    # 11 - generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export('11_hindi.mp3',format="mp3")
    

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)

if __name__ == '__main__':
    print("Generating Skeleton....")
    generateSkeleton()
    print("Now generating Announcement....")
    generateAnnouncement("announce_hindi.xlsx")
    