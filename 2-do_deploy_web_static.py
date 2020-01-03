#!/usr/bin/python3
"""
Deploys the tar which has the static codebase
"""
import re
import os
from fabric.api import *
from datetime import datetime

env.use_ssh_config = True
env.hosts = ['35.229.53.195', '35.190.175.59']


def do_pack():
    """Packs the folder web_static
    """
    now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    outpath = "./versions/web_static_{}".format(now)
    filename = "{}.tgz".format(outpath)
    local('mkdir -p ./versions')
    local("tar -zcvf '{}' web_static".format(filename))

    if os.path.exists(filename):
        return outpath
    else:
        return None


def do_deploy(archive_path):
    """Deploys to the nodes
    """
    if os.path.exists(archive_path):
        tar_name = re.search('web_static_[0-9]*.tgz', archive_path).group(0)
        untar_path = "/data/web_static/releases/{}"\
            .format(tar_name.replace('.tgz', ''))

        put(archive_path, '/tmp')
        run("mkdir -p {}".format(untar_path))
        run("tar -zxf /tmp/{} -C {}".format(tar_name, untar_path))
        run("rm /tmp/{}".format(tar_name))
        run("mv {}/web_static/* {}".format(untar_path, untar_path))
        run("rm -rf {}/web_static".format(untar_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(untar_path))
        print('New version deployed!')
    else:
        return False
