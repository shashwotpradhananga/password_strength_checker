# 🔐 Password Strength Checker

## 📌 About the Project

This is a beginner-level Python project that checks the strength of a password based on its length.

This is **Version 1** of the project.

As I continue learning Python and cybersecurity, I will keep improving this project by adding more password-security checks and making the analyzer more advanced.

---

## 🧠 How It Works

The current version uses a simple rule:

- If the password has **12 or more characters** → it is considered **Strong**
- If the password has **less than 12 characters** → it is considered **Weak**

The program first asks the user to enter a password.

It then:

1. Takes the password as input.
2. Calculates its length using Python's `len()` function.
3. Stores the length in a variable.
4. Uses an `if/else` statement to check the length.
5. Displays the result to the user.

---

## 💻 Version 1

### Current Features

- Takes a password from the user
- Calculates password length
- Checks whether the password contains at least 12 characters
- Displays whether the password is weak or strong
- Gives the user a suggestion if the password is weak


## 🚀 Future Versions

This project will continue to evolve as I learn more about **Python, cybersecurity, and password security**.

The goal is to gradually transform this simple password length checker into a more complete password strength analyzer.

### 🔹 Version 2 — Character Analysis

The next version will check more than just password length.

Planned checks:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Minimum password length

This will make the analysis more meaningful than simply checking the number of characters.

---

### 🔹 Version 3 — Strength Scoring

The program will be upgraded from a simple **Strong/Weak** result to a scoring system.

Possible strength levels:
```text
Very Weak
Weak
Moderate
Strong
Very Strong


