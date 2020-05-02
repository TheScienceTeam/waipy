#!/usr/bin/env python3

import json
import urllib.request
from pathlib import Path
from os import getlogin
from platform import system

def read_file(filename):
    with open(filename, encoding = 'utf-8', mode = 'r') as file:
        return file.read()

def read_json(filename):
    return json.loads(read_file(filename))

def make_onedrive_directory(foldername):
    if system() == 'Windows':
        root = Path("C:/Users/").joinpath(getlogin()).joinpath("OneDrive")
        directory = root.joinpath(foldername)
        directory.mkdir(parents = True, exist_ok = True)
        return directory
    else:
        raise NotImplementedError()

def download(url, filename):
    urllib.request.urlretrieve(url, filename)