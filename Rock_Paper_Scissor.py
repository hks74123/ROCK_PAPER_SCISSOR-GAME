from tkinter import *

import random

from tkinter import messagebox

def start(event):
    global scvalue
    global c
    global u
    global written_val1
    global written_val2
    global c_score
    global u_score
    written_val1.set("")
    written_val2.set("")
    c_score=int(c.get())
    u_score=int(u.get())
    t=random.choice(tools)
    scvalue.set("")
    tct=event.widget.cget("text")
    scvalue.set(scvalue.get()+tct)
    if scvalue.get()=='ROCK':
        if t=='ROCK':
            written_val1.set('YOUR CHOICE IS : ROCK')
            written_val2.set('COMPUTER CHOICE IS : ROCK')
            t3=Label(frame2,text=written_val1.get(),fg='red')
            t3.pack()
            t4=Label(frame2,text=written_val2.get(),fg='red')
            t4.pack()
            c.set(c_score)
            u.set(u_score)
            i1.update()
            i2.update()
        elif t=='PAPER':
            written_val1.set('YOUR CHOICE IS : ROCK')
            written_val2.set('COMPUTER CHOICE IS : PAPER')
            t5=Label(frame2,text=written_val1.get(),fg='red')
            t5.pack()
            t6=Label(frame2,text=written_val2.get(),fg='red')
            t6.pack()
            c.set(c_score+1)
            u.set(u_score)
            i1.update()
            i2.update()
        elif t=='SCISSOR':
            written_val1.set('YOUR CHOICE IS : ROCK')
            written_val2.set('COMPUTER CHOICE IS : SCISSOR')
            t7=Label(frame2,text=written_val1.get(),fg='red')
            t7.pack()
            t8=Label(frame2,text=written_val2.get(),fg='red')
            t8.pack()
            c.set(c_score)
            u.set(u_score+1)
            i1.update()
            i2.update()
    elif scvalue.get()=='PAPER':
        if t=='ROCK':
            written_val1.set('YOUR CHOICE IS : PAPER')
            written_val2.set('COMPUTER CHOICE IS : ROCK')
            t9=Label(frame2,text=written_val1.get(),fg='red')
            t9.pack()
            t0=Label(frame2,text=written_val2.get(),fg='red')
            t0.pack()
            c.set(c_score)
            u.set(u_score+1)
            i1.update()
            i2.update()
        elif t=='PAPER':
            written_val1.set('YOUR CHOICE IS : PAPER')
            written_val2.set('COMPUTER CHOICE IS : PAPER')
            t01=Label(frame2,text=written_val1.get(),fg='red')
            t01.pack()
            t02=Label(frame2,text=written_val2.get(),fg='red')
            t02.pack()
            c.set(c_score)
            u.set(u_score)
            i1.update()
            i2.update()
        elif t=='SCISSOR':
            written_val1.set('YOUR CHOICE IS : PAPER')
            written_val2.set('COMPUTER CHOICE IS : SCISSOR')
            t03=Label(frame2,text=written_val1.get(),fg='red')
            t03.pack()
            t04=Label(frame2,text=written_val2.get(),fg='red')
            t04.pack()
            c.set(c_score+1)
            u.set(u_score)
            i1.update()
            i2.update()
    elif scvalue.get()=='SCISSOR':
        if t=='ROCK':
            written_val1.set('YOUR CHOICE IS : SCISSOR')
            written_val2.set('COMPUTER CHOICE IS : ROCK')
            t05=Label(frame2,text=written_val1.get(),fg='red')
            t05.pack()
            t06=Label(frame2,text=written_val2.get(),fg='red')
            t06.pack()
            c.set(c_score+1)
            u.set(u_score)
            i1.update()
            i2.update()
        elif t=='PAPER':
            written_val1.set('YOUR CHOICE IS : SCISSOR')
            written_val2.set('COMPUTER CHOICE IS : PAPER')
            t07=Label(frame2,text=written_val1.get(),fg='red')
            t07.pack()
            t08=Label(frame2,text=written_val2.get(),fg='red')
            t08.pack()
            c.set(c_score)
            u.set(u_score+1)
            i1.update()
            i2.update()
        elif t=='SCISSOR':
            written_val1.set('YOUR CHOICE IS : SCISSOR , ')
            written_val2.set('COMPUTER CHOICE IS : SCISSOR')
            t09=Label(frame2,text=written_val1.get(),fg='red')
            t09.pack()
            t011=Label(frame2,text=written_val2.get(),fg='red')
            t011.pack()
            c.set(c_score)
            u.set(u_score)
            i1.update()
            i2.update()
    if int(c.get())==10:
        print('COMPUTER WINS')
        messagebox.showinfo("RESULTS","SORRY YOU LOSE AND COMPUTER WINS")
        scr.destroy()#this is to close program
    elif int(u.get())==10:
        print('YOU WON')    
        messagebox.showinfo("RESULTS","CONGRATULATIONS YOU WON BUDDY")
        scr.destroy()
            
 
scr=Tk()
scr.title('your game')
scr.geometry('500x800')
scr.resizable(height=True,width=True)
tools=['ROCK','PAPER','SCISSOR']
scvalue=StringVar("")
written_val1=StringVar("")
written_val2=StringVar("")
c=StringVar("")
c_score=0
u_score=0
c.set('0')
u=StringVar("")
u.set('0')
frame1=Frame(scr,width=500,height=300)
frame1.pack(side=TOP)
frame2=Frame(scr,width=500,height=200)
frame2.pack(side=TOP)
t1=Label(frame2,text="Computer Score is :")
t1.pack()
i1=Entry(frame2,textvariable=c,bg='light grey',width=2)
i1.pack()
t2=Label(frame2,text="Your Score is :")
t2.pack()
i2=Entry(frame2,textvariable=u,width=2,bg='light grey')
i2.pack()
b1=Button(frame1,text='ROCK',width=25,height=4,bg='light green')
b1.bind("<Button-1>",start)
b1.pack()
b2=Button(frame1,text='PAPER',width=25,height=4,bg='white')
b2.bind("<Button-1>",start)
b2.pack(side=TOP)
b3=Button(frame1,text='SCISSOR',width=25,height=4,bg='grey')
b3.bind("<Button-1>",start)
b3.pack(side=TOP)
