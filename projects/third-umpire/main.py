import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils

stream = cv2.VideoCapture('media/clip.mp4')
flag = True


# Set the dimensions for the canvas 
SET_WIDTH = 650
SET_HEIGHT = 368

def play(speed):
    print(f"Your clicked on play. speed is {speed}")

    global flag
    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        return

    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    if flag:
        canvas.create_text(150,25, fill="yellow",font="Times 27 italic bold",text="Decision pending")
    
    flag = not flag


def pending(decision):
    # display decision pending image
    frame = cv2.cvtColor(cv2.imread("media/pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # wait for 1 second
    time.sleep(1)

    # display sponsor image
    frame = cv2.cvtColor(cv2.imread("media/sponsor.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # wait for 1.5 second
    time.sleep(1.5)

    if decision == "out":
        decisionImg = "media/out.png"
    else:
        decisionImg = 'media/not_out.png'

    # display out/notout image
    frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    

def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print("player is out")


def not_out():
    thread = threading.Thread(target=pending,args=("not out",))
    thread.daemon = 1
    thread.start()
    print("player is out")

    print("player is not out")


if __name__ == '__main__':
    # Tkinter gui starts here
    window = tkinter.Tk()
    window.title("CodeWithHarry Third Umpire Review kit")
    cv_img = cv2.cvtColor(cv2.imread("media/welcome.png"), cv2.COLOR_BGR2RGB)
    canvas  = tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    image_on_canvas = canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
    canvas.pack()

    window.geometry('750x600+252+90')
    

    # Buttons to control Playback
    btn = tkinter.Button(window,width=50,text="<< Previous (fast)",command=partial(play,-25))
    btn.pack()
    
    btn = tkinter.Button(window,width=50,text="<< Previous (slow)",command=partial(play,-2))
    btn.pack()
    
    btn = tkinter.Button(window,width=50,text="Next (fast) >>",command=partial(play,25))
    btn.pack()

    btn = tkinter.Button(window,width=50,text="Next (slow) >>",command=partial(play,2))
    btn.pack()
    
    btn = tkinter.Button(window,width=50,text="Give out",command=out)
    btn.pack()
    
    btn = tkinter.Button(window,width=50,text="Give not out",command=not_out)
    btn.pack()

    window.mainloop()