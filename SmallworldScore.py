# Smallworld Scoring App
# Kara James
# Began Spring 2014, continued implementing Spring 2015

NumberPlayers = 0

# Player class for keeping track of a player's score
class Player:
	PlayerName = "Unknown"
	score = 0

	def __init__(self, name):
		self.PlayerName = name

	def Update_Score(self, gain):
		print "Updating score for", self.PlayerName, " "
		self.score = self.score + int(gain)

# Function Definitions
# Welcome/Startup function
#	Sets number of players
def Welcome():
	# Print welcome message
	print "\n * * * * * * * * * *\n"
	print "Welcome to Smallworld Scoring App!"
	print "This app will keep track of each players' score as you play."
	
	print "\n * * * * * * * * * *\n"

	#Displau this message
	#Checking for unique player names not implemented yet
	print "For now, please use unique player names.\n"

	#This needs to be fixed
	# Ask amount of players
	amount_response = raw_input("First off, how many players are in this game? ")
	if int(amount_response) < 6 and 1 < int(amount_response):
		num = int(amount_response)
		print "\nNumber of players: ", num, "\n"
	else:
		print "Error! Not a legal amount of players!"
	return num

# Make classes for each player
def Setup_Players(num):
	temp = 1
	while num > 1:
		print "Hello!"
		temp = temp + 1
		print "Now making player", temp
		num = num - 1
		print "Num:", num
	print "Game is set up for", temp, "players!"

# Calling Functions
# Set value for number of players
NumberPlayers = Welcome()
Setup_Players(NumberPlayers)

print "Outside Num:", NumberPlayers
