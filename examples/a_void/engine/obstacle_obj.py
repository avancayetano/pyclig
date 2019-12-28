import pyclig, random

class Obstacle(pyclig.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.dx = random.random() * random.choice([-1, 1])
		if self.dx == 0:
			self.dx = 0.5
		self.dy = (1 - self.dx ** 2) ** (1 / 2)


	def reset(self):
		self.x = self.init_xy[0]
		self.y = self.init_xy[1]
		self.dx = random.random() * random.choice([-1, 1])
		if self.dx == 0:
			self.dx = 0.5
		self.dy = (1 - self.dx ** 2) ** (1 / 2)
		self.speed = self.init_speed

	def update(self):
		self.x += self.dx * self.speed
		self.y += self.dy * self.speed
		self.speed = (self.window.player.score // 200) * 0.25 + 1
		self.check_bounds()


	def change_direction(self, other):
		temp_dx = self.dx
		temp_dy = self.dy
		self.dx = other.dx
		self.dy = other.dy
		other.dx = temp_dx
		other.dy = temp_dy

	def check_bounds(self):
		if self.x < 1:
			self.x = 1
			self.dx = -self.dx
		if self.x + self.width > self.window.width - 1:
			self.x = self.window.width - 1 - self.width
			self.dx = -self.dx
		if self.y < 1:
			self.y = 1
			self.dy = -self.dy
		if self.y + self.height > self.window.height - 1:
			self.y = self.window.height - 1 - self.height
			self.dy = -self.dy

		collided = self.check_group_collision(self.window.obstacles)
		if collided:
			self.change_direction(collided)

		if self.is_collided_with(self.window.player) and self.window.player.state == "alive":
			self.window.player.state = "dead"
			for obj in self.window.obstacles:
				obj.reset()
			self.window.player.reset()

			self.window.refresh()