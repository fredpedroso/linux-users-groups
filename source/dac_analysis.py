#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" DAC analysis module. """

import pwd
import grp
import operator


def read_passwd_file(passwd_file):
    """
    Read /etc/passwd file from a given path

    @param passwd_file: linux passwd file path
    @type  passwd_file: str
    """
    passwd_file_raw = open(passwd_file, 'r')

    users_list = []
    for line in passwd_file_raw:

        if not line.split(' ', 1)[0] == '#':
            line = line.strip()
            fields = line.split(":")

            if not fields[0] == '#':
                users_list.append(fields)

    passwd_file_raw.close()

    return users_list


def read_group_file(group_file):
    """
    Read /etc/group file from a given path

    @param group_file: linux group file path
    @type  group_file: str
    """
    group_file_raw = open(group_file, 'r')

    group_list = []
    for line in group_file_raw:

        if not line.split(' ', 1)[0] == '#':
            line = line.strip()
            fields = line.split(":")

            if not fields[0] == '#':
                group_list.append(fields)

    group_file_raw.close()

    return group_list


def read_system_passwd():
    """
    Read /etc/passwd file from current system running
    """
    passwd_list = []
    os_users_data = pwd.getpwall()
    os_users = sorted((user
                       for user in os_users_data
                       if not user.pw_name.startswith('_')),
                      key=operator.attrgetter('pw_name'))

    passwd_info = ''
    for os_user in os_users:
        name = os_user.pw_name
        passwd = os_user.pw_passwd
        uid = os_user.pw_uid
        gid = os_user.pw_gid
        gecos = os_user.pw_gecos
        dir = os_user.pw_dir
        shell = os_user.pw_shell

        passwd_info = (name,
                       passwd,
                       uid,
                       gid,
                       gecos,
                       dir,
                       shell)

        passwd_list.append(passwd_info)

    return passwd_list


def read_system_group():
    """
    Read /etc/group file from current system running
    """
    group_list = []
    os_groups_data = grp.getgrall()
    os_groups = sorted((groups
                        for groups in os_groups_data
                        if not groups.gr_name.startswith('_')),
                       key=operator.attrgetter('gr_name'))

    group_info = ''
    for os_group in os_groups:
        name = os_group.gr_name
        passwd = os_group.gr_passwd
        gid = os_group.gr_gid
        mem = os_group.gr_mem

        group_info = (name,
                      passwd,
                      gid,
                      mem)

        group_list.append(group_info)

    return group_list
