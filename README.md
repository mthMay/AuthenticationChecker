# AuthenticationChecker
### Description
The Authentication Checker is a Python-based program designed to authenticate user credentials before granting access to the system. It allows users to sign up for an account with unique usernames and secure passwords, log in with their existing credentials, and even delete their accounts if they wish. The program ensures password security by enforcing strict rules and stores basic user information, such as name, age, address, and email.

### Features
• **User Registration**: Allows users to create a new account with unique usernames. Collects user details such as name, age, address, mobile number, nationality and email address.<br>
• **Password Validation**: Enforces a strong password policy requiring more than 11 characters, at least 3 numbers, 2 special symbols, and 1 uppercase letter.<br>
• **Login System**: Authenticates users by checking their username and password against the stored data before granting access to the system.<br>
• **Unique Usernames**: Ensures that each username is unique and cannot be reused.<br>
• **Account Deletion**: Allows users to delete their account upon confirmation of their credentials.<br>
• **User Data Storage**: Stores user information in a text file (userDetails.txt), allowing easy access for login and deletion features.<br>

### How to Run
1. Clone the repository:
   ```https://github.com/mthMay/AuthenticationChecker.git```
2. Navigate to the project directory:
   ```cd AuthenticationChecker```
3. Run the application:
   ```python3 main.py```

**NOTE: Ensure Python 3 is installed on your system before running the application.**

### How to Use
1. **Sign Up**:<br>
• When prompted, type S to sign up for a new account.<br>
• Input your desired username, ensuring it hasn’t been taken by another user.<br>
• Create a secure password following the program’s rules.<br>
• Enter additional personal details, including your name, age, address, and email.<br>
• The program will save your information in a text file for future use.
2. **Login**:<br>
• Select the L option to log in with an existing account.<br>
• Enter your username and password when prompted.<br>
• The program will check your credentials and grant access if the details match.
3. **Account Deletion**:<br>
• Once logged in, the program will ask if you wish to delete your account.<br>
• Confirm your decision by re-entering your username, and your account will be removed from the system.
