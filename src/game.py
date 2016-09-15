from operator import itemgetter, attrgetter
print 'hello'

class AltValue():
	def __init__(self, v):
		self.max = v
		self.v = v

	def __str__(self):
		return str(self.v)

	def __sub__(self, other):
		self.v = self._change(-other)
		return self.v

	def __add__(self, other):
		self.v = self._change(other)
		return self.v

	def _change(self, other):
		v = self.v + other
		if v > self.max:
			self.v = self.max
		elif v < 0:
			self.v = 0
		else:
			self.v = v
		return self.v

class AddValue():
	def __init__(self, v):
		self.v = v
		self.add = 0

	def __str__(self):
		return str(self.v + self.add)

	def __sub__(self, other):
		return self.v + self._change(-other)

	def __add__(self, other):
		return self.v + self._change(other)

	def _change(self, v):
		if v < 0 and abs(v) > self.v:
			self.add = -self.v
		else:
			self.add = v
		return self.add

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

c = Creature("shanhao", 100, 10, 5)
b = BattleUnit()
b.activeTime = 14.3
bb = BattleUnit()
bb.activeTime = 1.0
bbb = BattleUnit()
bbb.activeTime = 5.0

t = BattleTime()
t.units.append(b)
t.units.append(bb)
t.units.append(bbb)
t.run()

