from random import randint
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
		print('you did it! A was:' + a )
	else: 
		print('helaas pindakaas.\n Jij dacht: ' + str(guess) + 'maar het was: ' + str(a))

start()
