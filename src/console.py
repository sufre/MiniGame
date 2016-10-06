#coding:utf-8

import cmd
import sys
import os

from src import game

class GameClient(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "input> "

    def do_new(self, arg):
        if arg == "":
            print "please input a new game name!"
        else:
            self.game = game.Game().new("./save/" + arg + ".save")
            self.prompt = arg + "> "
            print "new game success!"

    def do_load(self, arg):
        if arg == "":
            count = 0
            for root, dirs, files in os.walk("./save/"):
                for f in files:
                    count += 1
                    gameName = f[:f.find(".")]
                    print str(count) + ":" + gameName
        else:
            try:
                choice = int(arg)
                count = 0
                for root, dirs, files in os.walk("./save/"):
                    for f in files:
                        count += 1
                        if count == choice:
                            self.game = game.Game().load(os.path.join(root, f))
                            self.prompt = f[:f.find(".")] + "> "
                            print "load game " + self.prompt + " success!"
            except:
                print "Error input"
    
    def do_quit(self, arg):
        sys.exit(1)

    def do_info(self, arg):
        if self.game is not None:
            print self.game.info()
        else:
            print "please load game first!"

    #快捷键设置
    do_l = do_load
    do_q = do_quit