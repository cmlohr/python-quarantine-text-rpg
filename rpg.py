# python text rpg
# cmlohr

import cmd 
import textwrap
import sys
import os
import time
import random

screen_width = 100

###### Player Setup ######

class player:
def _init_(self):
	self.name = ''
	self.job = ''
	self.hp = 0
	self.mp = 0
	self.status_effects = []
	self.location = 'start'
	self.game_over = False
myPlayer = player()

##### Title Screen #####
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		start_game() # placeholder till written
	elif option.lower() == ("help"):
		help_menu()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid command.")
		option = input("> ")
		if option.lower() == ("play"):
			start_game() # 'nother placeholder
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()

def title_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	print('#########################')
	print('# Welcome to my TXT RPG!#')
	print('#########################')
	print('          -Play-         ')
	print('          -Help-         ')
	print('          -Quit-         ')
	print(' Coypyright 2020 @cmlohr ')
	title_screen_selections()

def help_menu():
	print('#########################')
	print('# Welcome to my TXT RPG!#')
	print('#########################')
	print('   Type your commands    ')
	print('  up, down, left, right  ')
	print('         to move         ')
	print('    "look" to inspect    ')
	print('        GOOD LUCK!       ')
	print(' Coypyright 2020 @cmlohr ')
	title_screen_selections()



##### GAME FUNCTIONALITY #####
def start_game():


##### MAP #####
"""
a1 a2... #PLAYER STARTS AT b2
-------------
|  |  |  |  | a4
-------------
|  |  |  |  | b4...
-------------
|  |  |  |  | 
-------------
|  |  |  |  | 
-------------
"""
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up','north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
				'b1': False, 'b2': False, 'b3': False, 'b4': False,
				'c1': False, 'c2': False, 'c3': False, 'c4': False,
				'd1': False, 'd2': False, 'd3': False, 'd4': False,
				}
######## FILL OUT MAP!!! ######
zonemap = {
	'a1': {
	ZONENAME: 'Spooky Woods',
	DESCRIPTION: 'These woods are spooky, no one has been here in a while.',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: '',
	DOWN: 'b1',
	LEFT: '',
	RIGHT: 'a2',
	},
	'a2': {
	ZONENAME: 'Sparce Woods',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: '',
	DOWN: 'b2',
	LEFT: 'a1',
	RIGHT: 'a3',
	},
	'a3': {
	ZONENAME: 'Clearing',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: '',
	DOWN: 'b3',
	LEFT: 'a2',
	RIGHT: 'a4',
	},
	'a4': {
	ZONENAME: 'Hobo Camp',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: '',
	DOWN: 'b4',
	LEFT: 'a3',
	RIGHT: '',
	},
	'b1': {
	ZONENAME: 'Blue House',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'a1',
	DOWN: 'c1',
	LEFT: '',
	RIGHT: 'b2',
	},
	'b2': {
	ZONENAME: 'My House',
	DESCRIPTION: 'This is your home!',
	EXAMINATION: 'Your home looks pretty shabby - someone should cut the grass.',
	SOLVED: False,
	UP: 'a2',
	DOWN: 'c2',
	LEFT: 'b1',
	RIGHT: 'b3',
	},
	'b3': {
	ZONENAME: 'Red House',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'a1',
	DOWN: 'c1',
	LEFT: '',
	RIGHT: 'b2',
	},
	'b4': {
	ZONENAME: 'Grey House',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'a4',
	DOWN: 'c4',
	LEFT: 'b3',
	RIGHT: '',
	},
	'c1': {
	ZONENAME: 'Armistice Apartments',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'b1',
	DOWN: 'd1',
	LEFT: '',
	RIGHT: 'c2',
	},
	'c2': {
	ZONENAME: 'Lava Lamps'
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'b2',
	DOWN: 'd2',
	LEFT: 'c1',
	RIGHT: 'c3',
	},
	'c3': {
	ZONENAME: 'Shiny Shoes'
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'a1',
	DOWN: 'c1',
	LEFT: '',
	RIGHT: 'b2',
	},
	'c4': {
	ZONENAME: 'Library',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'b4',
	DOWN: 'd4',
	LEFT: 'c3',
	RIGHT: '',
	},
	'd1': {
	ZONENAME: 'High School',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'c1',
	DOWN: '',
	LEFT: '',
	RIGHT: 'd2',
	},
	'd2': {
	ZONENAME: 'City Park',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'c2',
	DOWN: '',
	LEFT: 'd1',
	RIGHT: 'd3',
	},
	'd3': {
	ZONENAME: 'Spuds',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'c3',
	DOWN: '',
	LEFT: 'd2',
	RIGHT: 'd4',
	},
	'd4': {
	ZONENAME: 'Hammers-N-Stuff',
	DESCRIPTION: 'description',
	EXAMINATION: 'examine',
	SOLVED: False,
	UP: 'c4',
	DOWN: '',
	LEFT: 'd3',
	RIGHT: '',
	},
}

