#!/usr/bin/env python3
# if using python 2, swap the next two lines
# from Tkinter import *
from tkinter import *
import copy
from convexhull import computeHull


def hello(event):
    print("Single Click, Button-l")

def addPoint(event):
	drawPoint(w, event.x, event.y)
	points.append((event.x,event.y))

def drawPoint(canvas,x,y):
	id = canvas.create_text((x,y),fill="darkred",font="Times 20 bold", text=f"({x},{y})")
	return id

def showPoints(event):
	print(points)

def drawHull():
	hull = copy.copy(computeHull(points))
	hull.append(hull[0])
	for i in range(0,len(hull)-1):
		x1 = hull[i][0]
		y1 = hull[i][1]
		x2 = hull[i+1][0]
		y2 = hull[i+1][1]
		w.create_line(x1, y1, x2, y2, width=3)


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
w.bind('<Button-1>', addPoint)

w.mainloop()
