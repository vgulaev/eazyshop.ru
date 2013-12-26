# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("/var/lib/stickshift/529c40574382ecb58e00000c/app-root/data/682633/cgi")
sys.path.append("/var/lib/stickshift/529c40574382ecb58e00000c/app-root/data/682633/ezshp")
#import ezshp.myadmin.initdb

#d = ezshp.myadmin.initdb.dbworker(dbuser=os.environ['C9_USER'])
#d.doinitdb()
import socket
print(socket.gethostname())

#sys.path.append(settings.SITE_ROOT + "/ezshp")