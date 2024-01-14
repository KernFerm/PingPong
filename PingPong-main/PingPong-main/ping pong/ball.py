import pygame, sys, random
from settings import WIDTH, HEIGHT


pygame.init()

class Ball:
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
		self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
		self.color = pygame.Color("white")
		self.direction = "right" # or "left" depending on the initial direction
		self.speed_x = 11
		self.speed_y = 11
		self._random_direction()

	def _random_direction(self):
		direction = ("right", "left")
		self.direction = random.choice(direction)

	def _ball_movement(self):
		# horizontal handling
		if self.direction == "right":
			self.rect.x += self.speed_x
		else:
			self.rect.x -= self.speed_x

		# vertical handling
		if self.rect.y >= HEIGHT - self.radius:
			self.speed_y = -11
		elif self.rect.y <= 0 + self.radius:
			self.speed_y = 11

		# wall bounce handling
		self.rect.y += self.speed_y

	def update(self, screen):
		self._ball_movement()
		pygame.draw.circle(screen, self.color, (self.rect.x, self.rect.y), self.radius)