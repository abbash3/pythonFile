#!/usr/bin/env python
import glob
import os
for item in glob.glob(os.path.join(".","*")) :
    print item
