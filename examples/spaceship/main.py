import sys, os, time, random

# warning: hard-coded shit below: 
sys.path.append(sys.path[0] + "/../..") # cause main.py is two directories away from the pyclig package


import pyclig
from engine import player_obj, asteroid, button
from pynput import keyboard

class GameWindow(pyclig.window.Window):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.title = pyclig.label.Label(window=self, text="< == SPACE == >", x=self.width // 2, y=15, anchor="center")
		buttons_text = ["PLAY", "QUIT"]
		self.buttons = [button.Button(window=self, text=txt, x=self.width // 2, y=20 + idx, anchor="center") 
			for idx, txt in enumerate(buttons_text)]
		self.buttons[0].active = True
		self.player = player_obj.Player(window=self, x=self.width // 2, y=self.height - 4, direction=(0, 0), speed=(2, 1), 
			image=pyclig.util.load_image("resources/spaceship.txt"))
		asteroid_img = pyclig.util.load_image("resources/obstacles.txt")
		self.asteroids = [asteroid.Asteroid(window=self, x=random.randrange(1, self.width - 1 - asteroid_img.width), 
			y=random.randrange(-asteroid_img.height - 20, -asteroid_img.height),
			direction=(0, 1), speed=(0, 1), image=asteroid_img) for i in range(4)]
		self.score = pyclig.label.Label(window=self, text="SCORE: {}".format(self.player.score), x=0, y=self.height - 1)

		self.listener = keyboard.Listener(on_press=self.player.on_press, on_release=self.player.on_release)
		self.listener.start()


	def run(self):
		while True:
			if time.time() - self.clock > 1 / self.fps:
				os.system("clear")
				self.refresh()
				self.score.update()
				self.score.render()
				if self.player.state == "dead":
					self.title.render()
					for btn in self.buttons:
						btn.update()
						btn.render()
				else:
					self.player.update()
					self.player.render()
					for ast in self.asteroids:
						ast.update()
						if self.player.state == "dead":
							break
						ast.render()

				self.draw()
				self.clock = time.time()

			

if __name__ == "__main__":
	window = GameWindow(width=130, height=50, char=" ", fps=60)
	window.run()