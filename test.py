from src import *
import json

c = game.Creature("shanhao", 100, 10, 5)
b = game.BattleUnit()
b.activeTime = 14.3
bb = game.BattleUnit()
bb.activeTime = 1.0
bbb = game.BattleUnit()
bbb.activeTime = 5.0

t = game.BattleTime()
t.units.append(b)
t.units.append(bb)
t.units.append(bbb)
t.run()