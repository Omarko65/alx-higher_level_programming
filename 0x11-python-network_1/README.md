0x11. Python - Network #1
=========================

#### In a nutshell…

*   **Auto QA review:** 0.0/75 mandatory & 0.0/8 optional
*   **Altogether:**  **0.0%**
    *   Mandatory: 0.0%
    *   Optional: 0.0%
    *   Calculation:  0.0% + (0.0% \* 0.0%)  == **0.0%**

Resources
---------

**Read or watch**:

*   [HOWTO Fetch Internet Resources Using urllib Package](/rltoken/KoRrs5dVWsb-B82e-M1TQQ "HOWTO Fetch Internet Resources Using urllib Package")
*   [Quickstart with Requests package](/rltoken/OGcRGPr7TSWtzypDd0ZibQ "Quickstart with Requests package")
*   [Requests package](/rltoken/dUNaNQrV2bMSstILitQbXQ "Requests package")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/kn48lNAWMEoi1DysNqM6bg "explain to anyone"), **without the help of Google**:

### General

*   How to fetch internet resources with the Python package `urllib`
*   How to decode `urllib` body response
*   How to use the Python package `requests` #requestsiswaysimplerthanurllib
*   How to make HTTP `GET` request
*   How to make HTTP `POST`/`PUT`/etc. request
*   How to fetch JSON resources
*   How to manipulate data from an external service

### Copyright - Plagiarism

*   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
*   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
*   You are not allowed to publish any content of this project.

\- Any form of plagiarism is strictly forbidden and will result in removal from the program.
--------------------------------------------------------------------------------------------

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file at the root of the repo, containing a description of the repository
*   A `README.md` file, at the root of the folder of _this_ project, is mandatory
*   Your code should use the pycodestyle (version `2.8.*`)
*   All your files must be executable
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   You must use [get](/rltoken/ddDVKG3F084DP9byugbABw "get") to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   Your code should not be executed when imported (by using `if __name__ == "__main__":`)

Tasks
-----

### 0\. What's my status? #0

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

*   You must use the package `urllib`
*   You are not allowed to import any packages other than `urllib`
*   The body of the response must be displayed like the following example (tabulation before `-`)
*   You must use a `with` statement

    guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
    Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `0-hbtn_status.py`

Done?! Help

×

#### Students who are done with "0. What's my status? #0"

Check your code

×

#### Correction of "0. What's my status? #0"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 0\. What's my status? #0

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 1\. Response header value #0

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

*   You must use the packages `urllib` and `sys`
*   You are not allow to import packages other than `urllib` and `sys`
*   The value of this variable is different for each request
*   You don’t need to check arguments passed to the script (number or type)
*   You must use a `with` statement

    guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
    ade2627e-41dd-4c34-b9d9-a0fa0f47b237
    guillaume@ubuntu:~/0x11$ 
    guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
    6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `1-hbtn_header.py`

Done?! Help

×

#### Students who are done with "1. Response header value #0"

Check your code

×

#### Correction of "1. Response header value #0"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 1\. Response header value #0

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 2\. POST an email #0

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

*   The email must be sent in the `email` variable
*   You must use the packages `urllib` and `sys`
*   You are not allowed to import packages other than `urllib` and `sys`
*   You don’t need to check arguments passed to the script (number or type)
*   You must use the `with` statement

Please test your script in the sandbox provided, using the web server running on port 5000

    guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
    Your email is: hr@holbertonschool.com
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `2-post_email.py`

Done?! Help

×

#### Students who are done with "2. POST an email #0"

Check your code

×

#### Correction of "2. POST an email #0"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 2\. POST an email #0

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 3\. Error code #0

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

*   You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
*   You must use the packages `urllib` and `sys`
*   You are not allowed to import other packages than `urllib` and `sys`
*   You don’t need to check arguments passed to the script (number or type)
*   You must use the `with` statement

Please test your script in the sandbox provided, using the web server running on port 5000

    guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
    Index
    guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
    Error code: 401
    guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
    Error code: 404
    guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
    Error code: 500
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `3-error_code.py`

Done?! Help

×

#### Students who are done with "3. Error code #0"

Check your code

×

#### Correction of "3. Error code #0"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 3\. Error code #0

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 4\. What's my status? #1

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

*   You must use the package `requests`
*   You are not allow to import packages other than `requests`
*   The body of the response must be display like the following example (tabulation before `-`)

    guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
    Body response:$
        - type: <class 'str'>$
        - content: OK$
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `4-hbtn_status.py`

Done?! Help

×

#### Students who are done with "4. What's my status? #1"

Check your code

×

#### Correction of "4. What's my status? #1"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 4\. What's my status? #1

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 5\. Response header value #1

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

