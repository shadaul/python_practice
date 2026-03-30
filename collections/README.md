# Data Grouping with defaultdict

This repository demonstrates how to efficiently group and aggregate flat data structures into structured dictionaries using Python's `collections.defaultdict`.

## Core Concept

* **Optimized Data Aggregation:** Instead of using standard dictionaries that require repetitive `if key not in dict` checks before appending data, this script utilizes `defaultdict(list)`. This automatically initializes missing keys with an empty list, allowing for clean, one-line data insertion.
* **E-Commerce Application:** This approach is highly effective for processing transaction logs or event streams. The provided example demonstrates taking a flat list of individual item purchases and grouping them by `user_id` to instantly build a complete order history for each customer.

## Usage

Run the script to see how a flat list of transaction dictionaries is transformed into a mapped dictionary, where each user ID points to an aggregated list of their purchased items.
