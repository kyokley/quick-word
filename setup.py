# -*- coding: utf-8 -*-
import re
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


REQUIRES = [
    'docopt',
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


__version__ = find_version("quick_word/main.py")


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='quick_word',
    version="0.1.0",
    description='Generate a random list of words',
    long_description=read("README.rst"),
    author='Kevin Yokley',
    author_email='kyokley2@gmail.com',
    url='https://github.com/kyokley/quick_word',
    install_requires=REQUIRES,
    license=read("LICENSE"),
    zip_safe=False,
    keywords='quick_word',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
    ],
    py_modules=["quick_word"],
    entry_points={
        'console_scripts': [
            "quick_word = quick_word.main:main"
        ]
    },
    tests_require=['pytest'],
    cmdclass={'test': PyTest}
)
