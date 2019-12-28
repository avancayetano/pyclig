import pyclig, os

class Player(pyclig.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.score = 0
		self.state = "dead"
		self.cursor = 0


	def on_press(self, key):
		try:
			key = key.char
		except:
			key = key.name
		if self.state == "dead":
			if key == "w":
				self.window.buttons[self.cursor].active = False
				self.window.buttons[self.cursor].update()
				self.cursor -= 1
			if key == "s":
				self.window.buttons[self.cursor].active = False
				self.window.buttons[self.cursor].update()
				self.cursor += 1

			if key == "space" and "PLAY" in self.window.buttons[self.cursor].text:
				self.window.refresh()
				self.state = "alive"
				self.cursor = 0
				self.score = 0
				self.window.buttons[self.cursor].active_help = False

			if key == "space" and "HELP" in self.window.buttons[self.cursor].text:
				self.window.buttons[self.cursor].active_help = not self.window.buttons[self.cursor].active_help
				self.window.buttons[self.cursor].toggle_help()

			if key == "space" and "QUIT" in self.window.buttons[self.cursor].text:
				os.system("kill -STOP {}".format(os.getpid()))

			if self.cursor < 0:
				self.cursor = len(self.window.buttons) - 1
			if self.cursor > len(self.window.buttons) - 1:
				self.cursor = 0
			self.window.buttons[self.cursor].active = True
			self.window.buttons[self.cursor].update()

		else:
			if key == "space":
				self.speed = 3
			if key == "w":
				self.dy = -1
			if key == "s":
				self.dy = 1
			if key == "d":
				self.dx = 2
			if key == "a":
				self.dx = -2

	def on_release(self, key):
		if self.state == "alive":
			try:
				key = key.char
			except:
				key = key.name
			if key == "space":
				self.speed = 1
			if key == "w" or key == "s":
				self.dy = 0
			if key == "a" or key == "d":
				self.dx = 0

	def update(self):
		self.score += 1
		self.window.score.text = "SCORE: {}".format(self.score)
		self.x += self.dx * self.speed
		self.y += self.dy * self.speed
		self.check_bounds()

	def check_bounds(self):
		if self.x < 1:
			self.x = 1
		if self.x + self.width > self.window.width - 1:
			self.x = self.window.width - 1 - self.width
		if self.y < 1:
			self.y = 1
		if self.y + self.height > self.window.height - 1:
			self.y = self.window.height - 1 - self.height