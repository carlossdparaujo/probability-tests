from dices import Dice
from dices import DishonestDice

def get_prob(use_dishonest_dice):
	if use_dishonest_dice:
		test_given_prob(DishonestDice(6, 0.6, 6))
	else:
		test_given_prob(Dice(6))

def test_given_prob(dice):
	total_rounds = 1000000
	rounds_first_roll_equals_second = 0

	rounds_first_rolls_equals_seconds_and_third = 0
	rounds_first_rolls_equals_third = 0

	for i in range(0, total_rounds):
		rolls = []

		for j in range(0, 3):
			rolls += [dice.roll()]

		if rolls[0] == rolls[1]:
			rounds_first_roll_equals_second += 1

		if rolls[0] == rolls[2]:
			rounds_first_rolls_equals_third += 1
			if rolls[0] == rolls[1]:
				rounds_first_rolls_equals_seconds_and_third += 1


	first_rolls_equals_third_given_first_equals_second_prob = float(rounds_first_rolls_equals_seconds_and_third)/float(rounds_first_roll_equals_second)
	first_rolls_equals_third_prob = float(rounds_first_rolls_equals_third)/float(total_rounds)

	print("First == Third: " + str(first_rolls_equals_third_prob))
	print("First == Third | First == Second: " + str(first_rolls_equals_third_given_first_equals_second_prob))
