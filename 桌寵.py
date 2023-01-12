import pygame
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os
from os import system
import time
import threading
import tkinter.filedialog
pygame.mixer.init()

enter_p=True
time_h = 0
time_m = 0
time_s = 0
num_of_secs = 0
min_sec_format = '00:00'
ct = 0
ctfin = pygame.mixer.Sound(os.path.join('fin.wav'))
lock = 0
added = 0


folder = ''

res = []
num = 0
now_music = ''


def ADD():
    global folder
    global res
    global added
    if added != 0:
        res = []

    try:
        folder = tkinter.filedialog.askdirectory()
        musics = [folder + '\\' + music for music in os.listdir(folder) if music.endswith(('.mp3','.wav','.ogg','.m4a','.flac'))]
        ret = []
        for i in musics:
            ret.append(i.split('\\')[1:])
            res.append(i.replace('\\', '/'))
        var2 = StringVar()
        var2.set(ret)
    finally:
        if not folder:
            return

    global playing
    playing = True
    added = 1


def play():
    if len(res):
        pygame.mixer.init()
        global num
        while playing:
            if not pygame.mixer.music.get_busy():
                nextMusic = res[num]
                pygame.mixer.music.load(nextMusic)
                pygame.mixer.music.play()
                if len(res) - 1 == num:
                    num = 0
                else:
                    num = num + 1
                nextMusic = nextMusic.split('\\')[1:]
            else:
                time.sleep(0.1)


def PLAY():
    global folder

    if not folder:
        try:
            folder = tkinter.filedialog.askdirectory()
            musics = [folder + '\\' + music for music in os.listdir(folder) if music.endswith(('.mp3','.wav'))]
            ret = []
            for i in musics:
                ret.append(i.split('\\')[1:])
                res.append(i.replace('\\', '/'))
            var2 = StringVar()
            var2.set(ret)
        finally:
            return

    global playing
    playing = True
    pygame.mixer.music.unpause()
    t = threading.Thread(target=play)
    t.start()


def NEXT():
    global playing
    palying = False
    pygame.mixer.music.stop()
    global num
    if len(res) == num:
        num = 0

    playing = True
    t = threading.Thread(target=play)
    t.start()


def CLOSE():
    global playing
    palying = False
    time.sleep(0.2)
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass
    root.destroy()

def PREV():
    global playing
    palying = False
    pygame.mixer.music.stop()
    global num
    if num == 0:
        num = len(res) - 2
    elif num == len(res) - 1:
        num -= 2
    else:
        num -= 2

    playing = True
    t = threading.Thread(target=play)
    t.start()

def PAUSE():
    global playing
    playing = False
    pygame.mixer.music.pause()



def countdownT():
    global num_of_secs
    global time_h
    global time_m
    global time_s
    global min_sec_format
    global ct
    ct = 0
    num_of_secs = time_h*3600+time_m*60+time_s
    time_h_entry.config(state='disable')
    time_m_entry.config(state='disable')
    time_s_entry.config(state='disable')
    while num_of_secs>=0:
        m1, s = divmod(num_of_secs, 60)
        h, m2 = divmod(m1, 60)
        if h>0:
            min_sec_format = '{:02d}:{:02d}:{:02d}'.format(h,m2,s)
        else:
            min_sec_format = '{:02d}:{:02d}'.format(m2,s)
        
        L_t.config(text=f'{min_sec_format}')
        time.sleep(0.995)
        num_of_secs -= 1

    if ct == 0:
        ctfin.play()
    global enter_p
    enter_p=True
    L_t.config(text="00:00")
    time_h_entry.config(state='normal')
    time_m_entry.config(state='normal')
    time_s_entry.config(state='normal')
    
def countdown():
    global enter_p
    global time_h
    global time_m
    global time_s
    if time_m_entry.get() == '' and time_s_entry.get() == '' and time_h_entry.get() == '' :
        L_t.config(text='請輸入時間')

    elif enter_p:
        if time_h_entry.get() == '':
            time_h = 0
        else:
            time_h = int(time_h_entry.get())
        
        if time_m_shut_entry.get() == '':
            time_m = 0
        else:
            time_m = int(time_m_shut_entry.get())
        
        if time_s_entry.get() == '':
            time_s = 0
        else:
            time_s = int(time_s_entry.get())
        
        t=threading.Thread(target=countdownT)
        t.start()
        enter_p=False

def validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False

def entry_reset():
    global num_of_secs
    global ct
    ct = 1
    num_of_secs = 0
    time_h_entry.delete(0,"end")
    time_h_entry.config(state='normal')
    time_m_entry.delete(0,"end")
    time_m_entry.config(state='normal')
    time_s_entry.delete(0,"end")
    time_s_entry.config(state='normal')


def NOTET():
    os.system('notepad')
def NOTE():
    Nt=threading.Thread(target=NOTET)
    Nt.start()


def COMPUTERT():
    os.system('calc')
def COMPUTER():
    Ct=threading.Thread(target=COMPUTERT)
    Ct.start()


def MAGNIFYT():
    os.system('magnify')
def MAGNIFY():
    Mt=threading.Thread(target=MAGNIFYT)
    Mt.start()


