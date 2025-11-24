Project Title:Online Banking Management System


Overwiew of the Project:The Online Banking System is a console-based or simple web-based application focused on implementing the core ledger transactions of a bank. This project provides a basic but functional model for managing customer accounts, including essential operations like creating accounts, handling cash deposits and withdrawals, and checking account status


Features:
This project implements the following fundamental banking operations:

ACCOUNT LIFESTYLE & MANAGEMENT
Create New Account: Allows users to open a new account with an initial deposit.
Display All Accounts: Lists details (Account Number, Name, Balance) for all active accounts.
Close Account: Permanently deactivates and removes a specified account.

TRANSACTION MANAGEMENT
Deposit Funds: Add money to a specified account.
Withdraw Funds: Subtract money from a specified account, with validation for sufficient balance.
Check Balance: Quickly view the current balance of a specific account.

Technologies/Tools used:
python:The primary programming language likely using classes and functions for structure.
github:For source code management.
IDE:Integrated Development Environment for coding.
command line interface(CONSOLE/CLI):The primary user interface for interaction.
CSV file handling:Used for persistent storage of account and transaction data.

Steps to Install and Run the project

Follow these steps to set up and run the Online Banking System on your local machine.
Prerequisites
Python 3.8+ installed.
pip (Python package installer).
Git installed.

1.  Clone the Repository
Open your terminal or command prompt and run.

2.  Create and Activate Virtual Environment
It is best practice to use a virtual environment.

3. Install Dependencies
Install all required Python packages (if any are outside the standard library).
4.Run the Application
Execute the main Python script to start the banking system's console interface:
nstructions for Testing

The system should present a main menu upon running. Test each numbered menu option thoroughly.

INSTRUCTIONS FOR TESTING

Test Scenarios
1)Create Account (Setup)
Select the "Create New Account" option.
Enter required details (Name, Initial Deposit). Ensure the initial deposit meets any minimum requirement (e.g., $100).
Note the Account Number assigned by the system.

2)Display All Accounts
Select the "Display All Accounts" option.
Verify the newly created account appears in the list with the correct initial balance.

3)Deposit and Balance Check
Select deposit amount. Enter the Account Number created in step 1.
Deposit a significant amount.
Select "Check Balance" for that account number to confirm the balance is Initial Balance + $500.

4)Withdrawal (Success and Failure)
Success: Select "Withdraw Funds". Withdraw a small amount (e.g., $50).
Select "Check Balance" to ensure the balance is updated correctly.
Failure: Attempt to withdraw an amount greater than the current balance (e.g., the current balance + $1). The system should display an "Insufficient Funds" error and the balance should remain unchanged.

5)Closing Account
Select "Close Account". Enter the Account Number. Confirm the closure when prompted.
Select "Display All Accounts" again to ensure the account is no longer listed.
Attempt to check the balance or deposit funds into the closed account to confirm the system handles it with an "Account Not Found" error.



