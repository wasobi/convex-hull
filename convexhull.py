import math
import sys

# cannot import numpy
EPSILON = sys.float_info.epsilon

'''
Given two points, p1 and p2,
an x coordinate, x,
and y coordinates y3 and y4,
compute and return the (x,y) coordinates
of the y intercept of the line segment p1->p2
with the line segment (x,y3)->(x,y4)
'''
def yint(p1, p2, x, y3, y4):
	if p1[0] == p2[0]: return (0, 0)	# fix division by zero error
	x1, y1 = p1
	x2, y2 = p2
	x3 = x
	x4 = x
	px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / \
		 float((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
	py = ((x1*y2 - y1*x2)*(y3-y4) - (y1 - y2)*(x3*y4 - y3*x4)) / \
			float((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3-x4))
	return (px, py)

'''
Given three points a,b,c,
computes and returns the area defined by the triangle
a,b,c.
Note that this area will be negative
if a,b,c represents a clockwise sequence,
positive if it is counter-clockwise,
and zero if the points are collinear.
'''
def triangleArea(a, b, c):
	return (a[0]*b[1] - a[1]*b[0] + a[1]*c[0] \
                - a[0]*c[1] + b[0]*c[1] - c[0]*b[1]) / 2.0;

'''
Given three points a,b,c,
returns True if and only if
a,b,c represents a clockwise sequence
(subject to floating-point precision)
'''
def cw(a, b, c):
	return triangleArea(a,b,c) < EPSILON;
'''
Given three points a,b,c,
returns True if and only if
a,b,c represents a counter-clockwise sequence
(subject to floating-point precision)
'''
def ccw(a, b, c):
	return triangleArea(a,b,c) > EPSILON;

'''
Given three points a,b,c,
returns True if and only if
a,b,c are collinear
(subject to floating-point precision)
'''
def collinear(a, b, c):
	return abs(triangleArea(a,b,c)) <= EPSILON

'''
Given a list of points,
sort those points in clockwise order
about their centroid.
Note: this function modifies its argument.
'''
def clockwiseSort(points):
	# get mean x coord, mean y coord
	xavg = sum(p[0] for p in points) / len(points)
	yavg = sum(p[1] for p in points) / len(points)
	angle = lambda p:  ((math.atan2(p[1] - yavg, p[0] - xavg) + 2*math.pi) % (2*math.pi))
	points.sort(key = angle)

'''
some text here
'''
def cwSort(pivot, points):
	x = pivot[0]
	y = pivot[1]
	points.remove(pivot)
	angle = lambda p:  ((math.atan2(p[1] - y, p[0] - x) - (1/2)*math.pi) % (2*math.pi))
	points.sort(key = angle)
	points.insert(0, pivot)

'''

SOURCE: https://math.stackexchange.com/questions/1928991/how-to-change-the-angle-origin-of-a-circle
'''
def ccwSort(pivot, points):
	x = pivot[0]
	y = pivot[1]
	points.remove(pivot)
	angle = lambda p:  (-(math.atan2(p[1] - y, p[0] - x) - (1/2)*math.pi) % (2*math.pi))
	points.sort(key = angle)
	points.insert(0, pivot)

'''
find the median value in a given array
# return the array
'''
def find_median(points):
	med_val = 0
	#if ():
	#else if:

	return med_val

'''
find lowest first, most leftward point and sort radially ccw
'''
def setAnchor(points):
	anchor = points[0]
	for i in range(1, len(points)):
		if (points[i][1] > anchor[1]) or (points[i][1] == anchor[1] and points[i][0] < anchor[0]):
			anchor = points[i]

	ccwSort(anchor, points)

'''
some text here
'''
def grahamScan(points):
	setAnchor(points)
	hull = []
	i = 0
	n = len(points)
	for point in points:
		while len(hull) > 1 and ccw(hull[-2], hull[-1], point):
			hull.pop()
		hull.append(point)
		i += 1
	print(f"hull computed\n{hull}")
	return hull

'''
some text here
'''
def upperTangent(A, B):
	i = 0
	j = 0
	sizeA = len(A)
	sizeB = len(B)

	print("::upper tangent::")

	# edge case: we want floating point incase there's something like A: 284 B: 285 x's
	x = (A[0][0] + B[0][0]) / 2
	y1 = 0
	y2 = 800

	# Error handling
	try:
		while yint(A[i], B[(j + 1) % sizeB], x, y1, y2) < yint(A[i], B[j], x, y1, y2) \
		or yint(A[i-1], B[j], x, y1, y2) < yint(A[i], B[j], x, y1, y2):
			if yint(A[i], B[(j + 1) % sizeB], x, y1, y2) < yint(A[i], B[j], x, y1, y2):
				j = (j + 1) % sizeB
			else:
				i = (i - 1) % sizeA
		# break
	except IndexError:
		print("IndexError: list index out of range")

		print("==DEBUG==")
		print(f"\ni: {i}\tj: {j}")

		exit(1)
	except ZeroDivisionError:
		print("ZeroDivisionError: float division by zero")

		print("==DEBUG==")
		print(f"\ni: {i}\tj: {j}")
		print(f"Points: {A[i]}, {B[i]}")

	print("::ut done::")
	return (A[i], B[j])

'''
some text here
'''
def lowerTangent(A, B):
	i = 0
	j = 0
	sizeA = len(A)
	sizeB = len(B)

	print("::lower tangent::")

	#
	x = (A[0][0] + B[0][0]) / 2
	y1 = 0
	y2 = 800

	try:
		# INVARIANT
		# Pivot at
		while yint(A[i], B[j-1], x, y1, y2) > yint(A[i], B[j], x, y1, y2) \
		or yint(A[(i + 1) % sizeA], B[j], x, y1, y2) > yint(A[i], B[j], x, y1, y2):
			#
			if yint(A[i], B[j-1], x, y1, y2) > yint(A[i], B[j], x, y1, y2):
				j = (j - 1) % sizeB
			#
			else:
				i = (i + 1) % sizeA
	except IndexError:
		print("IndexError: list index out of range")

		print("==DEBUG==")
		print(f"\ni: {i}\tj: {j}")

		exit(1)
	except ZeroDivisionError:
		print("ZeroDivisionError: float division by zero")

		print("==DEBUG==")
		print(f"\ni: {i}\tj: {j}")
		print(f"Points: {A[i]}, {B[i]}")

	print("::lt done::")
	return (A[i], B[j])

'''
some text here
'''
def merge(A, B):
	pivotA = A[0]
	# find pivot, that is: furthest right point
	for i in range(1, len(A)):
		if (A[i][0] == pivotA[0]):		# FIXES WHERE POINTS LINE UP IN Y
			if (A[i][1] > pivotA[1]):
				pivotA = A[i]
		elif (A[i][0] > pivotA[0]):
			pivotA = A[i]

	cwSort(pivotA, A)

	pivotB = B[0]
	# find pivot, that is: furthest left point
	for i in range(1, len(B)):
		if (B[i][0] == pivotB[0]):		# FIXES WHERE POINTS LINE UP IN Y
			if (B[i][1] > pivotB[1]):
				pivotB = B[i]
		elif (B[i][0] < pivotB[0]):
			pivotB = B[i]

	cwSort(pivotB, B)

	print("==MERGING A & B==")
	print(f"A: {A}")
	print(f"B: {B}")

	# two finger algorithm
	utPoints = upperTangent(A, B)
	ltPoints = lowerTangent(A, B)

	print(f"UT: {utPoints} and LT: {ltPoints}")

	C = []

	i = A.index(ltPoints[0])
	sizeA = len(A)
	while A[i] is not utPoints[0]:
		C.append(A[i])
		i = (i + 1) % sizeA

	C.append(utPoints[0])

	i = B.index(utPoints[1])
	sizeB = len(B)
	while B[i] is not ltPoints[1]:
		C.append(B[i])
		i = (i + 1) % sizeB

	C.append(ltPoints[1])

	print(f"C: {C}")
	print("==DONE MERGING==")
	return C

'''
some text here
'''
def convexHull(points):
	n = len(points)
	# INVARIANT
	# For less than 5 points, a valid convex hull will alwasys
	if n <= 5:
		return grahamScan(points)
	A = []
	B = []
	half = int(n / 2)
	A = convexHull(points[:half])
	B = convexHull(points[half:n])

	return merge(A, B)

'''
some text here
'''
def computeHull(points):
	# sort from least to greatest x coords
	points.sort(key=lambda tup: tup[0])	# https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
	#return convexHull(points)
 	points = grahamScan(points)	# uncomment this & comment above to see that graham scan work for any n points

 	return points
