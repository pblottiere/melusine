# -*- coding: utf-8 -*-
from setuptools import setup

requirements = (
    'cliff',
    'owslib'
)

setup(
    name="mscli",
    version="0.1",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'mscli = mscli.main:main'
            ],
        'mscli': [
            'connect = mscli.connect:Connect',
            'disconnect = mscli.connect:Disconnect',
            'info = mscli.info:Info',
            'layers = mscli.layers:Layers',
            'operations = mscli.ops:Operations',
            'servers = mscli.servers:Servers',
            'map = mscli.map:Map',
            'formats = mscli.formats:Formats'
            ],
        },
)
