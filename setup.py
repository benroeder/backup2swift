# -*- coding: utf-8 -*-
"""
    Copyright (C) 2013 Kouhei Maeda <mkouhei@palmtb.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys

from setuptools import setup, find_packages

sys.path.insert(0, 'src')
import backup2swift

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Programming Language :: Python",
    "Topic :: Internet",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Environment :: OpenStack",
]

long_description = \
        open(os.path.join("docs","README.rst")).read() + \
        open(os.path.join("docs","TODO.rst")).read() + \
        open(os.path.join("docs","HISTORY.rst")).read()

if sys.version_info > (2, 6) and sys.version_info < (2, 7):
    requires = ['setuptools', 'swiftsc', 'argparse']
elif sys.version_info > (2, 7):
    requires = ['setuptools', 'swiftsc']

setup(name='backup2swift',
      version=backup2swift.__version__,
      description='Backup data to OpenStack Swift',
      long_description=long_description,
      author='Kouhei Maeda',
      author_email='mkouhei@palmtb.net',
      url='https://github.com/mkouhei/backup2swift',
      license=' GNU General Public License version 3',
      classifiers=classifiers,
      packages=find_packages('src'),
      package_dir={'': 'src'},
      data_files=[('share/backup2swift/examples', ['examples/bu2sw.conf', 'examples/bu2sw_ignore_verify.conf'])],
      install_requires=requires,
      extras_require=dict(
        test=[
            'pytest',
            'pep8',
            'mock',
            ],
        ),
      test_suite='tests',
      tests_require=['pytest','pep8','mock'],
      entry_points={
        "console_scripts": [
            "bu2sw = backup2swift.command:main",
            ]
        },
)
