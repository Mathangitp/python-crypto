#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "crypto",
    version = "1.0.0",
    url = 'http://ondrejsika.com/docs/python-crypto',
    download_url = 'https://bitbucket.org/sikaondrej/python-crypto',
    license = 'GNU LGPL v.3',
    description = "Simply tool for cryptography",
    author = 'Ondrej Sika',
    author_email = 'dev@ondrejsika.com',
    packages = find_packages(),
    install_requires = ["rsa"],
    include_package_data = True,
)
