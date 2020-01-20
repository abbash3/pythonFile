#!/usr/bin/env python
import os
def child_process () :
    print "Child Process PID: %d"%os.getpid()

def Parent_process() :
    print "Parent Process PID: %d" %os.getpid()
    childpid = os.fork()
    if chilpid == 0 :
        child_process()
    else :
        print "Our child has the PID : %d"%childpid
    while Ture:
        pass
Parent_process()
