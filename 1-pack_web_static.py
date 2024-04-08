#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    local("mkdir -p versions/")

    now = datetime.now()
    nameAr = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    result = local("tar czvf {} web_static".format(nameAr))

    if result.succeeded:
        return nameAr
    else:
        return None
