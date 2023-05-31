'''
TYRO is an educational app which helps in learning programming by providing best output videos from different types of platforms.
TYRO - A Beginner (Meaning in Latin).
'''

import tkinter as tk
import webbrowser as wb
from tkinter import messagebox

window = tk.Tk()
list1 = [
  'sriram', 'santhosh', 'kranthi', 'bharat', 'damodhar', 'kiran', 'bharath','dddw']
plist = ['1235', '1236', 'abhiram', '7856', 'apac', 'wolf','12224']
window1 = None  # define window1 outside of any function so that it can be accessed globally


def link():
  wb.open('https://youtu.be/TRya0OKgbNg')


def link1():
  wb.open('https://youtu.be/iM1ig-iNS8s')


def link2():
  wb.open('https://youtu.be/2PXyofk43gY')


def link3():
  wb.open('https://youtu.be/W8rfLAA7L1s')


def link4():
  wb.open('https://youtu.be/G2Y5nZChxto')


def link5():
  wb.open('how-to-code-in-python.pdf')


def l1():
  wb.open("https://youtu.be/8PopR3x-VMY")


def l2():
  wb.open("https://youtu.be/0EgpeYB115s")


def l3():
  wb.open("https://youtu.be/-cuhwmOsxsU")


def l4():
  wb.open("https://youtu.be/MQIF-WMUOL8")

def l5():
    wb.open("let-us-c-14.pdf")


def C():
  window5 = tk.Toplevel(window1)
  window5.title("Online")
  jilebi1 = tk.Label(window5, width='300', height='300')
  button13 = tk.Button(jilebi1,
                       text="Basics Of C",
                       width="100",
                       height="5",
                       fg="white",
                       bg="black",
                       command=l1)
  button14 = tk.Button(jilebi1,
                       text="Arrays",
                       width="100",
                       height="5",
                       fg="white",
                       bg="black",
                       command=l2)
  button15 = tk.Button(jilebi1,
                       text="Pointers",
                       width="100",
                       height="5",
                       fg="white",
                       bg="black",
                       command=l3)
  button16 = tk.Button(jilebi1,
                       text="Files",
                       width="100",
                       height="5",
                       fg="white",
                       bg="black",
                       command=l4)
  button17 = tk.Button(jilebi1,
                       text="Study Materials",
                       width="100",
                       height="5",
                       fg="white",
                       bg="black",
                       command=l5)

  jilebi1.pack()
  button13.pack()
  button14.pack()
  button15.pack()
  button16.pack()
  button17.pack()


def python():
  window2 = tk.Toplevel(window1)
  window2.title("Kranthi Kiran Sir")
  jilebi1 = tk.Label(window2, width='300', height='300')
  button6 = tk.Button(jilebi1,
                      text="Basics",
                      width="100",
                      height="5",
                      fg="white",
                      bg="black",
                      command=link)
  button8 = tk.Button(jilebi1,
                      text="Loops",
                      width="100",
                      height="5",
                      fg="white",
                      bg="black",
                      command=link1)
  button9 = tk.Button(jilebi1,
                      text="List, Tuples, Dictionaries and Sets",
                      width="100",
                      height="5",
                      fg="white",
                      bg="black",
                      command=link2)
  button10 = tk.Button(jilebi1,
                       text="Functions",
                       width="100",
                       height="5",
                       fg="white",
                       bg="black",
                       command=link3)
  button11 = tk.Button(jilebi1,
                       text="GUI",
                       width="100",
                       height="5",
                       fg="white",
                       bg="black",
                       command=link4)
  button12 = tk.Button(jilebi1,
                       text="Study Materials",
                       width="100",
                       height="5",
                       fg="white",
                       bg="black",
                       command=link5)

  jilebi1.pack()
  button6.pack()
  button8.pack()
  button9.pack()
  button10.pack()
  button11.pack()
  button12.pack()


def signup():
  window3 = tk.Toplevel()
  window3.title("SIGN UP PAGE")
  lable_heading = tk.Label(window3,
                           text='SIGN UP',
                           fg='red',
                           bg='gold',
                           font=('Arial', 14))
  entry2 = tk.Entry(window3)
  entry3 = tk.Entry(window3)
  create = tk.Button(window3,
                     text="Create",
                     width='12',
                     height='3',
                     fg='gold',
                     bg='purple',
                     command=lambda: printing(entry2, entry3))
  lable_username = tk.Label(window3, text='New Username:')
  lable_pass = tk.Label(window3, text='New Password:')
  lable_heading.pack()
  lable_username.pack()
  entry2.pack()
  lable_pass.pack()
  entry3.pack()
  create.pack()


def printing(entry1, entry2):
  print(f"Username: {entry1.get()}")
  print(f"Password: {entry2.get()}")


def login():
  global window1  # make window1 a global variable so that it can be accessed and modified inside the function
  username = entry.get()
  password = entry1.get()
  if username in list1 and password in plist:
    window1 = tk.Toplevel()
    window1.title("TYRO")
    jilebi = tk.Label(window1, width='300', height='300')
    button3 = tk.Button(jilebi,
                        text="Python progamming",
                        width="100",
                        height="5",
                        fg="blue",
                        bg="yellow",
                        command=python)
    button4 = tk.Button(jilebi,
                        text="C programming",
                        width="100",
                        height="5",
                        fg="gold",
                        bg="red",
                        command=C)
    button5 = tk.Button(jilebi,
                        text="Java programming",
                        width="100",
                        height="5",
                        fg="white",
                        bg="blue")
    jilebi.pack()
    button3.pack()
    button4.pack()
    button5.pack()

  else:
    messagebox.showwarning("User", 'wrong')


lable = tk.Label(window, width='300', height='300', bg="yellow")
image = tk.PhotoImage(file='Logo.png')
lable1 = tk.Label(window, width='55', height='10', bg='white')
lable_username = tk.Label(window, text='Username:')
lable_username1 = tk.Label(window, text='Password:')
lable_username2 = tk.Label(window,
                           text='||NEW USER? SIGN UP NOW BY CLICKING ABOVE||')
entry = tk.Entry(window)
entry1 = tk.Entry(window)
button1 = tk.Button(lable1,
                    text="Log in",
                    width='12',
                    height='3',
                    fg='gold',
                    bg='purple',
                    command=login)

button7 = tk.Button(lable1,
                    text="Sign up",
                    width='12',
                    height='3',
                    fg='gold',
                    bg='purple',
                    command=signup)
lable.configure(image=image)
lable.pack()
lable_username.pack()
entry.pack()
lable_username1.pack()
entry1.pack()
lable1.pack()
button1.pack()
lable_username2.pack()
button7.pack()
window.mainloop()
