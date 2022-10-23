#!/usr/bin/python3
""" Basic Authentication to GitHub API """
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    response = requests.post('https://api.github.com/user',
                             auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    data = response.json()
    print(data.get('id'))
