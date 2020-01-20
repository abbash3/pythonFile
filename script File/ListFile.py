#!/usr/bin/env python
import os
import glob

prin t "List Directory:" +str(os.listdir("."))
for itemDir in os.listdir("."):
    #print itemDir
    if os.path.isdir(itemDir) :
        print "List Directory:" + itemDir
        print os.listdir(itemDir)
        #if itemDir == os.path.isdir(itemDir) :
        #print os.listdir(itemDir)
