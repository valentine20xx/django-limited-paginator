# -*- coding: utf-8 -*-
from distutils.core import setup

VERSION = "0.0.1"

setup(
    name="django-limited-paginator",
    version=VERSION,
    packages=["limited_paginator"],
    url = "https://github.com/valentine20xx/django-limited-pagginator",
    author="Nikolai Morozov",
    author_email="morozovns89@gmail.com",
    license="GPL3",
    description = "Limited Paginator",
    long_description = open("README", "r").read(),
    download_url = "https://github.com/valentine20xx/django-limited-pagginator/archive/master.zip",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
