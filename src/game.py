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

class Game(dict):
	def __getattr__(self, name):
		try:
			return self[name]
		except KeyError:
			raise AttributeError(name)
			
	def __setattr__(self, name, value):
		self[name] = value

	def new(self, saveFile):
		self.saveFile = saveFile
		self.save()
		return self

	def load(self, saveFile):
		with open(saveFile, "rb") as sfile:
			self.update(json.loads(sfile.read()))
		return self

	def save(self):
		with open(self.saveFile, "wb") as sfile:
			sfile.write(json.dumps(self, default=lambda obj: obj.__dict__))
		return self