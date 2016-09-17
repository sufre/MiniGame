from operator import itemgetter, attrgetter
from values import AltValue, AddValue

import config
import json
import os


class Creature():
	def __init__(self, name, hp, atk, dfs):
		self.hp = AltValue(hp)
		self.atk = AddValue(atk)
		self.dfs = AddValue(dfs)

class BattleUnit():
	def __init__(self):
		self.activeTime = 0.0

	def __str__(self):
		return str(self.activeTime)

	def active(self):
		pass

class BattleTime():
	def __init__(self):
		self.units = []

	def run(self):
		while (len(self.units) >= 2):
			unit = self.units[0]
			unit.active()
			self.units.sort(key=attrgetter('activeTime'))
			for u in self.units:
				print u
			self.units = []

class Game():
	def __init__(self, name=""):
		files = os.listdir(config.savePath)
		for f in files:
			print f + " "
		print "\n"
		if name == "":
			characterName = input("New Game Character Name:\n")
			print characterName
			self.sfile = os.path.join(config.savePath, characterName)
			print self.sfile
		else:
			self.sfile = os.path.join(config.savePath, name)
		self.load(self.sfile)

	def load(self):
		with open(self.sfile, "rb") as saveFile:
			self.data = json.loads(saveFile.read())

	def save(self):
		with open(self.sfile, "wb") as saveFile:
			saveFile.write(json.dumps(self.data))