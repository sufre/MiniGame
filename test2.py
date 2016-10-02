

class ObjectDict(dict):
    """Makes a dictionary behave like an object, with attribute-style access.
    """

    def __getattr__(self, name):
        print 2
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        print 3
        self[name] = value

    def __init__(self, m):
        print 1
        self = m
        #print self.a
    
    def load(self, m):
        self = m

    def test(self):
        self.a = "bb"
        print self.a

o = ObjectDict(1)
#o.a = 'aa'
o.update({"a":"aa"})
o.test()
print o

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