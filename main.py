import random 
import hangman_art as hangman
import hangman_words as words


print(hangman.logo)

word_list = words.word_list
chosen_word = random.choice(word_list)
display = []
lives = 6
#testing
print(f"Choesen word is :  {chosen_word}")


for char in range(1, len(chosen_word) + 1):
	display.append("_")
print(display)

end_of_game = False

while not end_of_game:
	guess = (str(input("Guess the letter:>"))).lower()
	for position in range(len(chosen_word)):
		char = chosen_word[position]
		if char == guess:
			display[position] = char
			print(display)
	if guess not in chosen_word:
		lives -= 1
		print(f"Letter not in word, you lose a point: {lives} left")
		if lives == 0:
			end_of_game = True
			print("You've lost")
	if "_" not in display:
		end_of_game = True
		print(f" THE WORD IS: {' '.join(display).upper()} ")
		print("You've won")


	print(hangman.stages[lives])
			
	
		



