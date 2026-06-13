# Bajillion Search Engine
<p align="center">

<img src="https://img.shields.io/badge/Stanford-Code%20in%20Place-8C1515?style=flat-square">
<img src="https://img.shields.io/badge/CS106A-Final%20Project-2F6BFF?style=flat-square">
<img src="https://img.shields.io/badge/Status-Completed-2EA44F?style=flat-square">

</p>

## Technologies

<p align="center">

<img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white">

</p>


## About the Project

**Bajillion Search Engine** is a Python application developed as a final project for **Stanford Code in Place / CS106A**.

The program creates an inverted index from a collection of BBC News articles and allows users to search for documents using one or more keywords.

It includes both a command-line interface and a web interface that displays the titles of matching articles.

---

## Features

* Search using one or multiple keywords
* Index hundreds of BBC News articles
* Return only documents containing all query terms
* Display article titles in the search results
* Command-line search mode
* Web interface inspired by modern search engines
* Case-insensitive word matching
* Punctuation cleaning
* Local HTTP server
* JSON-based responses

---

## How It Works

The program reads every text file in the selected dataset and creates an **inverted index**.

Each word is stored as a key in a Python dictionary, while the value contains a list of files where that word appears.

For example:

```python
{
    "apple": ["bbcnews/033.txt", "bbcnews/120.txt"],
    "stanford": ["bbcnews/066.txt", "bbcnews/217.txt"]
}
```

When the user searches for multiple words, the program finds the files that contain all of them.

---

## Command-Line Interface

To run the search engine in the terminal:

```bash
python searchengine.py bbcnews -s
```

Example queries:

```text
stanford
stanford bike
cheap apple products
```

Press Enter without typing anything to stop the program.

---

## Web Interface

To start the web version:

```bash
python extension_server.py
```

Keep the terminal open and visit:

```text
http://localhost:8000
```

Example searches:

```text
nice
stanford
cheap apple products
```

To stop the server, press:

```text
Ctrl + C
```

## Project Structure

```text
Assignment6/
├── common_elements.py
├── searchengine.py
├── ethics.txt
├── extension_server.py
├── extension_client.html
├── SimpleServer.py
├── extension.py
├── small/
└── bbcnews/
```

---

## Main Concepts

This project applies:

* Functions
* Lists
* Dictionaries
* String processing
* File reading
* Directory traversal
* Command-line arguments
* JSON
* HTTP requests
* Local web servers
* Search indexing

---

## Example Search

```text
Query: stanford

Results:
1. Yahoo celebrates a decade online
2. Google to scan famous libraries
```

---

## Academic Context

This project was completed as part of:

**Stanford Code in Place / CS106A**

It is based on the Bajillion Search Engine assignment and includes the optional web interface extension.

---