def PC_SHUTDOWNT():
    if time_h_shut_entry.get() == '':
        time_h = 0
    else:
        time_h = int(time_h_shut_entry.get())
    
    if time_m_shut_entry.get() == '':
        time_m = 0
    else:
        time_m = int(time_m_entry.get())
    
    if time_s_shut_entry.get() == '':
        time_s = 0
    else:
        time_s = int(time_s_shut_entry.get())
    shut_time = time_h*3600 + time_m*60 + time_s
    os.system('shutdown -a')
    os.system('shutdown -s -t {}'.format(shut_time))
def PC_SHUTDOWN():
    Pt=threading.Thread(target=PC_SHUTDOWNT)
    Pt.start()


def REGRETT():
    os.system('shutdown -a')
def REGRET():
    Pt=threading.Thread(target=REGRETT)
    Pt.start()


def CHARMAPT():
    os.system('charmap')
def CHARMAP():
    CHt=threading.Thread(target=CHARMAPT)
    CHt.start()


def nope():
    button_sure.place(x=75,y=-100)
    button_nope.place(x=275,y=-100)
    button_reset.place(x=175,y=-100)
    
    time_h_entry.place(x=w_box*1/3-70,y=-100,width=52, height=30)
    time_m_entry.place(x=w_box*2/3-70,y=-100,width=52, height=30)
    time_s_entry.place(x=w_box*3/3-140,y=-100,width=52, height=30)

    time_h_shut_entry.place(x=65,y=-30,width=52, height=30)
    time_m_shut_entry.place(x=155,y=-30,width=52, height=30)
    time_s_shut_entry.place(x=245,y=-30,width=52, height=30)

    L_h.place(x=400*1/4+50,y=-100)
    L_m.place(x=400*1/4+50,y=-100)
    L_s.place(x=400*3/4+40,y=-100)
    L_t.place(x=137,y=-100)
    
    L_word.place(x=0,y=-33)

def count_show():
    button_sure.place(x=75,y=66)
    button_nope.place(x=275,y=66)
    button_reset.place(x=175,y=66)
    button_sure.config(text='開始',command=countdown)
    button_reset.config(text='重製',command=entry_reset)
    
    time_h_entry.place(x=65,y=0,width=52, height=30)
    time_m_entry.place(x=155,y=0,width=52, height=30)
    time_s_entry.place(x=245,y=0,width=52, height=30)
    
    time_h_shut_entry.place(x=65,y=-30,width=52, height=30)
    time_m_shut_entry.place(x=155,y=-30,width=52, height=30)
    time_s_shut_entry.place(x=245,y=-30,width=52, height=30)
    
    L_h.place(x=115,y=0)
    L_m.place(x=205,y=0)
    L_s.place(x=295,y=0)
    L_t.place(x=-1,y=33)
    L_t.config(text=f"{min_sec_format}")
    
    L_word.place(x=0,y=-33)

def shut_show():
    button_sure.place(x=75,y=66)
    button_nope.place(x=275,y=66)
    button_reset.place(x=155,y=66)
    button_sure.config(text='確定',command=PC_SHUTDOWN)
    button_reset.config(text='取消關機',command=REGRETT)
    
    time_h_entry.place(x=65,y=-30,width=52, height=30)
    time_m_entry.place(x=155,y=-30,width=52, height=30)
    time_s_entry.place(x=245,y=-30,width=52, height=30)
    
    time_h_shut_entry.place(x=65,y=30,width=52, height=30)
    time_m_shut_entry.place(x=155,y=30,width=52, height=30)
    time_s_shut_entry.place(x=245,y=30,width=52, height=30)
    
    L_h.place(x=115,y=30)
    L_m.place(x=205,y=30)
    L_s.place(x=295,y=30)
    L_t.place(x=-1,y=-33)
    
    L_word.place(x=0,y=0)
    L_word.config(text='電腦將於以下時間後關機')



def stay_top_on():
    show_mod.entryconfigure("關閉", state='normal')
    show_mod.entryconfigure("開啟", state='disable')
    root.call('wm', 'attributes', '.', '-topmost', '1')

def stay_top_off():
    show_mod.entryconfigure("開啟", state='normal')
    show_mod.entryconfigure("關閉", state='disable')
    root.call('wm', 'attributes', '.', '-topmost', '0')


def lock_on():
    global lock
    global x,y
    global nx,ny
    global ox,oy
    ox,oy = nx-x,ny-y-100
    lock_mod.entryconfigure("關閉", state='normal')
    lock_mod.entryconfigure("開啟", state='disable')
    lock_mod.entryconfigure("固定在上個位置", state='disable')
    lock = 1

def lock_off():
    global lock
    lock_mod.entryconfigure("開啟", state='normal')
    lock_mod.entryconfigure("關閉", state='disable')
    lock_mod.entryconfigure("固定在上個位置", state='normal')
    lock = 0

def lock_last():
    global ox,oy
    global lock
    root.geometry(f"+{ox}+{oy}")
    lock_mod.entryconfigure("開啟", state='disable')
    lock_mod.entryconfigure("關閉", state='normal')
    lock_mod.entryconfigure("固定在上個位置", state='disable')
    lock = 1


