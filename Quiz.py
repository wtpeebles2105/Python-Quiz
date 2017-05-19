# Here are the three steneces I came up with so that I could create the quiz.
easy_string = "Coding in __1__ can be __2__, but once you learn simple __3__ it can become __4__."
medium_string = "Python is just one __1__ in coding. You can create different __2__ with different __1__s. It just takes __3__ and __4__."
hard_string = "Using __1__ statements help create __2__ in your __3__. __2__ are useful when you need to keep checking a statement until it reaches the __4__ requirement. Good __4__ help computers complete all sorts of tasks."

# Here are the words I decided to omit to create quiz answers.
easy_answers = ["python", "difficult", "rules", "easy"]
medium_answers = ["language", "programs", "effort", "determination" ]
hard_answers = ["If", "loops", "code", "programs"]

# This is the difficulty selection, it will take your input and pull the corresponding string and answers from the lists above.
def level_selector():
	easy = ["easy", "Easy", "EASY"]
	medium = ["medium", "Medium", "MEDIUM"]
	hard = ["hard", "Hard", "HARD"]
	user_input = raw_input("Select your level of difficulty: easy / medium / hard" + "\n")
	if user_input in easy:
		print "\n" + easy_string
		return game_proper (easy_string, easy_answers)
	elif user_input in medium:
		print "\n" + medium_string
		return game_proper (medium_string, medium_answers)
	elif user_input in hard:
		print "\n" + hard_string
		return game_proper (hard_string, hard_answers)
	else:
		print "Try again." + "\n"
		level_selector ()

# This will slowly fill each part of the string with the answers the user chooses and then check them for accuracy. If it is correct it will move on to the next blank to fill in. It will trigger when it reaches the correct number between the __'s.
def game_proper(string, answers):
	index = 0
	while index < len(answers):
		user_input = raw_input("What is the answer to __" + str(index + 1) + "__ ?" + "\n")
		if user_input.lower() == answers[index].lower():
			print "Congratulations!" + "\n"
			index += 1
			string = string.replace("__" + str(index) + "__", user_input)
			print string
		else:
			print "Incorrect answer." + "\n" + string
	print "Good game!"

# This is the actual game, it pulls in the definitions from the other areas and runs them in order.
def play_game():
	level_selector()
	yes = ['yes', 'Y', 'YES', 'Yes','y']
	no = ['no', 'N', 'NO', 'No', 'n']
	user_input = raw_input("Play Again?: yes / no ")
	if user_input in yes:
		play_game()
	else:
		print "Thanks for playing!"

play_game()
