#!/usr/bin/python3
"""this script to define pack function"""
from datetime import datetime
from fabric.api import *
from os.path import isdir, exists


env.hosts = ['3.89.155.41', '54.208.154.58']
def do_pack():
    """define function"""
    t = datetime.now()
    arc = 'web_static_' + t.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    if isdir ('versions') is False:
        local('mkdir -p versions')
    my_arc = local('tar -czvf versions/{} web_static'.format(arc))
    if my_arc is not None:
        return arc
    else:
        return None

def do_deploy(archive_path):
    """Define deploy."""
    if exists(archive_path) is False:
        return False
    try:
        new_arc = archive_path.split("/")[-1]
        new_name = new_arc.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, new_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(new_arc, path, new_name))
        run('rm /tmp/{}'.format(new_arc))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, new_name))
        run('rm -rf {}{}/web_static'.format(path, new_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, new_name))
        return True
    except Exception:
        return False
def deploy():
    """create path"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy( archive_path)

