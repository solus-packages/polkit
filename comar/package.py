#!/usr/bin/python

import os, re

OUR_ID = 27
OUR_NAME = "polkitd"
OUR_DESC = "PolicyKit Daemon"
OUR_HOME = "/var/empty"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system ("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system ("useradd -m -d %s -r -s /bin/false -u %d -g %d %s -c \"%s\"" % (OUR_HOME, OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))
    except:
        pass

def postRemove():
    try:
        os.system ("userdel %s" % OUR_NAME)
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass
