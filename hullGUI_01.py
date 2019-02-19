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
	w.delete("all")
	points = []
	print("=====\n=====\n=====\n=====\n")

	# Generate an array of random points
	n = randint(100,400)
	for i in range(n):
		x = randint(0,1000)
		y = randint(0,800)
		drawPoint(w,x,y)
		points.append((x,y))
 r = 4
 id = canvas.create_oval(x-r,y-r,x+r,y+r)

	# very slow but it apparently generates unique points
	# https://stackoverflow.com/questions/19668463/generating-multiple-random-x-y-coordinates-excluding-duplicates
# 	radius = 200
# 	rangeX = (0, 1000)
# 	rangeY = (0, 800)
# 	qty = 10  # or however many points you want
#
# 	# Generate a set of all points within 200 of the origin, to be used as offsets later
# 	# There's probably a more efficient way to do this.
# 	deltas = set()
# 	for x in range(-radius, radius+1):
# 		for y in range(-radius, radius+1):
# 			if x*x + y*y <= radius*radius:
# 				deltas.add((x,y))
#
# 	points = []
# 	excluded = set()
# 	i = 0
# 	while i<qty:
# 		x = random.randrange(*rangeX)
# 		y = random.randrange(*rangeY)
# 		if (x,y) in excluded: continue
# 		points.append((x,y))
# 		i += 1
# 		excluded.update((x+dx, y+dy) for (dx,dy) in deltas)

	# test points
	# scenario 1
	# SET A
# 	points = [(227, 400), (48, 550), (196, 349)]
	# SET B
# 	points = [(314, 94), (465, 656), (363, 649)]
	# SET C
# 	points = [(227, 400), (48, 550), (196, 349), (314, 94), (465, 656), (363, 649)]
	# scenario 2
	# SET C
# 	points = [(247, 386), (855, 617), (1, 777), (706, 775), (183, 246), (409, 767), (35, 562), (465, 3), (178, 381), (153, 50), (487, 363), (373, 68), (473, 106)]
	# scenario 3
	# SET A
# 	points = [(284, 169), (254, 252), (2, 796), (121, 166)]
	# SET B
# 	points = [(285, 437), (456, 208), (532, 551), (416, 536)]
	# SET C
# 	points = [(91, 375), (554, 55), (416, 536), (284, 169), (532, 551), (930, 308), (254, 252), (535, 665), (121, 166), (396, 416), (631, 469), (571, 343), (896, 505), (883, 244), (794, 566), (782, 754), (456, 208), (792, 705), (2, 796), (285, 437)]
	# scenario 4 -- x's that match up (y-aligned) FIXED
# 	points = [(226, 243), (779, 40), (860, 790), (783, 330), (94, 650), (622, 628), (858, 36), (857, 132), (793, 585), (710, 783), (415, 456), (415, 320), (530, 240), (816, 737), (351, 532)]
	# scenario 5 -- x's that match up (y-aligned) FIXED
# 	points = [(538, 380), (441, 598), (933, 215), (979, 216), (318, 623), (426, 249), (554, 442), (347, 423), (801, 653), (267, 556), (441, 404), (696, 500), (866, 332), (548, 653), (677, 440), (914, 48)]
	# scenario 6 -- x's that match up (y-aligned) in set A and B
# 	points = [(201, 334), (684, 533), (388, 613), (75, 485), (406, 787), (555, 515), (631, 740), (720, 144), (573, 663), (864, 69), (135, 61), (508, 732), (543, 420), (992, 356), (791, 537), (441, 355), (747, 541), (9, 54), (157, 52), (154, 596), (737, 641), (658, 81), (370, 302), (780, 693), (573, 379), (28, 501), (435, 300), (43, 478), (510, 262), (59, 381), (468, 217), (792, 426), (629, 20), (693, 352), (257, 38), (111, 238), (459, 443), (558, 474), (138, 604), (805, 694)]
	# scenario 7 -- x's that match up (y-aligned) in set A and B : i can't fix this
	# SET C
 	#points = [(62, 237), (24, 114), (76, 101), (89, 188), (89, 458), (250, 513), (175, 599)]
	# ALL POINTS
    #points = [(388,538),(89,188),(637,331),(190,513), (527,571),(76,101),(810,9),(550,154),(905,761), (829,422),(930,606),(89,458),(481,467),(774,233),(175,599),(861,216),(422,783),(329,337),(347,713),(987,73), (366,697),(381, 368),(379,381),(24,114),(454,513),(62, 237),(490,190),(468,663),(281,352),(250,513),(309, 558),(343,454),(480, 359),(977,721)]

	#print(f"==POINTS==\n{points}\n\n")

	hull = copy.copy(computeHull(points))
	hull.append(hull[0])
	for i in range(0,len(hull)-1):
		x1 = hull[i][0]
		y1 = hull[i][1]
		x2 = hull[i+1][0]
		y2 = hull[i+1][1]
		w.create_line(x1, y1, x2, y2, width=3)

	for point in points:
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