root = tk.Tk()
menu = tk.Menu(root)
root.overrideredirect(True)
root.geometry('400x500+600+300')
root.call('wm', 'attributes', '.', '-topmost', '1')
root.attributes("-transparentcolor", "whitesmoke")

def resize(w,h,w_box,h_box,img):
    f1 = w_box/w
    f2 = h_box/h
    factor = min([f1,f2])
    width = int(w*factor)
    height = int(h*factor)
    return img.resize((width,height),Image.Resampling.LANCZOS)

w_box = 400
h_box = 400

img = Image.open('char.png')
w,h = img.size
img_resized = resize(w,h,w_box,h_box,img)
tk_img = ImageTk.PhotoImage(img_resized)

BG = tk.Label(root,text="",font= ('Helvetica 16'),width=100, height=100
              ,bg="whitesmoke"
              ,anchor="n")
BG.pack()

L = tk.Label(root, image=tk_img, width=w_box, height=h_box
                ,bg="whitesmoke",anchor="s")
L.place(x=0,y=100)


L_word = tk.Label(root,text="測試用文字",font= ('Helvetica 16'),width=33
                , height=1,bg="whitesmoke",anchor="n")

L_h = tk.Label(root,text="時",font= ('Helvetica 16'),width=3
                , height=1,bg="whitesmoke",anchor="n")

L_m = tk.Label(root,text="分",font= ('Helvetica 16'),width=3
                , height=1,bg="whitesmoke",anchor="n")

L_s = tk.Label(root,text="秒",font= ('Helvetica 16'),width=3
                , height=1,bg="whitesmoke",anchor="n")

L_t = tk.Label(root,text=f"{min_sec_format}",font= ('Helvetica 16')
                ,width=33, height=1,bg="whitesmoke",anchor="c")


button_sure = Button(root, text="開始", font=('Arial', 13))
button_nope = Button(root, text="返回", font=('Arial', 13),command=nope)
button_reset = Button(root, text="重製", font=('Arial', 13),command=entry_reset)



vcmd = (root.register(validate), '%P')
time_h_entry = tk.Entry(root, validate='key',font= ('Helvetica 16'), validatecommand=vcmd)
time_m_entry = tk.Entry(root, validate='key',font= ('Helvetica 16'), validatecommand=vcmd)
time_s_entry = tk.Entry(root, validate='key',font= ('Helvetica 16'), validatecommand=vcmd)


time_h_shut_entry = tk.Entry(root, validate='key',font= ('Helvetica 16'), validatecommand=vcmd)
time_m_shut_entry = tk.Entry(root, validate='key',font= ('Helvetica 16'), validatecommand=vcmd)
time_s_shut_entry = tk.Entry(root, validate='key',font= ('Helvetica 16'), validatecommand=vcmd)


m = Menu(root, tearoff = 0)

music_menu = Menu(root, tearoff = 0)

music_menu.add_command(label="加入音樂來源",command=ADD)
music_menu.add_command(label="播放", command=PLAY)
music_menu.add_command(label="暫停", command=PAUSE)
music_menu.add_command(label="上一首",command=PREV)
music_menu.add_command(label="下一首",command=NEXT)


tool_menu = Menu(root, tearoff = 0)
tool_menu.add_command(label="記事本",command=NOTE)
tool_menu.add_command(label="小算盤",command=COMPUTER)
tool_menu.add_command(label="放大鏡",command=MAGNIFY)
tool_menu.add_command(label="字元對應表",command=CHARMAP)


show_mod = Menu(root, tearoff = 0)

show_mod.add_command(label="開啟", command= stay_top_on)
show_mod.add_command(label="關閉", command= stay_top_off)


lock_mod = Menu(root, tearoff = 0)

lock_mod.add_command(label="開啟", command= lock_on)
lock_mod.add_command(label="關閉", command= lock_off)
lock_mod.add_command(label="固定在上個位置",command= lock_last)


m.add_cascade(label='音樂', menu=music_menu)
m.add_cascade(label='小工具', menu=tool_menu)
m.add_cascade(label='保持在上', menu=show_mod)
m.add_cascade(label='固定位置', menu=lock_mod)
m.add_command(label ="倒計時",command=count_show)
m.add_command(label="電腦關機",command=shut_show)
m.add_separator()
m.add_command(label ="退出",command=CLOSE)


def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


def motion(event):
    global x,y
    global nx,ny
    nx, ny = root.winfo_pointerxy()
    x, y = event.x, event.y

def move(event):
    global x,y
    global lock
    global nx,ny
    nx, ny = root.winfo_pointerxy()
    if lock == 0 :
        if y>35:
            root.geometry(f"+{nx-x}+{ny-y-100}")


show_mod.entryconfigure("開啟", state='disable')
lock_mod.entryconfigure("關閉", state='disable')
lock_mod.entryconfigure("固定在上個位置", state='disable')


root.bind('<Motion>', motion)
root.bind('<B1-Motion>',move)
root.bind('<B2-Motion>',move)
L.bind("<Button-3>", do_popup)


mainloop()
