#!/usr/bin/python3
"""This script is for deployment."""
from fabric.api import run, put, env
from os.path import exists

env.hosts = ['3.89.155.41', '54.208.154.58']

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
    except:
        return False
