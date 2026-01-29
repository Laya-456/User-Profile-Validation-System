# User Profile Validation System

## Introduction
This project is a **User Profile Validation System** developed using Python. The main objective of this assignment is to validate user-entered profile details before storing them in a university web portal.

The program verifies whether the given user information satisfies all predefined rules and then classifies the profile as **VALID** or **INVALID**.

---
## Purpose of the Project
In real-world applications, validating user input is essential to ensure data accuracy and reliability. This project simulates a basic validation system that checks the correctness of user details such as name, email, mobile number, and age.
The assignment emphasizes logical thinking and the use of fundamental Python concepts without relying on advanced features.

---
## Inputs Used
The program accepts the following inputs from the user:
1. Full Name (string)
2. Email ID (string)
3. Mobile Number (string)
4. Age (integer)

---
## How the Code Works
1. A variable named `valid` is initialized with value `1`, assuming the user profile is valid.
2. Each input is validated using conditional statements (`if` conditions).
3. If any validation rule fails, the value of `valid` is set to `0`.
4. After checking all conditions:
   - If `valid` remains `1`, the program prints **User Profile is VALID**.
   - Otherwise, it prints **User Profile is INVALID**.

This approach ensures that all validations are completed before displaying the final result.

---
## Validation Rules
### Full Name Validation
- Must contain at least two words.
- Must not start or end with a space.
### Email ID Validation
- Must contain exactly one `@` symbol.
- Must contain at least one `.` (dot).
- Must not start with `@`.
### Mobile Number Validation
- Must be exactly 10 digits.
- Must contain only numeric characters.
- Must not start with `0`.
### Age Validation
- Age must be between **18 and 60** (inclusive).

---
## Constraints Followed
- No loops are used.
- No regular expressions are used.
- No advanced libraries are used.
- Only basic Python data types, strings, and conditional statements are used.
- Allowed built-in functions:
  - `len()`
  - `count()`
  - `isdigit()`

---
## Sample Test Cases
### Test Case 1 (Valid Profile)
**Input:**
```
Full Name: Yasir Afaq
Email: yasir@gmail.com
Mobile: 9622949937
Age: 29
```

**Output:**
```
User Profile is VALID
```

---
### Test Case 2 (Invalid Profile)
**Input:**
```
Full Name: Yasir
Email: yasirgmail.com
Mobile: 0876543210
Age: 17
```

**Output:**
```
User Profile is INVALID
```

---
## How to Run the Program
1. Clone or download this repository.
2. Open the Python file in any Python-supported environment.
3. Run the program using the command:
```
python user_profile_validation.py
```
4. Enter the required inputs when prompted.

---
## Updates and Maintenance
This README.md file will be updated regularly to reflect:
- Changes in validation logic
- Code improvements or modifications
- Additional features or enhancements

This ensures the documentation remains accurate and aligned with the current version of the project.

---
## Conclusion
This project demonstrates how fundamental Python concepts can be applied to solve a real-world problem involving user input validation while strictly following given constraints.
