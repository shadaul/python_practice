# Data Cleaning & String Manipulation

This folder contains exercises focused on cleaning and processing text data, a common task in Data Engineering. 

## Files
- `promo_data.py`: A script that simulates handling raw promotional data and inventory SKUs.

## What it does
1. **Data Cleaning**: Takes a list of user-input promo codes with inconsistent casing and trailing spaces, and standardizes them using `.strip()` and `.upper()`.
2. **Parsing Strings**: Simulates extracting product categories from a list of SKUs by splitting strings at a delimiter using the `.split()` method.
3. **Message Generation**: Iterates through a list of customer dictionaries and uses formatted string literals (f-strings) to generate personalized marketing messages.

## Goal
To practice string manipulation methods and handling lists of dictionaries in Python.