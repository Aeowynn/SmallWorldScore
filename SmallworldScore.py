# Smallworld Scoring App
# Kara James
# Began Spring 2014, continued implementing Spring 2015

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
		number = amount_response
		print "\nNumber of players: ", number, "\n"
	else:
		print "Error! Not a legal amount of players!"



# Calling Functions
Welcome()
