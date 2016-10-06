#coding:utf-8

import cmd
import sys
import os

from src import game

class GameClient(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = u"请输入命令: ".encode("GBK")

    def do_load(self, arg):
        if arg == "":
            count = 0
            for root, dirs, files in os.walk("./save/"):
                for f in files:
                    count += 1
                    gameName = f[:f.find(".")]
                    print str(count) + ":" + gameName.encode("GBK")
        else:
            try:
                choice = int(arg)
                count = 0
                for root, dirs, files in os.walk("./save/"):
                    for f in files:
                        count += 1
                        if count == choice:
                            self.game = game.Game().load(os.path.join(root, f))
                            print "读取游戏成功！".encode("GBK")
            except expression as identifier:
                print "Error input"
    
    
    def do_quit(self, arg):
        sys.exit(1)
    

    #快捷键设置
    do_l = do_load
    do_q = do_quit