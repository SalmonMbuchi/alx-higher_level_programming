#!/usr/bin/python3
""" Send JSON data using post request """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1].isalpha():
            payload = {'q': sys.argv[1]}
        else:
            payload = {'q': ""}
    else:
        payload = {'q': ""}
    response = requests.post(
        'http://0.0.0.0:5000/search_user', data=payload)
    try:
        data = response.json()
        if data == {}:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
