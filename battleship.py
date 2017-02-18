import string
import os
import time
import copy
class Ship:
	def __init__(self, length, bow):
		self.length = length
		self.bow = bow
		self.hit = [False for i in range(sum(self.length) - 1)]
class Field:
	def __init__(self):
		import random
		points = [(i, j) for i in range(10) for j in range(10)]
		field = [[' ' for i in range(10)] for i in range(10)]
		check = []
		for ship in range(4, 0, -1):
			repeat = ship
			while repeat != 5:
				direction = random.choice((1,2))
				if direction == 1:
					while True:
						point = random.choice(points)
						g_ship = Ship((1, ship), point)
						for i in range(ship):
							if ((g_ship.bow[0]), (g_ship.bow[1] + i)) not in points:
								check = []
								break
							if ((g_ship.bow[0]), (g_ship.bow[1] + i)) in points:
								check.append(((g_ship.bow[0]), (g_ship.bow[1] + i)))
						if check == []:
							continue
						check = []
						for i in range(3):
							for k in range(ship + 2):
								if ((g_ship.bow[0] - 1 + i), (g_ship.bow[1] - 1 + k)) in points:
									check.append(((g_ship.bow[0] - 1 + i), (g_ship.bow[1] - 1 + k)))
						for i in check:
							points.remove(i)
						check = []
						for i in range(ship):
							field[g_ship.bow[0]][g_ship.bow[1] + i] = g_ship
						break
				if direction == 2:
					while True:
						point = random.choice(points)
						g_ship = Ship((ship, 1), point)
						for i in range(ship):
							if ((g_ship.bow[0] + i), (g_ship.bow[1])) not in points:
								check = []
								break
							if ((g_ship.bow[0] + i), (g_ship.bow[1])) in points:
								check.append(((g_ship.bow[0] + i), (g_ship.bow[1])))
						if check == []:
							continue
						check = []
						for i in range(3):
							for k in range(ship + 2):
								if ((g_ship.bow[0] - 1 + k), (g_ship.bow[1] - 1 + i)) in points:
									check.append(((g_ship.bow[0] - 1 + k), (g_ship.bow[1] - 1 + i)))
						for i in check:
							points.remove(i)
						check = []
						for i in range(ship):
							field[g_ship.bow[0] + i][g_ship.bow[1]] = g_ship
						break
				repeat += 1
		return field
class Player:
	def __init__(self):
		name = str(input("What's your name?: "))
		self.name = name
class Game:
	def __init__(self):
		Player.__init__(self)
		self.field = Field.__init__(self)
		self.ls = ls = [[' ' for i in range(10)] for i in range(10)]
		self.check = 'oops'
	def read_position(self):
		strike = str(input(self.name + ', enter move: '))
		if type(self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())]) == Ship:
			if self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].length[0] == 1:
				k = self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].bow[1] - string.ascii_letters.index(strike[0].lower())
				self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].hit[k] = True
			else:
				k = self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].bow[0] - int(strike[1]) - 1
				self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].hit[k] = True
		return strike
	def field_without_ships(self):
		strike = Game.read_position(self)
		time.sleep(1)
		if type(self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())]) == Ship:
			self.ls[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())] = 'X'
			self.check = 'checked'
		else:
			self.ls[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())] = '0'
			self.check = 'oops'
		fin = ""
		for i in self.ls:
			for k in i:
				fin += k
			fin += '\n'
		print(fin)
	def field_with_ships(self):
		field = copy.deepcopy(self.field)
		for i in range(len(field)):
			for j in range(len(field[i])):
				if type(field[i][j]) == Ship:
					if field[i][j].length[0] == 1:
						if field[i][j].hit[field[i][j].bow[1] - j] == True:
							field[i][j] = 'X'
						else:
							field[i][j] = '*'
					else:
						if field[i][j].hit[field[i][j].bow[0] - i] == True:
							field[i][j] = 'X'
						else:
							field[i][j] = '*'
		st = field
		fin = ""
		for i in st:
			for k in i:
				fin += k
			fin += '\n'
		print(fin)

player1 = Game()
print('')
player2 = Game()
time.sleep(0.5)
print('')
print('Field of the first player')
player2.field_with_ships()
time.sleep(4)
os.system('cls')
time.sleep(1)
print('')
print('Field of the second player')
player1.field_with_ships()
time.sleep(4)
os.system('cls')
time.sleep(2)
while True:
	print('First player')
	player2.field_with_ships()
	player1.field_without_ships()
	while player1.check == 'checked':
		time.sleep(1)
		os.system('cls')
		time.sleep(0.5)
		print('First player')
		player2.field_with_ships()
		player1.field_without_ships()
	time.sleep(1)
	os.system('cls')
	time.sleep(0.5)
	print('Second player')
	player1.field_with_ships()
	player2.field_without_ships()
	while player2.check == 'checked':
		time.sleep(1)
		os.system('cls')
		time.sleep(0.5)
		print('Second player')
		player1.field_with_ships()
		player2.field_without_ships()
	time.sleep(1)
	os.system('cls')
	time.sleep(0.5)