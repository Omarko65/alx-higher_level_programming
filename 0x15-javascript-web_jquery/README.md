Project: 0x15. JavaScript - Web jQuery | Lagos Intranet          Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);  

Toggle navigation[

](/)

*   [
    
    My Planning
    
    ](/planning/me)
*   [
    
    Projects
    
    ](/projects/current)
*   [
    
    QA Reviews I can make
    
    ](/corrections/to_review)
*   [
    
    Evaluation quizzes
    
    ](/dashboards/my_current_evaluation_quizzes)

* * *

*   [
    
    Curriculums
    
    ](/dashboards/my_curriculums)
*   [
    
    Concepts
    
    ](/concepts)
*   [
    
    Conference rooms
    
    ](/dashboards/video_rooms)
*   [
    
    Servers
    
    ](/servers)
*   [
    
    Sandboxes
    
    ](/user_containers/current)
*   [
    
    Tools
    
    ](/dashboards/my_tools)

* * *

*   [
    
    Peers
    
    ](/users/peers)
*   [
    
    Captain's Logs
    
    ](/dashboards/my_captain_log)

* * *

*   [
    
    Slack
    
    ](https://alx-students.slack.com)
    
    [
    
    My Profile
    
    ](/users/my_profile)
    

[

](/)

*   [
    
    My Planning
    
    ](/planning/me)
*   [
    
    Projects
    
    ](/projects/current)
*   [
    
    QA Reviews I can make
    
    ](/corrections/to_review)
*   [
    
    Evaluation quizzes
    
    ](/dashboards/my_current_evaluation_quizzes)

* * *

*   [
    
    Curriculums
    
    ](/dashboards/my_curriculums)
*   [
    
    Concepts
    
    ](/concepts)
*   [
    
    Conference rooms
    
    ](/dashboards/video_rooms)
*   [
    
    Servers
    
    ](/servers)
*   [
    
    Sandboxes
    
    ](/user_containers/current)
*   [
    
    Tools
    
    ](/dashboards/my_tools)

* * *

*   [
    
    Peers
    
    ](/users/peers)
*   [
    
    Captain's Logs
    
    ](/dashboards/my_captain_log)

* * *

*   [
    
    Slack
    
    ](https://alx-students.slack.com)
    
    [
    
    My Profile
    
    ](/users/my_profile)
    

0x15. JavaScript - Web jQuery
=============================

### Concepts

_For this project, we expect you to look at these concepts:_

*   [JavaScript in the browser](/concepts/3)
*   [Dealing with data statically versus dynamically](/concepts/35)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/4724718.jpg)

Resources
---------

**Read or watch**:

*   [What is JavaScript?](/rltoken/NJ5XM_fzjlBKERHTkdF-uA "What is JavaScript?")
*   [Selector](/rltoken/wsnVUxEcAzzlCx6ES1qc7g "Selector")
*   [Get and set content](/rltoken/rwtc96sn2_LHToBAd0MIhQ "Get and set content")
*   [Manipulate CSS classes](/rltoken/IcM5kKVzssU0ibdUo-2gKQ "Manipulate CSS classes")
*   [Manipulate DOM elements](/rltoken/ve8UKsZLVw2t27PtWscZfQ "Manipulate DOM elements")
*   [API](/rltoken/vKc7XmiHG7HIh3N0Kl_VQw "API")
*   [Introduction](/rltoken/QiUwuS_9TXE49D5IVL-ocg "Introduction")
*   [GET & POST request](/rltoken/Mbe7uoy0iMAfTVs2Tn4Pzg "GET & POST request")
*   [JQuery Ajax Tutorial #1 - Using AJAX & API’s](/rltoken/gMwyXisSLu-kZicmGA0-LQ "JQuery Ajax Tutorial #1 - Using AJAX & API's")
*   [What went wrong? Troubleshooting JavaScript](/rltoken/4eYyJr72PO-cohImk93M3w "What went wrong? Troubleshooting JavaScript")
*   [JQuery](/rltoken/HnjBq6jf84S9S-C15Qi0vw "JQuery")
*   [JQuery API](/rltoken/jvibhq-8VEdQHNUWKTCI7w "JQuery API")
*   [JQuery Ajax](/rltoken/rBZyrXxuRuISDfPBzO9Y7Q "JQuery Ajax")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/uOCIGjC7u4MtYfDwCwODTA "explain to anyone"), **without the help of Google**:

### General

*   Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
*   How to select HTML elements in JavaScript
*   How to select HTML elements with JQuery
*   What are differences between `ID`, `class` and `tag name` selectors
*   How to modify an HTML element style
*   How to get and update an HTML element content
*   How to modify the DOM
*   How to make a `GET` request with JQuery Ajax
*   How to make a `POST` request with JQuery Ajax
*   How to listen/bind to DOM events

\- How to listen/bind to user events
------------------------------------

### Copyright - Plagiarism

*   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
*   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
*   You are not allowed to publish any content of this project.
*   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted on Chrome (version 57.0)
*   All your files should end with a new line
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should be `semistandard` compliant with the flag `--global $`: `semistandard *.js --global $`
*   You must use JQuery version 3.x
*   You are not allowed to use `var`
*   HTML should not reload for each action: DOM manipulation, update values, fetch data…

More Info
---------

### Import JQuery

    <head>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    </head>
    

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/1f1ihd.jpg)

