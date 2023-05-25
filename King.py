import pygame
from Piece import Piece

class King(Piece):
	def __init__(self, x, y, color, board):
		super().__init__(x, y, color, board)
		img_path = f'images/{color}-king.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width, board.tile_height))
		self.notation = 'k'

	def _possible_moves(self):
		possible_moves = []
		for i in range(1, 8):  # Дозволити переміщення на будь-яку кількість клітинок
			possible_moves.extend([(-i, -i), (+i, -i), (-i, +i), (+i, +i)])
		return possible_moves

	def valid_moves(self):
		tile_moves = []
		moves = self._possible_moves()
		for move in moves:
			tile_pos = (self.x + move[0], self.y + move[1])
			while 0 <= tile_pos[0] <= 7 and 0 <= tile_pos[1] <= 7:
				tile = self.board.get_tile_from_pos(tile_pos)
				if tile.occupying_piece is None:
					tile_moves.append(tile)
				else:
					break  # Зупиняємо перевірку, якщо зустрічаємо фігуру
				tile_pos = (tile_pos[0] + move[0], tile_pos[1] + move[1])
		return tile_moves


	def valid_jumps(self):
		tile_jumps = []
		moves = self._possible_moves()
		for move in moves:
			tile_pos = (self.x + move[0], self.y + move[1])
			while 0 <= tile_pos[0] < 8 and 0 <= tile_pos[1] < 8:
				tile = self.board.get_tile_from_pos(tile_pos)
				if tile.occupying_piece is not None:
					if tile.occupying_piece.color != self.color:
						next_pos = (tile_pos[0] + move[0], tile_pos[1] + move[1])
						while 0 <= next_pos[0] < 8 and 0 <= next_pos[1] < 8:
							next_tile = self.board.get_tile_from_pos(next_pos)
							if next_tile.occupying_piece is None:
								tile_jumps.append((next_tile, tile))
								next_pos = (next_pos[0] + move[0], next_pos[1] + move[1])
							else:
								break
					break
				tile_pos = (tile_pos[0] + move[0], tile_pos[1] + move[1])
		return tile_jumps
