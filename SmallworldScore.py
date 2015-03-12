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

	#Display this message
	#Checking for unique player names not implemented yet
	print "For now, please use unique player names.\n"

	#This needs to be fixed
	# Ask amount of players
	amount_response = raw_input("First off, how many players are in this game? ")
	if int(amount_response) < 6 and 1 < int(amount_response):
		num = int(amount_response)
		print "\nNumber of players: ", num, "\n"
		return num
	else:
		print "\nError! Not a legal amount of players! Please enter a value 2-5."
		Welcome()

# Make classes for each player
def Setup_Players(num):
	print "\n * * * * * * * * * *\n"
	print "Now we'll set up the player list!"
	print "\n * * * * * * * * * *\n"
	temp = 1
	PList = []
	while num >= 1:
		print "Now requesting information for player", temp
		player_response = raw_input("Name for player? ")
		print "Recieved", player_response, "\n"
		#player = Player(player_response)
		PList.append(player_response)
		temp = temp + 1
		num = num - 1
	print "\n * * * * * * * * * *\n"
	print "Alright, game is set up for", temp-1, "players!"
	print "\n * * * * * * * * * *\n"
	return PList

def RoundSetter(length):
	if length == 2 or length == 3:
		return 10
	elif length == 4:
		return 9
	elif length == 5:
		return 8

def MainScreen(PlayerList, i):
	print PlayerList[i], "it is your turn."
	print "If", PlayerList[i], "spent gold this turn, please press 1."
	print "If", PlayerList[i], "stole gold this turn, please press 2."
	print "If", PlayerList[i], "is ready to score their turn, please press 3."
	response = int(raw_input("Your answer: "))
	if response == 1:
		SpentScreen(PlayerList, i)
	elif response == 2:
		StolenScreen(PlayerList, i)
	elif response == 3:
		UpdateScreen(PlayerList, i)
	else:
		print "Error; invalid answer."
		return

def StolenScreen(PlayerList, i):
	print "\n", PlayerList[i], "stole from how many players?"
	num = raw_input("Your answer: ")
	while num > 0:
		print "Which player did", PlayerList[i], "steal from?"
		player = raw_input("Your answer: ")
		#find that player
		print "How much did", PlayerList[i], "steal?"
		amt = raw_input("Your answer: ")
		#update player score
		#update active player's score
	
def SpentScreen(PlayerList, i):
	print "\n", PlayerList[i], "spent how much this turn? If you accidentally went to this prompt, press x to go back."
	dec = raw_input("Your answer: ")
	if dec == 'x':
		print "Recieved 'x'. Sending you back to previous screen.\n"
		MainScreen(PlayerList, i)
	elif int(dec) > 0:
		dec = 0 - int(dec)
		PlayerList[i].UpdateScore(dec)
		return
	else:
		print "Error, incorrect decrement value."
		return

def UpdateScreen(PlayerList, i):
	print "\n", PlayerList[i], "scored how many points this turn? If you accidentally went to this prompt, press x to go back."
	inc = raw_input("Your answer: ")
	if inc == 'x':
		print "Recieved 'x'. Sending you back to the previous screen.\n"
		MainScreen(PlayerList, i)
	elif int(inc) > 0:
		PlayerList[i].UpdateScore(inc)
		return
	else:
		print "Error, incorrect increment value."
	return

# Calling Functions
# Set value for number of players
NumberPlayers = Welcome()
PlayerList = Setup_Players(NumberPlayers)

print "CHECK: Now making objects."
j = 0
while j < len(PlayerList):
	print PlayerList[j]
	#need way of referencing it
	Player(PlayerList[j])
	j = j + 1

print "\n * * * * * * * * * *\n"
print "Now we'll set up the amount of rounds!"
print "\n * * * * * * * * * *\n"
rounds = RoundSetter(len(PlayerList))
#print "Alright! Now we just need to know how many rounds will be played."
#rounds = int(raw_input("Number of rounds? "))
print "Cool!", rounds, "rounds will be played.\n"

print "Before we start, here's some important information:"
print "Please enter in the changes in points in the order provided."
print "You will not be able to return to the spent or stolen screens after submitting the round score."
print "The stolen screen is only necessary for abilities in Underground and Be Not Afraid."
print "If you aren't playing with either of those, you can ignore the stolen option."

print "Alright, let's begin the game.\n"

#provide space for players to enter in score information
#per player per round
while rounds != 0:
	#Call update score
	# variable for keeping track of the current player
	i = 0
	current = 1
	print "It's now round", current,"\n"
	#Mainscreen will go to dec & inc for each player
	while i < len(PlayerList):
		MainScreen(PlayerList, i)
		i = i + 1
	rounds = rounds - 1
	current = current + 1

