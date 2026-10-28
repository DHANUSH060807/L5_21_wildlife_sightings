# SE Lab 5 — Reflection

**Student Name:** DHANUSH K S  
**SRN:** PES1UG24CS148

### 1. What is static code analysis?

Static code analysis examines source code without executing it to identify potential bugs, security weaknesses, and style violations. It helps improve software quality and maintainability.

### 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint identifies code-quality problems, naming issues, and potential programming mistakes. Bandit checks for common security vulnerabilities. Flake8 checks Python formatting and compliance with coding conventions.

### 3. What issues did you identify and fix?

I identified SQL query construction that could lead to SQL injection, the use of MD5 hashing, an assert statement, a mutable default argument, missing docstrings, inconsistent function naming, and formatting violations. I fixed these issues by using parameterized SQL, replacing MD5 with SHA-256, removing the assert statement, initializing mutable data safely, adding documentation, and formatting the code.

### 4. How did static analysis improve your program?

Static analysis helped improve the security, readability, consistency, and maintainability of my program. The Pylint score increased from 3.46/10 to 10.00/10, and the final Bandit and Flake8 checks reported no issues.

### 5. What are the limitations of static analysis?

Static analysis tools cannot guarantee that a program is completely correct or secure. Some warnings require human judgment, and runtime testing is still necessary to confirm that the program behaves as expected.
