#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''quick_word

Usage:
  quick_word <word_count>
  quick_word -h | --help
  quick_word --version

Options:
  -h --help     Show this screen.
  --version     Show version.
'''

from __future__ import unicode_literals, print_function
import sys
from docopt import docopt
from .words import get_word

__version__ = "0.1.0"
__author__ = "Kevin Yokley"
__license__ = "MIT"


def main():
    '''Main entry point for the quick_word CLI.'''
    args = docopt(__doc__, version=__version__)

    try:
        word_count = int(args['<word_count>'])
    except ValueError:
        print(f"Expected an int. Got '{args['<word_count>']}'")
        sys.exit(1)
    print('\n'.join(get_word() for i in range(word_count)))


if __name__ == '__main__':
    main()
