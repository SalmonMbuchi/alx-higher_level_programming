#!/usr/bin/python3
""" Fetch an URL using requests module """
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(response.text)
