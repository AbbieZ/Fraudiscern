# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:
@file: user_register.py
@time: 7/15/2021
@version:
"""
import csv
import hashlib
import os
import random

import pandas as pd


def get_authentication_code(code_length):
    """Generate a authentication code with appointed length.

    Args:
        code_length (int): The length of the authentication code.

    Returns:
        str: authentication code.
    """
    code_source = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for _ in range(code_length):
        salt += random.choice(code_source)
    return salt


def get_hash_sha1(message):
    """Get the sha1 hash value of message.

    Args:
        message (str): message content.

    Returns:
        str: sha1 hash value.
    """
    sha1 = hashlib.sha1()
    sha1.update(message.encode('utf-8'))
    return str(sha1.hexdigest())


def add_user(user_dict):
    """Add a user into the user register file.

    Args:
        user_dict (dict): A dictionary including user_name, mail and password.

    Returns:
        bool: True -- add the user successfully, False -- add the user unsuccessfully.
    """
    path = "users.csv"
    if not os.path.exists("users.csv"):
        with open(path, 'wb') as f:
            csv_write = csv.writer(f)
            csv_head = ["username", "mail", "password"]
            csv_write.writerow(csv_head)
        with open(path, 'a+') as f:
            csv_write = csv.writer(f)
            data_row = [get_hash_sha1(str(user_dict["user_name"])), get_hash_sha1(str(user_dict["mail"])),
                        get_hash_sha1(str(user_dict["password2"]))]
            csv_write.writerow(data_row)
    else:
        if _check_user(str(user_dict["user_name"])):
            with open(path, 'a+') as f:
                csv_write = csv.writer(f)
                data_row = [get_hash_sha1(str(user_dict["user_name"])), get_hash_sha1(str(user_dict["mail"])),
                            get_hash_sha1(str(user_dict["password2"]))]
                csv_write.writerow(data_row)
                return True
        else:
            return False


def _check_user(user_name):
    """Check whether one user exists in the register file.

    Args:
        user_name (str): The input user name, in the register file user name is unique.

    Returns:
        bool: True -- the user exists in the register file. False -- the user not exists in the register file.
    """
    df = pd.read_csv("users.csv")
    for row in df.iterrows():
        if int(bin(user_name)) ^ int(bin(row[0])):
            continue
        else:
            return False
    return True