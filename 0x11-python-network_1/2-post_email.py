#!/usr/bin/python3
""" Send a POST request """
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urlencode(val)
    email = data.encode('ascii')
    req = Request(url, email)
    with urlopen(req) as response:
        file = response.read()
        print(file.decode("utf-8"))
