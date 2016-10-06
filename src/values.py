#coding:utf-8

#最大值以及一个0~最大值的变值
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

#原始值不可变，变值可正可负，计算值不可小于0
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