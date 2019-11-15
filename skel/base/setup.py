from __future__ import print_function
import sys
from distutils.core import setup

VERSION = "0.1.0"
AUTHOR = 'Diego Montes'
DOWNLOAD_URL = '##DOWNLOAD_URL##'
requirements = []
tests_require = ['unittest2', 'tox', 'coverage']

if sys.version_info[0:2] != (2, 7):
    print('You need to run this with Python 2.7', file=sys.stderr)

setup(
    name='##PROJECT##',
    version=VERSION,
    description='Project description',
    author=AUTHOR,
    author_email='email',
    url=DOWNLOAD_URL,
    download_url=DOWNLOAD_URL,
    license='MIT',
    packages=["##PROJECT##"],
    entry_points="""\
    [console_scripts]
    ##PROJECT## = ##PROJECT##:main
    """,
    install_requires=requirements,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: System Administrators',
        'Topic :: Communications',
        'Topic :: Utilities'
    ]
)
