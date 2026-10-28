# SE Lab 5 — Static Code Analysis

**Student Name:** DHANUSH K S  
**SRN:** PES1UG24CS148  
**Repository:** https://github.com/SETAPESU26/L5_21_wildlife_sightings

## Issue Documentation

| No. | Issue | Tool | Severity / Type | Fix Applied |
|---|---|---|---|---|
| 1 | SQL query construction could allow SQL injection | Bandit | Medium — Security | Replaced string formatting with parameterized SQL queries. |
| 2 | Weak MD5 hashing algorithm | Bandit | High — Security | Replaced MD5 with SHA-256. |
| 3 | Assert statement used for program validation | Bandit | Low — Reliability | Removed the assert statement. |
| 4 | Mutable default dictionary argument | Pylint | Warning — Correctness | Changed the default to `None` and initialized the dictionary inside the function. |
| 5 | Function names did not follow snake_case | Pylint | Convention | Renamed functions using snake_case. |
| 6 | Missing module and function docstrings | Pylint | Convention | Added descriptive docstrings. |
| 7 | Long lines and formatting violations | Flake8 | Style | Reformatted the code and wrapped long lines. |
| 8 | Ambiguous variable names and naming conflicts | Pylint / Flake8 | Readability | Used clearer names and improved code structure. |

## Verification Results

- Original Pylint score: 3.46/10
- Final Pylint score: 10.00/10
- Final Bandit report: No issues identified.
- Final Flake8 report: Empty; no violations reported.
- Program execution: Successful.