### Manual QA Review

**It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.**

### Quiz questions

**Great!** You've completed the quiz successfully! Keep going!

#### Question #0

In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header class="my_header"> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul id="my_header">
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Question #1

In the following code snippet, does the selector called `('HeAdER')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Tips:

Selectors are case insensitive

#### Question #2

In the following code snippet, does the selector called `('.header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Question #3

In the following code snippet, does the selector called `('.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header class="my_header"> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Question #4

How many HTML tags are present in the following HTML code?

*   `<!DOCTYPE html>` is not an HTML tag
*   `<head></head>` is considered one HTML tag.

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   16
    
*   20
    
*   18
    
*   15
    

#### Question #5

In the following code snippet, does the selector called `('section.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header class="my_header"> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Question #6

How many HTML tags are present in the following HTML code?

*   `<!DOCTYPE html>` is not an HTML tag
*   `<head></head>` is considered one HTML tag.

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   5
    
*   7
    
*   6
    
*   4
    

#### Question #7

In the following code snippet, does the selector called `('body header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Question #8

How many HTML tags are present in the following HTML code?

*   `<!DOCTYPE html>` is not an HTML tag
*   `<head></head>` is considered one HTML tag.

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <ul>
            <li>Home</li>
            <li>Admission</li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   12
    
*   14
    
*   13
    
*   11
    

#### Question #9

In the following code snippet, does the selector called `('header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Question #10

In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header class="my_header"> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Question #11

In the following code snippet, does the selector called `('#header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Question #12

In the following code snippet, does the selector called `('header.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header class="my_header"> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

#### Question #13

In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <link rel="stylesheet" href="styles/global.css" />
      </head>
      <body>
        <header id="my_header"> 
          First HTML page
        </header>
        <section>
          <img src="logo.jpg" alt="" />
          <br />
          <ul>
            <li>Home</li>
            <li>Admission <span class="btn">apply</span></li>
            <li>Login</li>
          </ul>
        </section>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    

*   No
    
*   Yes
    

Tasks
-----

### 0\. No JQuery

mandatory

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

*   You must use `document.querySelector` to select the HTML tag
*   You can’t use the JQuery API

Please test with this HTML file in your browser:

    guillaume@ubuntu:~/0x15$ cat 0-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="0-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: `0-script.js`

Done?! Help

×

#### Students who are done with "0. No JQuery"

### 1\. With JQuery

mandatory

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    guillaume@ubuntu:~/0x15$ cat 1-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="1-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: `1-script.js`

Done?! Help

×

#### Students who are done with "1. With JQuery"

### 2\. Click and turn red

mandatory

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    guillaume@ubuntu:~/0x15$ cat 2-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <div id="red_header">Red header</div>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="2-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: `2-script.js`

Done?! Help

×

#### Students who are done with "2. Click and turn red"

### 3\. Add \`.red\` class

mandatory

Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`

*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    guillaume@ubuntu:~/0x15$ cat 3-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <style>
          .red {
            color: #FF0000;
          }
        </style>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <div id="red_header">Red header</div>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="3-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: `3-script.js`

Done?! Help

×

#### Students who are done with "3. Add \`.red\` class"

### 4\. Toggle classes

mandatory

Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:

*   The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
*   If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    guillaume@ubuntu:~/0x15$ cat 4-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <style>
          .red {
            color: #FF0000;
          }
          .green {
            color: #00FF00;
          }
        </style>
      </head>
      <body>
        <header class="green"> 
          First HTML page
        </header>
        <div id="toggle_header">Toggle header</div>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="4-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: `4-script.js`

Done?! Help

×

#### Students who are done with "4. Toggle classes"

### 5\. List of elements

mandatory

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:

*   The new element must be: `<li>Item</li>`
*   The new element must be added to `UL.my_list`
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    guillaume@ubuntu:~/0x15$ cat 5-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <br />
        <div id="add_item">Add item</div>
        <br />
        <ul class="my_list">
          <li>Item</li>
        </ul>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="5-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: `5-script.js`
