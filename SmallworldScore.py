# Smallworld Scoring App
# Kara James
# Began Spring 2014, continued implementing Spring 2015
import pygame
import playerObject
import functions

# Set amount of players
NumberPlayers = functions.Welcome()

# Make objects and list
Player_List = functions.Setup_Players(NumberPlayers)

# Set amount of rounds
rounds = functions.Round_Setter(NumberPlayers)

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

