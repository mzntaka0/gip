# -*- coding: utf-8 -*-
"""
"""
import subprocess


def get_global_ip():
    global_ip = subprocess.run(
            ['curl', 'ifconfig.io'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).stdout.decode().replace('\n', '')
    return global_ip
