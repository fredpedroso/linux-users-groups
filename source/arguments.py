#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Arguments Module. """

import argparse

def parse_args():
    """
    Parse input arguments

    @return: Arguments
    @rtype: list
    """
    parser = argparse.ArgumentParser(description='Linux User / Group - Matrix')
    parser.add_argument('--passwd',
                        dest='passwd',
                        help='passwd file',
                        type=str)
    parser.add_argument('--group',
                        dest='group',
                        help='group file',
                        type=str)
    parser.add_argument('--sys_running',
                        dest='system',
                        action='store_true',
                        help='system running analysis')
    parser.add_argument('--version',
                        dest='version',
                        action='store_true',
                        help='version')
    args = parser.parse_args()
    return args
