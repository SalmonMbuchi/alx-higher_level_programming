#!/usr/bin/python3
""" Display the value of a header variable"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.getheader("X-Request-Id"))
