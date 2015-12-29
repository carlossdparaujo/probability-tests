from random import randint

class Dice:
	def __init__(self, number_of_sides):
		self.number_of_sides = number_of_sides

	def roll(self):
		return randint(1, self.number_of_sides)

class DishonestDice:
	def __init__(self, number_of_sides, dishonesty, dishonest_side):
		self.number_of_sides = number_of_sides
		self.dishonesty = dishonesty
		self.dishonest_side = dishonest_side

	def roll(self):
		dice_roll = randint(1, self.number_of_sides)

		if dice_roll > self.number_of_sides*self.dishonesty:
			return dice_roll
		else:
			return self.dishonest_side
