# Linux User / Group Matrix

Generate a matrix report containing the Linux user / groups.

## Getting Started:

Clone the project repository: 

```
git clone https://github.com/fredpedroso/linux-users-groups
```

### Requirements:

Install the requirements:

```
pip install -r requirements.txt
```

### How to use:

Analyze from system running:

```
python dac.py --sys_running
```

Analyze from file:

```
python dac.py --passwd <file> --group <file>
```

The report will be generated in the _report_ folder.


# Appendix

## User accounts

User accounts are stored in /etc/passwd

```
username:password:UID:GID:GECOS:homedir:shell
```

- **username**: This is the user's login name. It should not contain capital letters and should be between 1 and 32 characters in length.
- **password**: An x character indicates that the password is stored in /etc/shadow file.
- **UID**: Each user must be assigned a user ID (UID).
- **GID**: The primary group ID (stored in /etc/group file)
- **GECOS**: This field (sometimes called the "comment field") is optional and used only for informational purposes. Usually, it contains the full username.
- **homedir**: The absolute path to the directory the user will be in when they log in. If this directory does not exist, then users directory becomes /
- **shell**: : The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell.


## Groups

Groups are stored in /etc/group

```
group_name:password:GID:user_list
```

- **group_name**: The name of the group.
- **password**: The (encrypted) group password. If this field is empty, no password is needed.
- **GID**: The numeric group ID.
- **user_list**: A list of the usernames that are members of this group, separated by commas.