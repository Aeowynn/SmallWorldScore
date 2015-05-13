#Player Class

class Player:
	# Player class for keeping track of a player's score
	PlayerCount = 0

	def __init__(self, name):
		self.player_name = name
		self.player_score = 0
		# for referencing...?
		self.player_ID = Player.PlayerCount
		Player.PlayerCount += 1

	def UpdateScore(self, gain):
		print "Updating score for", self.player_name, " "
		self.player_score = self.player_score + int(gain)
