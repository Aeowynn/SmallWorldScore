# Function Definitions
import playerObject

def Welcome():
	# Welcome/Startup function
	#	Sets number of players
	print "\n * * * * * * * * * *\n"
	print "Welcome to Smallworld Scoring App!"
	print "This app will keep track of each players' score as you play."
	
	print "\n * * * * * * * * * *\n"

	#Checking for unique player names not implemented yet
	print "For now, please use unique player names.\n"

	amount_response = raw_input("First off, how many players are in this game? ")
	if int(amount_response) < 6 and 1 < int(amount_response):
		num = int(amount_response)
		print "\nNumber of players: ", num, "\n"
		return num
	else:
		print "\nError! Not a legal amount of players! Please enter a value between 2-5."
		Welcome()

# Make classes for each player
def Setup_Players(num):
	print "\n * * * * * * * * * *\n"
	print "Now we'll set up the player list!"
	print "\n * * * * * * * * * *\n"
	temp = 1
	PlayerList = []
	while num >= 1:
		print "Now requesting information for player", temp
		player_response = raw_input("Name for player? ")
		print "Recieved", player_response, "\n"
		temp_player = playerObject.Player(player_response)
		PlayerList.append(temp_player)
		temp = temp + 1
		num = num - 1
	print "\n * * * * * * * * * *\n"
	print "Alright, game is set up for", temp-1, "players!"
	print "\n * * * * * * * * * *\n"
	return PlayerList

def Round_Setter(length):
	print "\n * * * * * * * * * *\n"
	print "Now we'll set up the amount of rounds!"
	print "\n * * * * * * * * * *\n"
	if length == 2 or length == 3:
		print "Cool! 10 rounds will be played.\n"
		return 10
	elif length == 4:
		print "Cool! 9 rounds will be played.\n"
		return 9
	elif length == 5:
		print "Cool! 8 rounds will be played.\n"
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
