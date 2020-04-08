import pyclig, random

class Obstacle(pyclig.shapes.Rect):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		direction_x = random.random() * random.choice([-1, 1])
		if direction_x == 0:
			direction_x = 0.5
		direction_y = (1 - direction_x ** 2) ** (1 / 2)
		self.direction = (direction_x, direction_y)
		self.init_speed = self.speed
		self.init_pos = (self.x, self.y)


	def reset(self):
		self.x = self.init_pos[0]
		self.y = self.init_pos[1]
		direction_x = random.random() * random.choice([-1, 1])
		if direction_x == 0:
			direction_x = 0.5
		direction_y = (1 - direction_x ** 2) ** (1 / 2)
		self.direction = (direction_x, direction_y)
		self.speed = self.init_speed


	def update(self):
		self.x += self.direction[0] * self.speed[0]
		self.y += self.direction[1] * self.speed[1]
		self.speed = ((self.window.player.score // 200) * 0.25 + self.init_speed[0], (self.window.player.score // 200) * 0.25 + self.init_speed[1])
		self.check_bounds()


	def change_direction(self, other):
		self.direction, other.direction = other.direction, self.direction

	def check_bounds(self):
		if self.x < 1:
			self.x = 1
			self.direction = (-self.direction[0], self.direction[1])
		if self.x + self.width > self.window.width - 1:
			self.x = self.window.width - 1 - self.width
			self.direction = (-self.direction[0], self.direction[1])
		if self.y < 1:
			self.y = 1
			self.direction = (self.direction[0], -self.direction[1])
		if self.y + self.height > self.window.height - 1:
			self.y = self.window.height - 1 - self.height
			self.direction = (self.direction[0], -self.direction[1])

		collided = self.check_group_collision(self.window.obstacles)
		if collided:
			self.change_direction(collided)

		if self.is_collided_with(self.window.player) and self.window.player.state == "alive":
			self.window.player.state = "dead"
			for obj in self.window.obstacles:
				obj.reset()
			self.window.player.reset()

			self.window.refresh()