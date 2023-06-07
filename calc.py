import tkinter as tk
w=tk.Tk()
w.iconbitmap('Calculator.png')
w.title('Calculator')
w.geometry('260x372')
w.resizable(0,0)
w.config(bg='#4C4C4C')
ent=tk.Entry(font=('Roboto',35),width=(10),bg='#4C4C4C',fg='#FFFFFF',justify=tk.RIGHT)
ent.place(x=0,y=0)
prim=[]
otp=[]
def resh(x):
    if x.isdigit():
        prim.append(x)
        otp.append(x)
    if x=='%':
        prim.append('%')
        otp.append('/100*')
    if x=='/' or x=='*' or x=='+' or x=='-' or x=='.':
        prim.append(x)
        otp.append(x)
    if x=='<-':
        prim.pop(-1)
        otp.pop(-1)
    if x=='AC':
        prim.clear()
        otp.clear()
    if x=='=':
        try:
            if not prim:
                for i in ent.get():
                    prim.append(i)
                    otp.append(i)
            a=eval(''.join(otp))
            prim.clear()
            otp.clear()
            for i in str(a):
                prim.append(i)
                otp.append(i)
        except Exception:
            prim.clear()
            otp.clear()
            ent.delete(0,tk.END)
            ent.insert(0,'Error')
            return
    ent.delete(0,tk.END)
    ent.insert(0,(''.join(prim)))
buts=['AC','<-','%','/','7','8','9','*','4','5','6','-','1','2','3','+','0','.','=']
cnop=[]
for e in buts:
    if buts.index(e)>=17:
        but=tk.Button(text=e,font=('Roboto',15),height=2,width=5,bg='#CBCBCB',command=lambda x=e:resh(x))
        but.place(x=(65*(1+((buts.index(e))%4))),y=(57+(63*((buts.index(e))//4))))
        cnop.append(but)
        continue
    if e=='0':
        but=tk.Button(text=e,font=('Roboto',15),height=2,width=11,bg='#CBCBCB',command=lambda x=e:resh(x))
        but.place(x=(65*((buts.index(e))%4)),y=(57+(63*((buts.index(e))//4))))
        cnop.append(but)
        continue
    but=tk.Button(text=e,font=('Roboto',15),height=2,width=5,bg='#CBCBCB',command=lambda x=e:resh(x))
    but.place(x=(65*((buts.index(e))%4)),y=(57+(63*((buts.index(e))//4))))
    cnop.append(but)
for i in cnop:
    if cnop.index(i)%4==3 or i==cnop[-1]:
        i.config(bg='#F69230',fg='#FFFFFF')
w.mainloop()
