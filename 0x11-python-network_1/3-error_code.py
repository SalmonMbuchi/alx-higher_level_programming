#!/usr/bin/python3
""" Handle errors and exceptions """
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            file = response.read()
            print(file.decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
