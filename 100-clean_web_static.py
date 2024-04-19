#!/usr/bin/python3
# fabfile to delete out-of-date archives

import os
from fabric.api import *

env.hosts = ["54.236.51.196", "35.153.83.101"]


def do_clean(number=0):
    """Delete out-of-date archives"""

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm {}".format(os.path.join("versions", a))) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf {}".format(os.path.join("/data/web_static/releases", a))) for a in archives]
