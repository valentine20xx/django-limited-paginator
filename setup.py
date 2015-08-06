# -*- coding: utf-8 -*-
from distutils.core import setup

VERSION = "0.0.1"

setup(
    name="django-limited-paginator",
    version=VERSION,
    packages=["limited_paginator"],
    # url = "https://github.com/alrusdi/django_digg_paginator",
    author="Nikolai Morozov",
    author_email="morozovns89@gmail.com",
    # maintainer = "alrusdi",
    # maintainer_email = "alrusdi@gmail.com",
    license="GPL3",
    # description = "Digg-like Paginator from Django Snippets",
    # long_description = open("README", "r").read(),
    # download_url = "https://github.com/alrusdi/django_digg_paginator/archive/master.zip",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)