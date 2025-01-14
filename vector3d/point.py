from math import sqrt
class Point:
	x = float()
	y = float()
	z = float()
	
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

def distance(a, b):
	return sqrt(pow((b.x - a.x), 2) + pow((b.y - a.y), 2) + pow((b.z - a.z), 2))

def center(a, b):
	return Point((b.x + a.x)/2, (b.y + a.y)/2, (b.z + a.z)/2)
