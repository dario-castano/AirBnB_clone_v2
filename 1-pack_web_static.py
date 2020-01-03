#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
import os
from fabric.api import *
from datetime import datetime

env.use_ssh_config = True


def do_pack():
    """Packs the folder web_static
    """
    now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    outpath = "./versions/web_static_{}".format(now)
    filename = "{}.tgz".format(outpath)
    local('sudo mkdir -p ./versions')
    local("tar -zcvf '{}' web_static".format(filename))

    if os.path.exists(filename):
        return outpath
    else:
        return None
