#!/usr/bin/python3
"""this script to define pack function"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """define function"""
    t = datetime.now()
    arc = 'web_static_' + t.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    my_arc = local('tar -czvf versions/{} web_static'.format(arc))
    if my_arc is not None:
        return arc
    else:
        return None
