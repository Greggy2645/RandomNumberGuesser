from random import randint
import time
begin = input('aight we gonna play a guess the number game. \n If you guesss the number right\n then you get a balloon. \nType start to begin.\n')

def start():
	if begin == 'start':
		chosenNumber()
	else:
		print('you retard that isnt start')
def chosenNumber():
	chosenNumber = int(input('choose a number:\n'))
	a = randint(0, chosenNumber)
	guess = int(input('guess the random number here:\n'))
	if a == guess:
		print('you did it!')
		start()
	else: 
		print('helaas pindakaas.\n You thought: ' + str(guess) + '\nbut it was: ' + str(a))
		time.sleep(0)
		print('you dumb fuck')
		exit()
start()
