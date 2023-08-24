``

# Automated Mailing

![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

## 🛠️ Description

This repository contains a Python script that automates the process of sending emails to a large audience using data
from a CSV file.

## ⚙️ Languages or Frameworks Used

The script utilizes the following modules:

- `os`
- `email.mime`
- `smtplib`
- `pandas`

You can find the full list of dependencies in the `requirements.txt` file. To install these dependencies, execute the
following command in your terminal:

```bash
pip install -r requirements.txt
```

## 🌟 How to Run

- Update the `from_addr` and `pd.read_csv("filepath")`
- Assign your email ID to the `email` variable and your email password to the `password` variable.
- Run the script

## 🤖 Author

[Chathura Abeygunawardhana](https://github.com/chathuraAbeygunawardhana)

## Changes Made for Optimization

- **Encapsulation into a Function**: The email sending logic has been encapsulated into a function named `send_emails()`
  . This design choice makes the code more modular and easier to manage.

- **Variable Naming**: The variable name `name` within the loop has been changed to `names` to avoid confusion with
  the `name` module that was imported.

- **Credentials**: Instead of hard coding email and password directly into the script, placeholders (`'YOUR_EMAIL'`
  and `'YOUR_PASSWORD'`) have been used. Users are advised to replace these placeholders with their actual email
  credentials.

- **Loop Using `zip()`**: The `zip()` function has been utilized to iterate through both the names and email addresses
  in parallel. This approach replaces the previous use of a counter variable for better code clarity.

- **Context Manager for SMTP**: The `with` statement (context manager) has been employed for the SMTP connection. This
  ensures proper connection establishment and closure, even in the event of exceptions.

### Usage

1. Clone the repository to your local machine.
2. Replace `'YOUR_EMAIL'` and `'YOUR_PASSWORD'` placeholders in the script with your actual email credentials.
3. Ensure you have a CSV file named `abc.csv` containing the email addresses and corresponding names.
4. Run the script by executing `python script.py` in your terminal.

### Branch Information

The optimized changes have been made in the branch named `email-contribution-refactor`. This branch showcases the
enhanced version of the email sending script. Users can review the changes made in this branch.

These changes aim to improve the code's quality and make it more user-friendly, providing a solid foundation for email
communication automation while maintaining security standards.

Feel free to contribute or reach out with any suggestions or improvements!

```

