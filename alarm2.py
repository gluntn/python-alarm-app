# -*- coding: utf-8 -*-
import Tkinter as tk

class App:

 def __init__(self, master):
 # VARIABLER

 # ELEMENTER
 # Hovedvindu
  frame = tk.Frame(master)
  frame.pack()
  
  # Også en test
  self.button = tk.Button(frame, text="window test", fg="red", command= lambda: self.notiBox("this is a test"))
  self.button.pack(side=tk.RIGHT)
  
  # Bare en test
  self.hi_there = tk.Button(frame, text="Hello", command=lambda:self.log("hi"))
  self.hi_there.pack(side=tk.RIGHT)
  
  # Liste for alle alarmer
  self.listTest = tk.Listbox(frame)
  self.listTest.pack(side=tk.LEFT)
  
  # Timer
  self.w = tk.Spinbox(master, from_=0, to=24,name="hour")
  self.w.pack()

  # Minutter
  self.x = tk.Spinbox(master, from_=0, to=60, name="minute")
  self.x.pack()

  # Tekst
  self.e = tk.Entry(master)
  self.e.pack()

 # LOGIKK

 # FUNKSJONER

 def log(self, message):
   print message

 def notiBox(self, message):
  # En liten funksjon som skaper en boks med tekst, beskjeder eller feil
  window = tk.Toplevel(root)
  
  self.label = tk.Label(window, text=message)
  self.label.pack()

  
root = tk.Tk()

app = App(root)

root.mainloop()
