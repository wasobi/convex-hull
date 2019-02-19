#!/usr/bin/env python3
# if using python 2, swap the next two lines
# from Tkinter import *
from tkinter import *
import copy
from random import randint
from convexhull import computeHull

def hello(event):
    print("Single Click, Button-l")

def showPoints(event):
	print(len(points))
	print(points)

def drawPoint(canvas,x,y):
# 	id = canvas.create_text((x,y),fill="darkred",font="Times 20 bold", text=f"({x},{y})")
	return id

def drawHull():
# 	hull = [(227, 400), (48, 550), (196, 349), (227, 400)]
# 	hull = [(284, 169), (254, 252), (2, 796), (121, 166), (284, 169)]
	hull = [(89, 188), (62, 237), (24, 114), (76, 101), (89, 188)]
	for i in range(0,len(hull)-1):
		x1 = hull[i][0]
		y1 = hull[i][1]
		x2 = hull[i+1][0]
		y2 = hull[i+1][1]
		w.create_line(x1, y1, x2, y2, width=3)
	
	for point in hull:
		w.create_text((point[0],point[1]),fill="darkred",font="Times 20 bold", text=f"({point[0]},{point[1]})")
	
# 	hull = [(314, 94), (465, 656), (363, 649), (314, 94)]
# 	hull = [(285, 437), (456, 208), (532, 551), (416, 536), (285, 437)]
	hull = [(89, 458), (250, 513), (175, 599), (89, 458)]
	for i in range(0,len(hull)-1):
		x1 = hull[i][0]
		y1 = hull[i][1]
		x2 = hull[i+1][0]
		y2 = hull[i+1][1]
		w.create_line(x1, y1, x2, y2, width=3)
	
	for point in hull:
		w.create_text((point[0],point[1]),fill="darkred",font="Times 20 bold", text=f"({point[0]},{point[1]})")


master = Tk()
points = []

submit_button = Button(master, text="Draw Hull", command=drawHull)
submit_button.pack()
quit_button = Button(master, text="Quit", command=master.quit)
quit_button.pack()

canvas_width = 1000
canvas_height = 800
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
ram = PhotoImage(file="ram-sm.gif")
w.pack()

w.mainloop()
