import sys, os, time
sys.path.append(sys.path[0] + "/../..") # now this is ugly as shit, i know

import pyclig
from engine import player_obj, obstacle_obj, button
from pynput import keyboard

class GameWindow(pyclig.window.Window):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.title = pyclig.label.Label(window=self, text="< == A VOID == >", x=self.width // 2, y=15, anchor="center")
		buttons_text = ["PLAY", "HELP", "QUIT"]
		self.buttons = [button.Button(window=self, text=txt, x=self.width // 2, y=20 + idx, anchor="center") 
			for idx, txt in enumerate(buttons_text)]
		self.buttons[0].active = True
		self.player = player_obj.Player(window=self, x=self.width // 2, y=self.height // 2, width=5, height=3, dx=0, dy=0, char="#", speed=1)
		self.score = pyclig.label.Label(window=self, text="SCORE: {}".format(self.player.score), x=0, y=self.height - 1)
		self.obstacles_number = 8
		coordinates = self.generate_obs_pos(self.obstacles_number)
		self.obstacles = [obstacle_obj.Obstacle(window=self, x=coordinates[i][0], y=coordinates[i][1], width=4, height=2, char="0") 
			for i in range(self.obstacles_number)]

		self.listener = keyboard.Listener(on_press=self.player.on_press, on_release=self.player.on_release)
		self.listener.start()

	def generate_obs_pos(self, number):
		coordinates = []
		x_interval = (self.width - 2) // ((number // 2))
		x = x_interval // 2
		for i in range(number):
			if i < number // 2:
				coordinates.append([x + x_interval * i, 2])
			else:
				coordinates.append([x + x_interval * (i - number // 2), self.height - 4])
		return coordinates

	def run(self):
		while True:			
			if self.player.state == "dead":
				self.update(self.title, self.score, *self.buttons)
			else:
				self.update(self.player, self.score, *self.obstacles)
			

if __name__ == "__main__":
	window = GameWindow(width=130, height=40, char=" ", fps=30)
	window.run()