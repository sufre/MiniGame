#coding:utf-8
from operator import itemgetter, attrgetter
from values import AltValue, AddValue

import config
import json
import os


class Creature():
	def __init__(self, name, itl, bod, hp, mp, atk, dfs, spd):
		#悟性、根骨，不自然成长
		self.itl = AddValue(itl)
		self.bod = AddValue(bod)

		#血量、攻击力，升级成长
		self.hp = AltValue(hp)
		self.atk = AddValue(atk)

		#内力、防御、速度，修炼成长
		self.mp = AltValue(mp)
		self.dfs = AddValue(dfs)
		self.spd = AddValue(spd)

class BattleUnit():
	def __init__(self):
		self.activeTime = 0.0
		self.pos = (0,0)

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
	
	def load(self, saveFile):
		with open(saveFile, "rb") as sfile:
			self.update(json.loads(sfile.read()))
		return self

	def save(self):
		with open(self.saveFile, "wb") as sfile:
			sfile.write(json.dumps(self, default=lambda obj: obj.__dict__))
		return self

	def new(self, saveFile):
		self.saveFile = saveFile
		self.gold = 0
		self.members = []
		self.teams = []
		self.houses = []
		self.save()
		return self

	def info(self):
		return \
		"\tgold: " + str(self.gold) + "\n" +\
		"\tmembers: " + str(len(self.members)) + "\n" +\
		"\tteams: " + str(len(self.teams)) + "\n" +\
		"\thouses: " + str(len(self.houses))