import pygame
import sys
import time
from player import Player
from ball import Ball

class Table:
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.Font(None, 32)  # Change None and 32 to your desired font file and size
		self.color = (255, 255, 255)  # Change to your desired color
		self.HEIGHT = 600  # Replace with the actual height value
		self.WIDTH = 800  # Replace with the actual width value
		self.score_limit = 5  # Replace with the actual score limit
		self.winner = None
		self._generate_world()

	def _generate_world(self):
		player_width = 100  # Replace with the actual value
		player_height = 200  # Define the player_height variable with the appropriate value
		self.playerA = Player(0, self.HEIGHT // 2 - (player_height // 2), player_width, player_height)
		self.playerB = Player(self.WIDTH - player_width,  self.HEIGHT // 2 - (player_height // 2), player_width, player_height)
		self.ball = Ball(self.WIDTH // 2 - player_width, self.HEIGHT - player_width, player_width)
		self.inst_font = pygame.font.SysFont('Bauhaus 93', 30)

	def _bot_opponent(self):
		if self.ball.direction == "left" and self.ball.rect.centery != self.playerA.rect.centery:
			if self.ball.rect.top <= self.playerA.rect.top:
				if self.playerA.rect.top > 0:
					self.playerA.move_up()
			if self.ball.rect.bottom >= self.playerA.rect.bottom:
				if self.playerA.rect.bottom < self.HEIGHT:
					self.playerA.move_bottom()

	def _ball_hit(self):
		if self.ball.rect.left >= self.WIDTH:
			self.playerA.score += 1
			self.ball.rect.x = self.WIDTH // 2
			time.sleep(1)
		elif self.ball.rect.right <= 0:
			self.playerB.score += 1
			self.ball.rect.x = self.WIDTH // 2
			time.sleep(1)

		if pygame.Rect.colliderect(self.ball.rect, self.playerA.rect):
			self.ball.direction = "right"
		if pygame.Rect.colliderect(self.ball.rect, self.playerB.rect):
			self.ball.direction = "left"

	def player_move(self):
		keys = pygame.key.get_pressed()

		self._bot_opponent()

		if keys[pygame.K_UP]:
			if self.playerB.rect.top > 0:
				self.playerB.move_up()
		if keys[pygame.K_DOWN]:
			if self.playerB.rect.bottom < self.HEIGHT:
				self.playerB.move_bottom()

	def _show_score(self):
		A_score, B_score = str(self.playerA.score), str(self.playerB.score)
		A_score = self.font.render(A_score, True, self.color)
		B_score = self.font.render(B_score, True, self.color)
		self.screen.blit(A_score, (self.WIDTH // 4, 50))
		self.screen.blit(B_score, ((self.WIDTH // 4) * 3, 50))

	def _game_end(self):
		if self.winner != None:
			print(f"{self.__init__} wins!!")
			pygame.quit()
			sys.exit()

	def update(self):
		self._show_score()

		self.playerA.update(self.screen)        
		self.playerB.update(self.screen)

		self._ball_hit()

		if self.playerA.score == self.score_limit:
			self.winner = "Opponent"

		elif self.playerB.score == self.score_limit:
			self.winner = "You"

		self._game_end()
		self.ball.update(self.screen)