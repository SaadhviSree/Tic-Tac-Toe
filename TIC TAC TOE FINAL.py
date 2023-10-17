from tkinter import *
from PIL import Image,ImageTk
import random
import numpy
main=''
#F0C0E8
#FFC0E8
#E3BBEA
#B9E3F3
#E1D8F6

def singleplayer():
    global resetcounter
    global main
    main.destroy()
    top=Tk()
    top.geometry("1200x700")
    top.title("Tic Tac Toe")
    #topbgopen=Image.open("D:\\Python\\New\\pastel.png")
    #topbgrender=ImageTk.PhotoImage(topbgopen)
    #topbg=Label(top,image=topbgrender)
    #topbg.place(x=0,y=0)
    heading=Label(top,text="Tic Tac Toe",bg="black",fg="white",width="400",height="2")
    heading.config(font=("Goudy Old Style",25,"bold"),justify=CENTER)
    heading.pack()
    resettext="Start"
    resetcounter=0
    xval=700
    yval=200
    heightval=5
    widthval=11
    Player3=''
    Rules=Label(top,text="How to use the game:",width="36",bg="black",fg="white")
    Rules.config(font=("Goudy Old Style",20,"bold"),justify=CENTER)
    Rules.place(x=40,y=110)
    Rules1=Label(top,text="Click Start\nEnter the names of player and click 'Go'.\nSelect the symbol of the Player.\nClick 'Reset' to start a new game.",width="42",bg="#FFC0E8")
    Rules1.config(font=("Goudy Old Style",17),justify=LEFT)
    Rules1.place(x=40,y=180)
    btna=''
    btnb=''
    btnc=''
    btnd=''
    btne=''
    btnf=''
    btng=''
    btnh=''
    btni=''
    btnchooseX=''
    btnchooseO=''
    symbolchoose=''
    noname=Label(top)
    x=''
    symbol=''
    winner=Label(top)
    def stateofbtn():
        global btna
        global btnb
        global btnc
        global btnd
        global btne
        global btnf
        global btng
        global btnh
        global btni
        btna["state"]=btnb["state"]=btnc["state"]=btnd["state"]=btne["state"]=btnf["state"]=btnh["state"]=btnh["state"]=btni["state"]=DISABLED
        btnreset["state"]=NORMAL
        
    def randomx():
        global btna
        global btnb
        global btnc
        global btnd
        global btne
        global btnf
        global btng
        global btnh
        global btni
        global other
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
        global z
        if a==2:
            btna["state"]=DISABLED
            btna["text"]=other
            btna["bg"]="white"
            btna["fg"]="black"
        if b==2:
            btnb["state"]=DISABLED
            btnb["text"]=other
            btnb["bg"]="white"
            btnb["fg"]="black"
        if c==2:
            btnc["state"]=DISABLED
            btnc["text"]=other
            btnc["bg"]="white"
            btnc["fg"]="black"
        if d==2:
            btnd["state"]=DISABLED
            btnd["text"]=other
            btnd["bg"]="white"
            btnd["fg"]="black"
        if e==2:
            btne["state"]=DISABLED
            btne["text"]=other
            btne["bg"]="white"
            btne["fg"]="black"
        if f==2:
            btnf["state"]=DISABLED
            btnf["text"]=other
            btnf["bg"]="white"
            btnf["fg"]="black"
        if g==2:
            btng["state"]=DISABLED
            btng["text"]=other
            btng["bg"]="white"
            btng["fg"]="black"
        if h==2:
            btnh["state"]=DISABLED
            btnh["text"]=other
            btnh["bg"]="white"
            btnh["fg"]="black"
        if i==2:
            btni["state"]=DISABLED
            btni["text"]=other
            btni["bg"]="white"
            btni["fg"]="black"
        z+=1
    def compplayafter():
        global a
        global b   # a  b  c
        global c   # d  e  f
        global d   # g  h  i
        global e
        global f
        global g
        global h
        global i
        global x
        board=[a,b,c,d,e,f,g,h,i]
        if a!=0 and a in board:
            board.remove(a)
        if b!=0 and b in board:
            board.remove(b)
        if c!=0 and c in board:
            board.remove(c)
        if d!=0 and d in board:
            board.remove(d)
        if e!=0 and e in board:
            board.remove(e)
        if f!=0 and f in board:
            board.remove(f)
        if g!=0 and g in board:
            board.remove(g)
        if h!=0 and h in board:
            board.remove(h)
        if i!=0 and i in board:
            board.remove(i)
        if ((a==2 and b==2) or (f==2 and i==2) or (g==2 and e==2)) and (c in board and c!=1 and c==0):
            c=2
            randomx()
        elif ((a==2 and d==2) or (h==2 and i==2) or (e==2 and c==2)) and (g in board and g!=1 and g==0):
            g=2
            randomx()
        elif ((b==2 and c==2) or (d==2 and g==2) or (e==2 and i==2)) and (a in board and a!=1 and a==0):
            a=2
            randomx()
        elif ((g==2 and h==2) or (a==2 and e==2) or (c==2 and f==2)) and (i in board and i!=1 and i==0):
            i=2
            randomx()
        elif ((a==2 and g==2) or (e==2 and f==2)) and (d in board and d!=1 and d==0):
            d=2
            randomx()
        elif ((a==2 and c==2) or (e==2 and h==2)) and (b in board and b!=1 and b==0):
            b=2
            randomx()
        elif ((c==2 and i==2) or (d==2 and e==2)) and (f in board and f!=1 and f==0):
            f=2
            randomx()
        elif ((g==2 and i==2) or (b==2 and e==2)) and (h in board and h!=1 and h==0):
            h=2
            randomx()
        elif ((a==2 and i==2) or (b==2 and h==2) or (c==2 and g==2) or (d==2 and f==2)) and (e in board and e!=1 and e==0):
            e=2
            randomx()
        elif ((a==1 and b==1) or (f==1 and i==1) or (g==1 and e==1)) and (c in board and c!=1 and c==0):
            c=2
            randomx()
        elif ((a==1 and d==1) or (h==1 and i==1) or (e==1 and c==1)) and (g in board and g!=1 and g==0):
            g=2
            randomx()
        elif ((b==1 and c==1) or (d==1 and g==1) or (e==1 and i==1)) and (a in board and a!=1 and a==0):
            a=2
            randomx()
        elif ((g==1 and h==1) or (a==1 and e==1) or (c==1 and f==1)) and (i in board and i!=1 and i==0):
            i=2
            randomx()
        elif ((a==1 and g==1) or (e==1 and f==1)) and (d in board and d!=1 and d==0):
            d=2
            randomx()
        elif ((a==1 and c==1) or (e==1 and h==1)) and (b in board and b!=1 and b==0):
            b=2
            randomx()
        elif ((c==1 and i==1) or (d==1 and e==1)) and (f in board and f!=1 and f==0):
            f=2
            randomx()
        elif ((g==1 and i==1) or (b==1 and e==1)) and (h in board and h!=1 and h==0):
            h=2
            randomx()
        elif ((a==1 and i==1) or (b==1 and h==1) or (c==1 and g==1) or (d==1 and f==1)) and (e in board and e!=1 and e==0):
            e=2
            randomx()
        else:
            boxtochoose=[a,c,g,i,e]
            random.shuffle(boxtochoose)
            x_int=numpy.random.randint(0,4)
            x_box=boxtochoose[x_int]
            if x_box==a and a in board and a!=1 and a==0:
                a=2
                randomx()
            elif x_box==c and c in board and c!=1 and c==0:
                c=2
                randomx()
            elif x_box==g and g in board and g!=1 and g==0:
                g=2
                randomx()
            elif x_box==i and i in board and i!=1 and i==0:
                i=2
                randomx()
            elif x_box==i and e in board and e!=1 and e==0:
                e=2
                randomx()
        board=[a,b,c,d,e,f,g,h,i]
        if a!=0 and a in board:
            board.remove(a)
        if b!=0 and b in board:
            board.remove(b)
        if c!=0 and c in board:
            board.remove(c)
        if d!=0 and d in board:
            board.remove(d)
        if e!=0 and e in board:
            board.remove(e)
        if f!=0 and f in board:
            board.remove(f)
        if g!=0 and g in board:
            board.remove(g)
        if h!=0 and h in board:
            board.remove(h)
        if i!=0 and i in board:
            board.remove(i)

    def compplayfirst():
        global a
        global b   # a  b  c
        global c   # d  e  f
        global d   # g  h  i
        global e
        global f
        global g
        global h
        global i
        global x
        if a==1 or b==1 or c==1 or d==1 or f==1 or g==1 or h==1 or i==1:
            e=2
            randomx()
        elif e==1:
            aftere=[i,a,g,c]
            random.shuffle(aftere)
            r_int=numpy.random.randint(0,3)
            x=aftere[r_int]
            if x==a:
                a=2
            elif x==c:
                c=2
            elif x==g:
                g=2
            elif x==i:
                i=2
            randomx()
        
    def winnerdeclare():
        global winner
        global a
        global b   # a  b  c
        global c   # d  e  f
        global d   # g  h  i
        global e
        global f
        global g
        global h
        global i
        global Player3
        global z
        if (a==1 and b==1 and c==1) or (d==1 and e==1 and f==1) or (g==1 and h==1 and i==1):
            winner.destroy()
            winner=Label(top,text=Player3.upper()+" IS THE WINNER!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
            z=0
        elif (a==1 and d==1 and g==1) or (b==1 and e==1 and h==1) or (c==1 and f==1 and i==1):
            winner.destroy()
            winner=Label(top,text=Player3.upper()+" IS THE WINNER!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
            z=0
        elif (a==1 and e==1 and i==1) or (c==1 and e==1 and g==1):
            winner.destroy()
            winner=Label(top,text=Player3.upper()+" IS THE WINNER!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
            z=0
        elif (a==2 and b==2 and c==2) or (d==2 and e==2 and f==2) or (g==2 and h==2 and i==2):
            winner.destroy()
            winner=Label(top,text="You lose... Try again",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
            z=0
        elif (a==2 and d==2 and g==2) or (b==2 and e==2 and h==2) or (c==2 and f==2 and i==2):
            winner.destroy()
            winner=Label(top,text="You lose... Try again",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
            z=0
        elif (a==2 and e==2 and i==2) or (c==2 and e==2 and g==2):
            winner.destroy()
            winner=Label(top,text="You lose... Try again",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
            z=0
        elif a!=0 and b!=0 and c!=0 and d!=0 and e!=0 and f!=0 and g!=0 and h!=0 and i!=0:
            winner.destroy()
            winner=Label(top,text="Its a TIE!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="white",fg="red")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
            z=0
    a,b,c,d,e,f,g,h,i=0,0,0,0,0,0,0,0,0
    chosen=''
    other=''

    #For Button 'a'
    def Onclicka():
        global z
        global a
        global chosen
        global Player3
        global btna
        if z%2==0:
            a=1
            btna["state"]=DISABLED
            btna["text"]=chosen
            btna["bg"]="black"
            btna["fg"]="white"
            z+=1
            winnerdeclare()
        if z%2!=0:
            if z<3:
                compplayfirst()
            elif z>=3 and z<10:
                compplayafter()
            winnerdeclare()

    #For Button 'b'
    def Onclickb():
        global z
        global b
        global chosen
        global Player3
        global btnb
        if z%2==0:
            b=1
            btnb["state"]=DISABLED
            btnb["text"]=chosen
            btnb["bg"]="black"
            btnb["fg"]="white"
            z+=1
            winnerdeclare()
        if z%2!=0:
            if z<3:
                compplayfirst()
            elif z>=3 and z<10:
                compplayafter()
            winnerdeclare()

    #For Button 'c'
    def Onclickc():
        global z
        global c
        global chosen
        global Player3
        global btnc
        if z%2==0:
            c=1
            btnc["state"]=DISABLED
            btnc["text"]=chosen
            btnc["bg"]="black"
            btnc["fg"]="white"
            z+=1
            winnerdeclare()
        if z%2!=0:
            if z<3:
                compplayfirst()
            elif z>=3 and z<10:
                compplayafter()
            winnerdeclare()
        
    #For Button 'd'
    def Onclickd():
        global z
        global d
        global chosen
        global Player3
        global btnd
        if z%2==0:
            d=1
            btnd["state"]=DISABLED
            btnd["text"]=chosen
            btnd["bg"]="black"
            btnd["fg"]="white"
            z+=1
            winnerdeclare()
        if z%2!=0:
            if z<3:
                compplayfirst()
            elif z>=3 and z<10:
                compplayafter()
            winnerdeclare()

    #For Button 'e'
    def Onclicke():
        global z
        global e
        global chosen
        global Player3
        global btne
        if z%2==0:
            e=1
            btne["state"]=DISABLED
            btne["text"]=chosen
            btne["bg"]="black"
            btne["fg"]="white"
            z+=1
            winnerdeclare()
        if z%2!=0:
            if z<3:
                compplayfirst()
            elif z>=3 and z<10:
                compplayafter()
            winnerdeclare()

    #For Button 'f'
    def Onclickf():
        global z
        global f
        global chosen
        global Player3
        global btnf
        if z%2==0:
            f=1
            btnf["state"]=DISABLED
            btnf["text"]=chosen
            btnf["bg"]="black"
            btnf["fg"]="white"
            z+=1
            winnerdeclare()
        if z%2!=0:
            if z<3:
                compplayfirst()
            elif z>=3 and z<10:
                compplayafter()
            winnerdeclare()

    #For Button 'g'
    def Onclickg():
        global z
        global g
        global chosen
        global Player3
        global btng
        if z%2==0:
            g=1
            btng["state"]=DISABLED
            btng["text"]=chosen
            btng["bg"]="black"
            btng["fg"]="white"
            z+=1
            winnerdeclare()
        if z%2!=0:
            if z<3:
                compplayfirst()
            elif z>=3 and z<10:
                compplayafter()
            winnerdeclare()

    #For Button 'h'
    def Onclickh():
        global z
        global h
        global chosen
        global Player3
        global btnh
        if z%2==0:
            h=1
            btnh["state"]=DISABLED
            btnh["text"]=chosen
            btnh["bg"]="black"
            btnh["fg"]="white"
            z+=1
            winnerdeclare()
        if z%2!=0:
            if z<3:
                compplayfirst()
            elif z>=3 and z<10:
                compplayafter()
            winnerdeclare()

    #For Button 'i'
    def Onclicki():
        global z
        global i
        global chosen
        global Player3
        global btni
        if z%2==0:
            i=1
            btni["state"]=DISABLED
            btni["text"]=chosen
            btni["bg"]="black"
            btni["fg"]="white"
            z+=1
            winnerdeclare()
        if z%2!=0:
            if z<3:
                compplayfirst()
            elif z>=3 and z<10:
                compplayafter()
            winnerdeclare()

    def buttons():
        global btna
        global btnb
        global btnc
        global btnd
        global btne
        global btnf
        global btng
        global btnh
        global btni
        btna=Button(top,height=heightval,width=widthval,command=Onclicka,font=("Goudy Old Style",15,"bold"))
        btna.place(x=xval,y=yval)
        btnb=Button(top,height=heightval,width=widthval,command=Onclickb,font=("Goudy Old Style",15,"bold"))
        btnb.place(x=xval+150,y=yval)
        btnc=Button(top,height=heightval,width=widthval,command=Onclickc,font=("Goudy Old Style",15,"bold"))
        btnc.place(x=xval+300,y=yval)
        btnd=Button(top,height=heightval,width=widthval,command=Onclickd,font=("Goudy Old Style",15,"bold"))
        btnd.place(x=xval,y=yval+150)
        btne=Button(top,height=heightval,width=widthval,command=Onclicke,font=("Goudy Old Style",15,"bold"))
        btne.place(x=xval+150,y=yval+150)
        btnf=Button(top,height=heightval,width=widthval,command=Onclickf,font=("Goudy Old Style",15,"bold"))
        btnf.place(x=xval+300,y=yval+150)
        btng=Button(top,height=heightval,width=widthval,command=Onclickg,font=("Goudy Old Style",15,"bold"))
        btng.place(x=xval,y=yval+300)
        btnh=Button(top,height=heightval,width=widthval,command=Onclickh,font=("Goudy Old Style",15,"bold"))
        btnh.place(x=xval+150,y=yval+300)
        btni=Button(top,height=heightval,width=widthval,command=Onclicki,font=("Goudy Old Style",15,"bold"))
        btni.place(x=xval+300,y=yval+300)

    def reset():
        global resetcounter
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
        global z
        global other
        global chosen
        global btna
        global btnb
        global btnc
        global btnd
        global btne
        global btnf
        global btng
        global btnh
        global btni
        global winner
        global turn
        global symbolchoose
        global btnchooseX
        global btnchooseO
        global noname
        if resetcounter==1:
            btna.destroy()
            btnb.destroy()
            btnc.destroy()
            btnd.destroy()
            btne.destroy()
            btnf.destroy()
            btng.destroy()
            btnh.destroy()
            btni.destroy()
            winner.destroy()
            btnchooseX.destroy()
            btnchooseO.destroy()
            symbolchoose.destroy()
            noname.destroy()
        resetcounter=1
        Name3=Label(top,text="Name of Player :",bg="#E3BBEA")
        Name3.config(font=("Goudy Old Style",18),justify=LEFT)
        Name3.place(x=40,y=360)
        Nametre=StringVar()
        Name3_entry=Entry(textvariable=Nametre,font=("Goudy old style",15),width=30)
        Name3_entry.place(x=230,y=363)
        z=0
        a,b,c,d,e,f,g,h,i=0,0,0,0,0,0,0,0,0
        chosen=''
        other=''
        Player3=''
        winner=Label(top)
        noname=Label(top,font=("Goudy Old Style",15),justify=CENTER,bg="#E1D8F6")
        btnreset["text"]="Reset"
        btnreset["state"]=DISABLED
        def Playclick():
            global Player3
            global noname
            global btnchooseX
            global btnchooseO
            global symbolchoose
            Player3=Nametre.get()
            if Player3=='':
                noname["text"]="Name not entered"
                noname.place(x=230,y=520)
            elif Player3!='':
                btnplay["state"]=DISABLED
                symbolchoose=Label(top,text=Player3+"... Choose your Symbol:",font=("Goudy Old Style",17),width="43",justify=CENTER,height=2,bg="#E1D8F6")
                symbolchoose.place(x=40,y=500)
                def chooseX():
                    global chosen
                    global other
                    global x
                    chosen="X"
                    other="O"
                    btnchooseX["bg"]="black"
                    btnchooseX["fg"]="white"
                    btnchooseX["state"]=DISABLED
                    btnchooseO["bg"]="white"
                    btnchooseO["fg"]="black"
                    btnchooseO["state"]=DISABLED
                    buttons()
                btnchooseX=Button(top,text='X',width=5,height=2,command=chooseX,font=("Goudy Old Style",15),bg="#E1D8F6")
                btnchooseX.place(x=230,y=570)
                def chooseO():
                    global chosen
                    global other
                    global x
                    chosen="O"
                    other="X"
                    btnchooseX["bg"]="white"
                    btnchooseX["fg"]="black"
                    btnchooseX["state"]=DISABLED
                    btnchooseO["bg"]="black"
                    btnchooseO["fg"]="white"
                    btnchooseO["state"]=DISABLED
                    buttons()
                btnchooseO=Button(top,text='O',width=5,height=2,command=chooseO,font=("Goudy Old Style",15),bg="#E1D8F6")
                btnchooseO.place(x=320,y=570)
        btnplay=Button(top,text="GO!",height=2,width=10,font=("Goudy Old Style",15),command=Playclick,bg="#B9E3F3",fg="black")
        btnplay.place(x=250,y=430)
    btnreset=Button(top,text=resettext,width=10,font=("Goudy Old Style",15),command=reset)
    btnreset.place(x=750,y=100)
    def gameexit():
        top.destroy()
        mainwindow()
    btnexit=Button(top,text="Exit",width=10,font=("Goudy Old Style",15),command=gameexit)
    btnexit.place(x=950,y=100)
    top.mainloop()

def doubleplayer():
    global resetcounter
    global main
    main.destroy()
    top=Tk()
    top.geometry("1200x700")
    top.title("Tic Tac Toe")
    #topbgopen=Image.open("D:\\Python\\New\\pastel 2.png")
    #topbgrender=ImageTk.PhotoImage(topbgopen)
    #topbg=Label(top,image=topbgrender)
    #topbg.place(x=0,y=0)
    heading=Label(top,text="Tic Tac Toe",bg="black",fg="white",width="400",height="2")
    heading.config(font=("Goudy Old Style",25,"bold"),justify=CENTER)
    heading.pack()
    resettext="Start"
    resetcounter=0
    xval=700
    yval=200
    heightval=5
    widthval=11
    Player1=''
    Player2=''
    Rules=Label(top,text="How to use the game:",width="36",bg="black",fg="white")
    Rules.config(font=("Goudy Old Style",20,"bold"),justify=CENTER)
    Rules.place(x=40,y=110)
    Rules1=Label(top,text="Click Start\nEnter the names of both the players and click 'Go'.\nSelect the symbol of the 1st Player.\nThe 2nd Player's symbol will be selected automatically.\n\
    Click 'Reset' to start a new game.",width="42")
    Rules1.config(font=("Goudy Old Style",17),justify=LEFT)
    Rules1.place(x=40,y=160)
    btna=''
    btnb=''
    btnc=''
    btnd=''
    btne=''
    btnf=''
    btng=''
    btnh=''
    btni=''
    btnchooseX=''
    btnchooseO=''
    symbolchoose=''
    noname=Label(top)
    def stateofbtn():
        global btna
        global btnb
        global btnc
        global btnd
        global btne
        global btnf
        global btng
        global btnh
        global btni
        btna["state"]=btnb["state"]=btnc["state"]=btnd["state"]=btne["state"]=btnf["state"]=btnh["state"]=btnh["state"]=btni["state"]=DISABLED
        btnreset["state"]=NORMAL
        
    def winnerdeclare():
        global winner
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
        global Player1
        global Player2
        if (a==1 and b==1 and c==1) or (d==1 and e==1 and f==1) or (g==1 and h==1 and i==1):
            winner=Label(top,text=Player1.upper()+" IS THE WINNER!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
        elif (a==1 and d==1 and g==1) or (b==1 and e==1 and h==1) or (c==1 and f==1 and i==1):
            winner=Label(top,text=Player1.upper()+" IS THE WINNER!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
        elif (a==1 and e==1 and i==1) or (c==1 and e==1 and g==1):
            winner=Label(top,text=Player1.upper()+" IS THE WINNER!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
        elif (a==2 and b==2 and c==2) or (d==2 and e==2 and f==2) or (g==2 and h==2 and i==2):
            winner=Label(top,text=Player2.upper()+" IS THE WINNER!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
        elif (a==2 and d==2 and g==2) or (b==2 and e==2 and h==2) or (c==2 and f==2 and i==2):
            winner=Label(top,text=Player2.upper()+" IS THE WINNER!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
        elif (a==2 and e==2 and i==2) or (c==2 and e==2 and g==2):
            winner=Label(top,text=Player2.upper()+" IS THE WINNER!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="black",fg="yellow")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
        elif a!=0 and b!=0 and c!=0 and d!=0 and e!=0 and f!=0 and g!=0 and h!=0 and i!=0:
            winner=Label(top,text="Its a TIE!!!",font=("Goudy Old Style",20,"bold"),width=30,justify=CENTER,bg="white",fg="red")
            winner.place(x=xval,y=yval+450)
            stateofbtn()
    z=0
    a,b,c,d,e,f,g,h,i=0,0,0,0,0,0,0,0,0
    chosen=''
    other=''

    #For Button 'a'
    def Onclicka():
        global z
        global a
        global other
        global chosen
        global Player1
        global Player2
        global btna
        global turn
        z+=1
        if z%2==0:
            turn["text"]=Player1+"'s turn:"
            turn.place(x=xval,y=yval-50)
            a=2
            btna["state"]=DISABLED
            btna["text"]=other
            btna["bg"]="black"
            btna["fg"]="white"
        else:
            turn["text"]=Player2+"'s turn:"
            turn.place(x=xval,y=yval-50)
            a=1
            btna["state"]=DISABLED
            btna["text"]=chosen
            btna["fg"]="black"
            btna["bg"]="white"
            if z==9:
                z=0
        winnerdeclare()

    #For Button 'b'
    def Onclickb():
        global z
        global b
        global other
        global chosen
        global Player1
        global Player2
        global btnb
        global turn
        z+=1
        if z%2==0:
            turn["text"]=Player1+"'s turn:"
            turn.place(x=xval,y=yval-50)
            b=2
            btnb["state"]=DISABLED
            btnb["text"]=other
            btnb["bg"]="black"
            btnb["fg"]="white"
        else:
            turn["text"]=Player2+"'s turn:"
            turn.place(x=xval,y=yval-50)
            b=1
            btnb["state"]=DISABLED
            btnb["text"]=chosen
            btnb["fg"]="black"
            btnb["bg"]="white"
            if z==9:
                z=0
        winnerdeclare()

    #For Button 'c'
    def Onclickc():
        global z
        global c
        global other
        global chosen
        global Player1
        global Player2
        global btnc
        global turn
        z+=1
        if z%2==0:
            turn["text"]=Player1+"'s turn:"
            turn.place(x=xval,y=yval-50)
            c=2
            btnc["state"]=DISABLED
            btnc["text"]=other
            btnc["bg"]="black"
            btnc["fg"]="white"
        else:
            turn["text"]=Player2+"'s turn:"
            turn.place(x=xval,y=yval-50)
            c=1
            btnc["state"]=DISABLED
            btnc["text"]=chosen
            btnc["fg"]="black"
            btnc["bg"]="white"
            if z==9:
                z=0
        winnerdeclare()
        
    #For Button 'd'
    def Onclickd():
        global z
        global d
        global other
        global chosen
        global Player1
        global Player2
        global btnd
        global turn
        z+=1
        if z%2==0:
            turn["text"]=Player1+"'s turn:"
            turn.place(x=xval,y=yval-50)
            d=2
            btnd["state"]=DISABLED
            btnd["text"]=other
            btnd["bg"]="black"
            btnd["fg"]="white"
        else:
            turn["text"]=Player2+"'s turn:"
            turn.place(x=xval,y=yval-50)
            d=1
            btnd["state"]=DISABLED
            btnd["text"]=chosen
            btnd["fg"]="black"
            btnd["bg"]="white"
            if z==9:
                z=0
        winnerdeclare()

    #For Button 'e'
    def Onclicke():
        global z
        global e
        global other
        global chosen
        global Player1
        global Player2
        global btne
        global turn
        z+=1
        if z%2==0:
            turn["text"]=Player1+"'s turn:"
            turn.place(x=xval,y=yval-50)
            e=2
            btne["state"]=DISABLED
            btne["text"]=other
            btne["bg"]="black"
            btne["fg"]="white"
        else:
            turn["text"]=Player2+"'s turn:"
            turn.place(x=xval,y=yval-50)
            e=1
            btne["state"]=DISABLED
            btne["text"]=chosen
            btne["fg"]="black"
            btne["bg"]="white"
            if z==9:
                z=0
        winnerdeclare()

    #For Button 'f'
    def Onclickf():
        global z
        global f
        global other
        global chosen
        global Player1
        global Player2
        global btnf
        global turn
        z+=1
        if z%2==0:
            turn["text"]=Player1+"'s turn:"
            turn.place(x=xval,y=yval-50)
            f=2
            btnf["state"]=DISABLED
            btnf["text"]=other
            btnf["bg"]="black"
            btnf["fg"]="white"
        else:
            turn["text"]=Player2+"'s turn:"
            turn.place(x=xval,y=yval-50)
            f=1
            btnf["state"]=DISABLED
            btnf["text"]=chosen
            btnf["fg"]="black"
            btnf["bg"]="white"
            if z==9:
                z=0
        winnerdeclare()

    #For Button 'g'
    def Onclickg():
        global z
        global g
        global other
        global chosen
        global Player1
        global Player2
        global btng
        global turn
        z+=1
        if z%2==0:
            turn["text"]=Player1+"'s turn:"
            turn.place(x=xval,y=yval-50)
            g=2
            btng["state"]=DISABLED
            btng["text"]=other
            btng["bg"]="black"
            btng["fg"]="white"
        else:
            turn["text"]=Player2+"'s turn:"
            turn.place(x=xval,y=yval-50)
            g=1
            btng["state"]=DISABLED
            btng["text"]=chosen
            btng["fg"]="black"
            btng["bg"]="white"
            if z==9:
                z=0
        winnerdeclare()

    #For Button 'h'
    def Onclickh():
        global z
        global h
        global other
        global chosen
        global Player1
        global Player2
        global btnh
        global turn
        z+=1
        if z%2==0:
            turn["text"]=Player1+"'s turn:"
            turn.place(x=xval,y=yval-50)
            h=2
            btnh["state"]=DISABLED
            btnh["text"]=other
            btnh["bg"]="black"
            btnh["fg"]="white"
        else:
            turn["text"]=Player2+"'s turn:"
            turn.place(x=xval,y=yval-50)
            h=1
            btnh["state"]=DISABLED
            btnh["text"]=chosen
            btnh["fg"]="black"
            btnh["bg"]="white"
            if z==9:
                z=0
        winnerdeclare()

    #For Button 'i'
    def Onclicki():
        global z
        global i
        global other
        global chosen
        global Player1
        global Player2
        global btni
        global turn
        z+=1
        if z%2==0:
            turn["text"]=Player1+"'s turn:"
            turn.place(x=xval,y=yval-50)
            i=2
            btni["state"]=DISABLED
            btni["text"]=other
            btni["bg"]="black"
            btni["fg"]="white"
        else:
            turn["text"]=Player2+"'s turn:"
            turn.place(x=xval,y=yval-50)
            i=1
            btni["state"]=DISABLED
            btni["text"]=chosen
            btni["fg"]="black"
            btni["bg"]="white"
            if z==9:
                z=0
        winnerdeclare()

    def buttons():
        global btna
        global btnb
        global btnc
        global btnd
        global btne
        global btnf
        global btng
        global btnh
        global btni
        btna=Button(top,height=heightval,width=widthval,command=Onclicka,font=("Goudy old style",15,"bold"))
        btna.place(x=xval,y=yval)
        btnb=Button(top,height=heightval,width=widthval,command=Onclickb,font=("Goudy old style",15,"bold"))
        btnb.place(x=xval+150,y=yval)
        btnc=Button(top,height=heightval,width=widthval,command=Onclickc,font=("Goudy old style",15,"bold"))
        btnc.place(x=xval+300,y=yval)
        btnd=Button(top,height=heightval,width=widthval,command=Onclickd,font=("Goudy old style",15,"bold"))
        btnd.place(x=xval,y=yval+150)
        btne=Button(top,height=heightval,width=widthval,command=Onclicke,font=("Goudy old style",15,"bold"))
        btne.place(x=xval+150,y=yval+150)
        btnf=Button(top,height=heightval,width=widthval,command=Onclickf,font=("Goudy old style",15,"bold"))
        btnf.place(x=xval+300,y=yval+150)
        btng=Button(top,height=heightval,width=widthval,command=Onclickg,font=("Goudy old style",15,"bold"))
        btng.place(x=xval,y=yval+300)
        btnh=Button(top,height=heightval,width=widthval,command=Onclickh,font=("Goudy old style",15,"bold"))
        btnh.place(x=xval+150,y=yval+300)
        btni=Button(top,height=heightval,width=widthval,command=Onclicki,font=("Goudy old style",15,"bold"))
        btni.place(x=xval+300,y=yval+300)

    def reset():
        global resetcounter
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
        global z
        global other
        global chosen
        global btna
        global btnb
        global btnc
        global btnd
        global btne
        global btnf
        global btng
        global btnh
        global btni
        global winner
        global turn
        global symbolchoose
        global btnchooseX
        global btnchooseO
        global noname
        if resetcounter==1:
            btna.destroy()
            btnb.destroy()
            btnc.destroy()
            btnd.destroy()
            btne.destroy()
            btnf.destroy()
            btng.destroy()
            btnh.destroy()
            btni.destroy()
            winner.destroy()
            btnchooseX.destroy()
            btnchooseO.destroy()
            turn.destroy()
            symbolchoose.destroy()
            noname.destroy()
        resetcounter=1
        Name1=Label(top,text="Name of Player 1 :")
        Name2=Label(top,text="Name of Player 2 :")
        Name1.config(font=("Goudy Old Style",18),justify=LEFT)
        Name2.config(font=("Goudy Old Style",18),justify=LEFT)
        Name1.place(x=40,y=330)
        Name2.place(x=40,y=370)
        Nameone=StringVar()
        Nametwo=StringVar()
        Name1_entry=Entry(textvariable=Nameone,font=("Goudy old style",15),width=30)
        Name2_entry=Entry(textvariable=Nametwo,font=("Goudy old style",15),width=30)
        Name1_entry.place(x=230,y=333)
        Name2_entry.place(x=230,y=373)
        z=0
        a,b,c,d,e,f,g,h,i=0,0,0,0,0,0,0,0,0
        chosen=''
        other=''
        Player1=''
        Player2=''
        noname=Label(top,font=("Goudy Old Style",15),width=20,justify=CENTER)
        btnreset["text"]="Reset"
        btnreset["state"]=DISABLED
        turn=Label(top,font=("Goudy Old Style",15),width=20,justify=LEFT)
        def Playclick():
            global Player1
            global Player2
            global noname
            global turn
            global btnchooseX
            global btnchooseO
            global symbolchoose
            Player1=Nameone.get()
            Player2=Nametwo.get()
            if Player1=='' or Player2=='':
                noname["text"]="Both names not entered!"
                noname.place(x=200,y=520)
            elif Player1!='' and Player2!='':
                btnplay["state"]=DISABLED
                symbolchoose=Label(top,text=Player1+"... Choose your Symbol:",font=("Goudy Old Style",17),width="43",justify=CENTER,height=2)
                symbolchoose.place(x=40,y=500)
                def chooseX():
                    global chosen
                    global other
                    global x
                    global turn
                    chosen="X"
                    other="O"
                    turn["text"]=Player1+"'s turn:"
                    turn.place(x=xval,y=yval-50)
                    btnchooseX["bg"]="white"
                    btnchooseX["fg"]="black"
                    btnchooseX["state"]=DISABLED
                    btnchooseO["bg"]="black"
                    btnchooseO["fg"]="white"
                    btnchooseO["state"]=DISABLED
                    buttons()
                btnchooseX=Button(top,text='X',width=5,height=2,command=chooseX,font=("Goudy Old Style",15))
                btnchooseX.place(x=230,y=570)
                def chooseO():
                    global chosen
                    global other
                    global x
                    global turn
                    chosen="O"
                    other="X"
                    turn["text"]=Player1+"'s turn:"
                    turn.place(x=xval,y=yval-50)
                    btnchooseX["bg"]="black"
                    btnchooseX["fg"]="white"
                    btnchooseX["state"]=DISABLED
                    btnchooseO["bg"]="white"
                    btnchooseO["fg"]="black"
                    btnchooseO["state"]=DISABLED
                    buttons()
                btnchooseO=Button(top,text='O',width=5,height=2,command=chooseO,font=("Goudy Old Style",15))
                btnchooseO.place(x=320,y=570)
        btnplay=Button(top,text="GO!",height=2,width=10,font=("Goudy Old Style",15),command=Playclick,bg="cyan",fg="black")
        btnplay.place(x=250,y=430)
    btnreset=Button(top,text=resettext,width=10,font=("Goudy Old Style",15),command=reset)
    btnreset.place(x=750,y=100)
    def gameexit():
        top.destroy()
        mainwindow()
    btnexit=Button(top,text="Exit",width=10,font=("Goudy Old Style",15),command=gameexit)
    btnexit.place(x=950,y=100)
    top.mainloop()
def mainwindowexit():
    global main
    main.destroy()
def mainwindow():
    global main
    main=Tk()
    main.geometry("470x340")
    main.title("Tic Tac Toe")
    #mainbgopen=Image.open('D:\\Python\\New\\bling.png')
    #mainbgrender=ImageTk.PhotoImage(mainbgopen)
    #mainbg=Label(main,image=mainbgrender)
    #mainbg.image=mainbgrender
    #mainbg.place(x=0,y=0)
    heading=Label(main,text="Tic Tac Toe",bg="black",fg="white",width="400",height="2")
    heading.config(font=("Goudy Old Style",20,"bold"),justify=CENTER)
    heading.pack()
    resetcounter=0
    btndp=Button(main,text="Single Player Mode",font=("Goudy Old Style",15),command=singleplayer,width=20,height=2)
    btndp.place(x=120,y=90)
    btndp=Button(main,text="Double Player Mode",font=("Goudy Old Style",15),command=doubleplayer,width=20,height=2)
    btndp.place(x=120,y=180)
    btnmainexit=Button(main,text="Exit Game",font=("Goudy Old Style",15),command=mainwindowexit)
    btnmainexit.place(x=175,y=270)
mainwindow()
