class Sprite:
	def __init__(self, window, x=0, y=0, width=1, height=1, dx=0, dy=0, char="*", speed=1):
		self.window = window
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.dx = dx
		self.dy = dy
		self.speed = speed
		self.char = char
		self.init_xy = [self.x, self.y]
		self.init_dxdy = [self.dx, self.dy]
		self.init_speed = self.speed

	def update(self):
		self.x += self.dx * self.speed
		self.y += self.dy * self.speed
		self.check_bounds()

	def reset(self):
		self.x = self.init_xy[0]
		self.y = self.init_xy[1]
		self.dx = self.init_dxdy[0]
		self.dy = self.init_dxdy[1]
		self.speed = self.init_speed

	def check_bounds():
		pass

	def unrender(self):
		for i in range(self.height):
			self.window.screen[int(self.y) + i][int(self.x): int(self.x) + self.width] = [self.window.char for j in range(self.width)]

	def render(self):
		for i in range(self.height):
			self.window.screen[int(self.y) + i][int(self.x): int(self.x) + self.width] = [self.char for j in range(self.width)]

	def check_group_collision(self, others):
		for obj in others:
			collided = self.is_collided_with(obj)
			if not(collided is self) and collided:
				return collided

	def is_collided_with(self, other):
		if (self.x < other.x + other.width and self.x + self.width > other.x) \
				and (self.y < other.y + other.height and self.y + self.height > other.y):
			return other