from tkinter import *
import time
#from tkinter.font import *

'''wn =Tk()
my_font = Font(family = "Helvetica" , size =12)


def make_bigger() :
      my_font['size'] += 2

def make_smaller() :
      my_font['size'] -= 2


my_text = Label(wn, text="Hello, world!", font = my_font)
my_text.pack()

big_butt = Button(wn, text="폰트를 크게", command=make_bigger)
small_butt = Button(wn, text="폰트를 작게", command=make_smaller)
big_butt.pack()
small_butt.pack()

wn.mainloop()'''


'''def checked(i) :
      global player, color, blank, semi_blank
      button = blist[i]

      if button["text"]  != blank :
            return

      button["text"] = semi_blank + player + semi_blank
      button["bg"] = color

      if player == "X" :
            player, color = "O", "lightgreen"

      else :
            player, color = "X", "yellow"


wn=Tk()


blank="                        "
semi_blank = "         "
player="X"
color="yellow"
blist = []

for i in range(9) :
      b= Button(wn, text=blank, command=lambda  k=i :  checked(k))
      b.grid(row=i//3, column = i%3)
      blist.append(b)

wn.mainloop()'''


#1 move rectangular
'''def left() :
      canvas.move(id, -5, 0)
      window.update()

def right() :
      canvas.move(id, 5, 0)
      window.update()

def up() :
      canvas.move(id, 0, -5)
      window.update()

def down() :
      canvas.move(id, 0, 5)
      window.update()
window = Tk()

canvas = Canvas(window, bg = "white", width = 500, height = 300)
canvas.grid(row=0, column = 0, columnspan = 4)

id= canvas.create_rectangle(100, 100, 200, 200, fill = "red")

Button(window, text = "<-(left)", command = left).grid(row=1, column=0)
Button(window, text = "->(right)", command = right).grid(row=1, column=1)
Button(window, text = "^(up)", command = up).grid(row=1, column=2)
Button(window, text = "u(down)", command = down).grid(row=1, column=3)


window.mainloop()'''

#2 .survey
'''window = Tk()

a=0
b=0
c=0
d=0

def a() :
      a += 1
      window.update()

def b() :
      b += 1
      window.update()

def c() :
      c += 1
      window.update()

def d() :
      d += 1
      window.update()

      

label = Label(window, text = "가장 여행하고 싶은 나라는?")
label.pack()

b1=Button(window, text = "미국" )
b2=Button(window, text ="영국 " )
b3=Button(window, text = "프랑스 ")
b4=Button(window, text = "일본 ")

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)


window.mainloop()'''

#3.database
window = Tk()

name = []
career = []
nation = []

def save() :
      name.append(e1)
      career.append(e2)
      nation.append(e3)

#def search() :
      
      
a=Label(window, text = "이름")
b=Label(window, text = "직업")
c=Label(window, text = "국적")

a.grid(row = 0)
b.grid(row = 1)
c.grid(row = 2)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

e1.grid(row= 0 , column = 1)
e2.grid(row= 1 , column = 1)
e3.grid(row= 2 , column = 1)

Button(window, text = "저장", command = save).grid(row = 3)
Button(window, text = "검색", command = search).grid(row=4)

label1 = Label(window, text = "저장할 데이터를 입력하세요")
label1.gird(row = 3, column = 1)

label2 = Label(window, text = "검색할 이름을 입력하세요")
label2.grid(row = 4, column = 1)

window.mainloop()

