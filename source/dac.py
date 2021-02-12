#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Main Module. """

import os
import logging
from source.settings import log_config
from source.arguments import parse_args
from source.report import generate_report
from source.dac_analysis import (
    read_system_passwd,
    read_system_group,
    read_passwd_file,
    read_group_file
)
from source import __version__


def main():
    """
    Main
    """
    log_config()
    args = parse_args()

    # tool version
    if args.version:
        logging.info('Tool version %s', __version__)
        return

    # system running argument
    if args.system is True:
        passwd_data = read_system_passwd()
        group_data = read_system_group()
        generate_report(passwd_data, group_data)
        return
    
    # analyze from file argument
    elif (args.passwd is not None) and (args.group is not None):
        
        if not os.path.isfile(args.passwd):
            logging.error('Not found the passwd file %s', args.passwd)
            return
        if not os.path.isfile(args.group):
            logging.error('Not found the group file %s', args.group)
            return

        passwd_data = read_passwd_file(args.passwd)
        group_data = read_group_file(args.group)
        generate_report(passwd_data, group_data)
