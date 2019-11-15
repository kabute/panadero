import sys
from distutils.core import setup

VERSION = "0.1.0"
AUTHOR = 'Diego Montes'
DOWNLOAD_URL = '##DOWNLOAD_URL##'
requirements = []
tests_require = ['unittest2', 'tox', 'coverage']

if sys.version_info[0] != 3:
    print('You need to run this with Python 3.X', file=sys.stderr)

setup(
    name='##PROJECT##',
    version=VERSION,
    description='Panadero',
    author=AUTHOR,
    author_email='kabute@kabute.org',
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: System Administrators',
        'Topic :: Communications',
        'Topic :: Utilities'
    ]
)
