# Smallworld Scoring App
# Kara James
# Began Spring 2014, continued implementing Spring 2015

NumberPlayers = 0
PlayerList = []

# Player class for keeping track of a player's score
class Player:
	PlayerName = "Unknown"
	score = 0

	def __init__(self, name):
		self.PlayerName = name

	def UpdateScore(self, gain):
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
	PList = []
	while num >= 1:
		print "Now requesting information for player", temp, "\n"
		player_response = raw_input("Name for player? ")
		print "Recieved", player_response, "\n"
		#player = Player(player_response)
		PList.append(player_response)
		temp = temp + 1
		num = num - 1
	print "Game is set up for", temp-1, "players!"
	return PList

def MainScreen(PlayerList, i):
	print PlayerList[i], "it is your turn."
	print "If", PlayerList[i], "spent gold this turn, please press 1."
	print "If", PlayerList[i], "is ready to score their turn, please press 2."
	response = int(raw_input("Your answer: "))
	if response == 1:
		SpentScreen(PlayerList, i)
	elif response == 2:
		UpdateScreen(PlayerList, i)
	else:
		print "Error; invalid answer."
		return
		
def SpentScreen(PlayerList, i):
	print PlayerList[i], "spent how much this turn? If you accidentally went to this prompt, press x to go back."
	dec = raw_input("Your answer: ")
	if dec == 'x':
		print "Recieved 'x'. Sending you back to previous screen."
		MainScreen(PlayerList, i)
	elif int(dec) > 0:
		dec = 0 - int(dec)
		PlayerList[i].UpdateScore(dec)
		return
	else:
		print "Error, incorrect decrement value."
		return

def UpdateScreen(PlayerList, i):
	print PlayerList[i], "scored how many points this turn? If you accidentally went to this prompt, press x to go back."
	inc = raw_input("Your answer: ")
	if inc == 'x':
		print "Recieved 'x'. Sending you back to the previous screen."
	
	return

# Calling Functions
# Set value for number of players
NumberPlayers = Welcome()
PlayerList = Setup_Players(NumberPlayers)

print "Now making objects."
j = 0
while j < len(PlayerList):
	print PlayerList[j]
	#need way of referencing it
	Player(PlayerList[j])
	j = j + 1

#This can be hardcoded in; may be different for base vs underground?
print "Alright! Now we just need to know how many rounds will be played."
round_response = int(raw_input("Number of rounds? "))
print "Cool!", round_response, "rounds will be played."

#provide space for players to enter in score information
#per player per round
while round_response != 0:
	#Call update score
	i = 0
	MainScreen(PlayerList, i)

