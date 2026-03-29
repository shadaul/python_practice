# Python Advanced Data Operations (E-Commerce Focus) 

This repository contains a collection of Python scripts demonstrating advanced, "Pythonic" techniques for handling data structures. These examples are focused on performance, readability, and common e-commerce backend scenarios.

##  Core Concepts Demonstrated

* **Fast Lookups (Sets):** Using Python's `set()` and the intersection operator `&` to instantly find common elements between two lists (e.g., matching wishlist items with cart items) in $O(1)$ average time complexity.
* **Data Zipping:** Utilizing the built-in `zip()` function combined with `dict()` to cleanly merge separate lists of keys (names) and values (prices) into a single key-value mapping without index-based loops.
* **Short-Circuit Evaluation (`all`/`any`):** Implementing highly efficient generator expressions within `all()` to verify conditions (e.g., checking if all items in a cart are in stock) without unnecessary full-list iteration.
* **Clean Enumeration (`enumerate`):** Generating ranked lists and leaderboards using `enumerate(..., start=1)` combined with List Comprehensions and f-strings for clean, index-free data formatting.

##  Usage
Run any of the Python files in this directory to see the output of these optimized data manipulation techniques.