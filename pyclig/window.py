import os, time, sys
from . import label, sprite

class Window:
	def __init__(self, width=80, height=22, char=" ", fps=30):
		self.width = width
		self.height = height
		self.char = char

		self.fps = fps
		self.clock = 0
		sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=height, cols=width)) # changes terminal dimensions
		self.refresh()

	def refresh(self):
		self.screen = []
		for i in range(self.height):
			if i == 0 or i == self.height - 1:
				self.screen.append(["=" for j in range(self.width)])
			else:
				self.screen.append(["|" if j == 0 or j == self.width - 1 else self.char for j in range(self.width)])

	# needs to be overwritten
	def update(self):
		pass		

	def exit(self):
		os.system("kill -STOP {}".format(os.getpid()))

	def draw(self):
		for i in range(self.height):
			print("".join(self.screen[i]))