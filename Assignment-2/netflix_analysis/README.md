# Netflix Titles Data Analysis 📺

## Overview
This project analyzes the Netflix Titles dataset to understand content trends, genres, and production distribution.

## Dataset
Netflix Titles dataset containing Movies and TV Shows available on Netflix.

## Objectives
- Identify top 10 most frequent genres
- Compare Movies vs TV Shows distribution
- Analyze content added per year
- Find country producing the most content
- Handle missing values
- Remove duplicate entries

## Tools Used
- Python
- Pandas
- Matplotlib (optional)

## Data Cleaning
- Removed duplicate titles based on title and type
- Filled missing country values with "Unknown"
- Dropped rows with missing genre or type

## Key Findings
- Drama is the most common genre
- Movies dominate Netflix content
- Content addition increased significantly after 2016
- United States produces the highest number of titles

## How to Run
```bash
pip install pandas
python analysis.py
