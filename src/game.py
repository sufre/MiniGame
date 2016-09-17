from operator import itemgetter, attrgetter
from values import AltValue, AddValue

print 'hello'



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



