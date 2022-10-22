# Python Networking 1

In this project I interacted with the following packages:
1. **urllib** 
2. **requests**

## urllib.request

urllib.request is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the *urlopen* function. This is capable of fetching URLs using a variety of different protocols.

It supports fetching URLs for many "schemes" using their associated network prottocols(e.g. FTP, HTTP).

## requests

The requests library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.

## Tasks

**0.What's my status**: [0-hbtn_status.py](./0-hbtn_status.py)

Write a Python script that fetches https://alx-intranet.hbtn.io/status using the urllib package

**1.Response header value**: [1-hbtn_header.py](./1-hbtn_header.py)

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

**2.POST an email**: [2-post_email.py](./2-post_email.py)

Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

**3.Error code**: [3-error_code.py](./3-error_code.py)

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

**4. What's my status?**: [4-hbtn_status.py](./4-hbtn_status.py)

Write a Python script that fetches https://alx-intranet.hbtn.io/status using requests package

**5. Response header value**: [5-hbtn_header.py](./5-hbtn_header.py)

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

**6. POST an email**: [6-post_email.py](./6-post_email.py)

Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

**7. Error code**: [7-error_code.py](./7-error_code.py)

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

**8. Search API**: [8-json_api.py](./8-json_api.py)

Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

**9. My GitHub!**: [10-my_github.py](./10-my_github.py)

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