##### GAME INTERACTIVITY #####
def print_location()
	print('\n' + ('#' * (4 + len(myPLayer.location))))
	print('# ' + myplayer.location.upper() + ' #')
	print('# ' + zonemap[myPlayer.postion][DESCRIPTION])
	print('\n' + ('#' * (4 + len(myPLayer.location))))

def prompt():
	print("\n" + "======================")
	print("What would you like to do?")
	action = input("> ")
	acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
	while action.lower() not in acceptable_actions:
		print("Unknown action, try again.\n")
		action = input("> ")
	if action.lower() == "quit":
		sys.exit()
	elif action.lower() in ['move', 'go', 'travel', 'walk']:
		player_move(action.lower())
	elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
		player_examine(action.lower())

def player_move(myAction):
	ask = "Where would you like to move to?\n"
	dest = input(ask)
	if dest in ['up', 'north']:
		destination = zonemape[myPlayer.location][UP]
		movement_handler(destination)
	elif dest in ['left', 'west']:
		destination = zonemape[myPlayer.location][LEFT]
		movement_handler(destination)
	elif dest in ['east', 'right']:
		destination = zonemape[myPlayer.location][RIGHT]
		movement_handler(destination)
	elif dest in ['south', 'down']:
		destination = zonemape[myPlayer.location][DOWN]
		movement_handler(destination)

def movement_handler(destination):
	print("\n" + "You have moved to the " + destination + ".")
	myPlayer.location = desitination
	print_location()


def player_examine(action):
	if zonemap[myPlayer.location][SOLVED]:
		print("You have already explored this area")
	else:
		print("There's something here")



##### GAME FUNCTIONALITY #####
def start_game():
	return

def main_game_loop():
	while myPlayer.game_over is False:
		prompt()
	# here handle if puzzles have been solved, boss defeated, explored everything, etc.



def setup_game
os.system('clear')

##### NAME #####
question1 = "Hello, what's your name?\n"
for character in question1:
	sys.stdout.write(character)
	sys.stdout.flush()
	time.sleep(0.05)
	player_name = input("> ")
	myPlayer.name = player_name

##### Job #####
	question2 = "Hello, what's your job?\n"
	question2added = "(you can play as a warrior, priest or mage)\n"
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in question2added:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.01)
	player_job = input("> ")
	valid_jobs = ['warrior', 'mage', 'priest']
	if player_job.lower() in valid_jobs:
		myPlayer.job = player_job
		print("YOu are now " + player_job + "!\n")
	while player_job.lower() not in valid_jobs:
		player_job = input("> ")
		if player_job.lower() in valid_jobs:
			myPlayer.job = player_job
			print("you are now " + player_job + "!\n")


####Player Stats#####
	if myPlayer.job is 'warrior':
		self.hp = 120
		self.mp = 20
	elif myPlayer.job is 'mage':
		self.hp = 40
		self.mp = 120
	elif myPlayer.job is 'priest':
		self.hp = 60
		self.mp = 60

#### INTRO ####

	question3 = "Welcome, " + player_name + " the " + player_job ".\n"
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	player_name = input("> ")
	myPlayer.name = player_name

	speech1 = "Welcome to my world!"
	speech2 = "I hope you enjoy it!"
	speech3 = "Just make sure to not get sick..."
	speech4 = "Hehehehe..."
	for character in speech1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in speech2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in speech3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.01)
	for character in speech4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.02)
	os.system('clear')
	print('#########################')
	print('#     LET\'S PLAY!      #')
	print('#########################')
	main_game_loop()














title_screen()