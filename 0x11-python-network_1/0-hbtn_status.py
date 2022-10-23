#!/usr/bin/python3
""" fetch an url using the package urllib"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        file = response.read()
        print("Body response:")
        print(f"\t- type: {type(file)}")
        print(f"\t- content: {file}")
        print(f"\t- utf8 content: {file.decode('utf-8')}")
