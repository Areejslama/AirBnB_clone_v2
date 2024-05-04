#!/usr/bin/python3
"""this script to define pack function"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """define function"""
    t = datetime.now()
    arc = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + tgz
    local("mkdir -p versions")
    my_arc = "tar -czvf versions /{}".format(arc)
    if my_arc is not None:
        return my_arc
    else:
        return None

