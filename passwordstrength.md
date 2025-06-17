# What have I made:
A password strength analyzer. It checks for basic criteria, and for further strengthening, checks against the Have I Been Pwned API. More beginner oriented, but easily scalable.

# What the tool does:
A simple python tool that checks password strength based on:
- length
- use of uppercase, lowercase, numbers, and symbols
- Whether it's been exposed in breaches using the HIBP API

# How to use:
- clone this repo
- run the script using `bash python3 password_checker.py`
- follow the prompts to enter the password

# Why This Matters

This project helps with basic **OS hardening** and **user account security**. It also shows:
- Basic input validation
- Working with Python’s `hashlib`, `requests`, and `re` modules
- Making secure API calls
