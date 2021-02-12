#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Settings module. """

import logging
import os

# Directories
HOME = os.getcwd()                              # home
TEMPLATE_DIR = os.path.join(HOME, 'template/')  # template
REPORT_DIR = os.path.join(HOME, 'report/')      # report

# Report template
REPORT_TEMPLATE = os.path.join(TEMPLATE_DIR, 'dac_analysis_template.xlsx')


def log_config():
    """
    Configure logging format
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M')
