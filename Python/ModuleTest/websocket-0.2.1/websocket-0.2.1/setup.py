#!/usr/bin/env python
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = re.search("__version__\s*=\s*'(.*)'", open('websocket/__init__.py').read(), re.M).group(1)
assert __version__


if __name__ == '__main__':
    setup(
        name='websocket',
        version=__version__,
        description='Websocket implementation for gevent',
        url='http://pypi.python.org/pypi/websocket',
        packages=['websocket'],
        package_data={'websocket': ['data/*.swf', 'data/*.py', 'data/*.js']},
        install_requires=['gevent', 'greenlet'],
        zip_safe=False,
        classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta"])
