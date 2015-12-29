from dices import Dice
from dices import DishonestDice

def get_prob(use_dishonest_dice):
	if use_dishonest_dice:
		dice_game_test(DishonestDice(6, 0.6, 6))
	else:
		dice_game_test(Dice(6))

def dice_game_test(dice):
	total_rounds = 1000000
	three_dice_points = 0
	four_dice_points = 0

	for i in range(0, total_rounds):
		if three_dice_game(dice):
			three_dice_points += 1

		if four_dice_game(dice):
			four_dice_points += 1

	three_dice_prob = float(three_dice_points)/float(total_rounds)
	four_dice_prob = float(four_dice_points)/float(total_rounds)

	print("Three dice probability: " + str(three_dice_prob))
	print("Four dice probability: " + str(four_dice_prob))

def three_dice_game(dice):
	rolls = []

	for j in range(0, 3):
		rolls += [dice.roll()]

	if rolls[0] == rolls[1] == rolls[2]:
		return True
	else:
		return False

def four_dice_game(dice):
	rolls = []

	for j in range(0, 4):
		rolls += [dice.roll()]

	if rolls[0] == rolls[1] and rolls[2] == rolls[3]:
		return True
	else:
		return False

