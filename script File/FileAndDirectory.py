#!/usr/bin/env python
import os
for item in os.listdir("."):
    if os.path.isfile(item) :
        print item + "is a file"
    elif os.path.isdir(item):
        print item + "is a directory"
    else :
        print "unknow!"
