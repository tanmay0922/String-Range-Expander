Number Range Expander

A Python utility that parses and expands number ranges from strings, with support for advanced features such as reversed ranges, step values, duplicate handling, and flexible output formats.

This project is implemented in 7 stages, each adding new functionality

Features

Stage 1 – Parse and expand simple numeric ranges ("1-5" → [1, 2, 3, 4, 5])

Stage 2 – Support multiple ranges separated by commas ("1-3,5-7")

Stage 3 – Handle whitespace gracefully ("1-3 , 5-7")

Stage 4 – Handle reversed and invalid ranges gracefully:

"5-3" → [5, 4, 3]

"3-3" → [3]

"3-a" → raises error

Stage 5 – Support step values:

"1-10:2" → [1, 3, 5, 7, 9]

"10-1:3" → [10, 7, 4, 1]

Stage 6 – Handle overlapping and duplicate ranges by merging and deduplicating results

Stage 7 – Flexible output format:

Python list: [1, 2, 3]

CSV string: "1,2,3"

Python set: {1, 2, 3}

Project Structure

number-range-expander/

│
├── range_expander.py 

├── test_stage1.py   


├── test_stage2.py

├── test_stage3.py

├── test_stage4.py

├── test_stage5.py

├── test_stage6.py

├── test_stage7.py

└── README.md

Command to test test cases:

run all tests (if using pytest):

pytest

Author:
TANMAY UPADHYAY
