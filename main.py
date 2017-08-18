from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
import ttsIBM as tts
import voice_recognizer as vr
import Wolfram_search as ws
import wiki as wk
from threading import Thread


root = Tk()
root.iconbitmap("res//icon.ico")
root.resizable(FALSE,FALSE)
root.title("Spirit Assistant")
style = ttk.Style()
style.theme_use('winnative')

MicPic = PhotoImage(file="res//micpic.png").subsample(20,20)
ClearPic = PhotoImage(file="res//clearpic.png").subsample(10,10)
SpeakPic = PhotoImage(file="res//speakerpic.png").subsample(10,10)
WikiPic = PhotoImage(file="res//wikipic.png").subsample(10,10)


def thr():
    t1 = Thread(target=query)
    t1.start()


def speakThread():
    t3 = Thread(target=speak)
    t3.start()



def speak():
    text = area.get('1.0', END)
    tts.tts(text)


def listen():
    return vr.voicerecog()


def clear():
    area.delete('1.0',END)


def wikiThread():
    t2 = Thread(target=wikiSearch)
    t2.start()


def wikiSearch():
        txt = area.get('1.0', END)
        clear()
        area.insert('1.0', wk.wiki(txt))



def query():
    input = listen()
    area.insert('1.0', input)
    if input != "Could not understand" and input != "Fail":
        text = area.get('1.0', END)
        answer = ws.wolfsearch(text)
        clear()
        area.insert(INSERT,answer)
        speakThread()


area = scrolledtext.ScrolledText(root, width=35, height=10,wrap=WORD,
                                 background="#62d5fc",font="Helvetica 14")
area.grid(row=0, column=0,columnspan=2)
button = Button(root,text="Speak", bd=0,overrelief="sunken",command=thr,image=MicPic)
button.grid(row=0, column=2,sticky=N)
button1 = Button(root,text="WikiSearch",image=WikiPic,bd=0,overrelief="sunken", command=wikiThread)
button1.grid(row=1, column=0,sticky=W)
button2 = Button(root,text="Read out loud",image=SpeakPic,bd=0,overrelief="sunken", command=speakThread)
button2.grid(row=1, column=1,sticky=W)
button3 = Button(root,text="Clear Entry",image=ClearPic,bd=0,overrelief="sunken", command=clear)
button3.grid(row=1, column=2,sticky=W)

area.focus()
root.mainloop()