*   You must use the packages `requests` and `sys`
*   You are not allow to import other packages than `requests` and `sys`
*   The value of this variable is different for each request
*   You don’t need to check script arguments (number and type)

    guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
    5e52e160-c822-4669-8b3a-8b3bbca7b090
    guillaume@ubuntu:~/0x11$ 
    guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
    eaceaf35-bc0f-4f74-994a-7be0728ec654
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `5-hbtn_header.py`

Done?! Help

×

#### Students who are done with "5. Response header value #1"

Check your code

×

#### Correction of "5. Response header value #1"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 5\. Response header value #1

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 6\. POST an email #1

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

*   The email must be sent in the variable `email`
*   You must use the packages `requests` and `sys`
*   You are not allowed to import packages other than `requests` and `sys`
*   You don’t need to error check arguments passed to the script (number or type)

Please test your script in the sandbox provided, using the web server running on port 5000

    guillaume@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
    Your email is: hr@holbertonschool.com
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `6-post_email.py`

Done?! Help

×

#### Students who are done with "6. POST an email #1"

Check your code

×

#### Correction of "6. POST an email #1"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 6\. POST an email #1

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 7\. Error code #1

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

*   If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
*   You must use the packages `requests` and `sys`
*   You are not allowed to import packages other than `requests` and `sys`
*   You don’t need to check arguments passed to the script (number or type)

Please test your script in the sandbox provided, using the web server running on port 5000

    guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
    Index
    guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
    Error code: 401
    guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
    Error code: 404
    guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
    Error code: 500
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `7-error_code.py`

Done?! Help

×

#### Students who are done with "7. Error code #1"

Check your code

×

#### Correction of "7. Error code #1"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 7\. Error code #1

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 8\. Search API

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

*   The letter must be sent in the variable `q`
*   If no argument is given, set `q=""`
*   If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
*   Otherwise:
    *   Display `Not a valid JSON` if the JSON is invalid
    *   Display `No result` if the JSON is empty
*   You must use the package `requests` and `sys`
*   You are not allowed to import packages other than `requests` and `sys`

Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random.

    guillaume@ubuntu:~/0x11$ ./8-json_api.py 
    No result
    guillaume@ubuntu:~/0x11$ ./8-json_api.py a
    [8446] amnirqhtfjq
    guillaume@ubuntu:~/0x11$ ./8-json_api.py 2
    No result
    guillaume@ubuntu:~/0x11$ ./8-json_api.py b
    [7094] bmofakakhke
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `8-json_api.py`

Done?! Help

×

#### Students who are done with "8. Search API"

Check your code

×

#### Correction of "8. Search API"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 8\. Search API

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 9\. My GitHub!

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](/rltoken/LjPfW9hW_55YwijGVofyTQ "GitHub API") to display your `id`

*   You must use [Basic Authentication](/rltoken/VsPQfbYBgBA0PPdpdJNPIQ "Basic Authentication") with a [personal access token as password](/rltoken/cQ7P5gl79x0I_3Pl3hG2hw "personal access token as password") to access to your information (only `read:user` permission is needed)
*   The first argument will be your `username`
*   The second argument will be your `password` (in your case, a [personal access token as password](/rltoken/cQ7P5gl79x0I_3Pl3hG2hw "personal access token as password"))
*   You must use the package `requests` and `sys`
*   You are not allowed to import packages other than `requests` and `sys`
*   You don’t need to check arguments passed to the script (number or type)

    guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
    2531536
    guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
    None
    guillaume@ubuntu:~/0x11$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x11-python-network_1`
*   File: `10-my_github.py`

Done?! Help

×

#### Students who are done with "9. My GitHub!"

Check your code

×

#### Correction of "9. My GitHub!"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress... : an error occurred Get a sandbox QA Review

×

#### 9\. My GitHub!

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Recommended Sandboxes

Copyright © 2022 ALX, All rights reserved.

×

#### Markdown Guide

#### Emphasis

\*\***bold**\*\*
\*_italics_\*
~strikethrough~~

#### Headers

\# Big header
## Medium header
### Small header
#### Tiny header

#### Lists

\* Generic list item
\* Generic list item
\* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item

#### Links

\[Text to display\](http://www.example.com)

#### Quotes

\> This is a quote.
> It can span multiple lines!

#### Images

CSS style available: `width, height, opacity`

!\[\](http://www.example.com/image.jpg)
!\[\](http://www.example.com/image.jpg | width: 200px)
!\[\](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)

#### Tables

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

_Or without aligning the columns..._

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |

#### Displaying code

\`var example = "hello!";\`

_Or spanning multiple lines..._

\`\`\`
var example = "hello!";
alert(example);
\`\`\`
