#==========import=========
from tkinter import*
import tkinter.messagebox
import random
#==========setting=========
root=Tk()
root.title('Rock , Paper , Scissor')
root.geometry('300x400')
root.resizable(False,False)
color='red'
root.configure(bg=color)
#=========define==========
def creator():
    tkinter.messagebox.showinfo('CREATOR','this game benn created by alireza etemadjoo')
def clear():
    btn4['text']=''
    btnr['text']=''
def rock():
    z=random.randint(0,2)
    if  z==0:
        btn4['text']='Rock'
        btnr['text']='Tie'
    elif z==1:
        btn4['text']='Paper'
        btnr['text']='Loss'
    elif z==2:
        btn4['text']='Scissor'
        btnr['text']='Win'
def paper():
    z=random.randint(0,2)
    if  z==0:
        btn4['text']='Rock'
        btnr['text']='Win'
    elif z==1:
        btn4['text']='Paper'
        btnr['text']='Tie'
    elif z==2:
        btn4['text']='Scissor'
        btnr['text']='Loss'        
def scissor():
    z=random.randint(0,2)
    if  z==0:
        btn4['text']='Rock'
        btnr['text']='Loss'
    elif z==1:
        btn4['text']='Paper'
        btnr['text']='Win'
    elif z==2:
        btn4['text']='Scissor'
        btnr['text']='Tie'    
    
#==========frame=========
f1=Frame(root,width=400,height=50,bg=color)
f1.pack()
f2=Frame(root,width=400,height=50,bg=color)
f2.pack()
f3=Frame(root,width=400,height=50,bg=color)
f3.pack()
f4=Frame(root,width=400,height=50,bg=color)
f4.pack()
f5=Frame(root,width=400,height=50,bg=color)
f5.pack()
f6=Frame(root,width=400,height=50,bg=color)
f6.pack()
f7=Frame(root,width=400,height=50,bg=color)
f7.pack()
f8=Frame(root,width=400,height=50,bg=color)
f8.pack()
#=========button==========
btn1=Button(f1 , text='Rock' , width=30, command=rock)
btn1.pack(padx=4,pady=4)

btn2=Button(f2  ,text='Paper' ,width=30,command=paper)
btn2.pack(padx=4,pady=4)

btn3=Button(f3 ,text='Scissor' ,width=30,command=scissor)
btn3.pack(padx=4,pady=4)

btn4=Button(f5,text='' ,width=30)
btn4.pack(padx=5,pady=5)

btnr=Button(f7,text='',width=30,)
btnr.pack(padx=5,pady=5)

btncrat=Button(f8,text='creator' ,width=8,command=creator )
btncrat.pack(side=LEFT,padx=5,pady=5)

btnclear=Button(f8,text='Clear',width=8,command=clear)
btnclear.pack(side=LEFT,padx=5,pady=5)
#=========label===========
lbl1=Label(f4,text='Computer move:' ,bg=color)
lbl1.pack(padx=5,pady=5)
lbl2=Label(f6,text='Result',bg=color)
lbl2.pack(padx=5,pady=5)
#==========run===========
root.mainloop()
