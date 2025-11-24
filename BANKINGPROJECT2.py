import random



class Account:

    def __init__(self, name, account_number, balance=0.0):
        self.name = name  
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print(" Deposit amount must always be positive.")
            
    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(" INSUFFICIENT BALANCE.")
        else:
            self.balance -= amount
            
            print(f" ₹{amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        
        print(f"Balance: ₹{self.balance:.2f}")


class Bank:
    def __init__(self):
        
        self.accounts = {} 

    def generate_account_number(self):
        # Generates a simple, unique 6-digit account number (for demonstration)
        while True:
            account_number = random.randint(100000, 999999)
            if account_number not in self.accounts:
                return str(account_number)

    def create_account(self, name, initial_deposit=0.0):
        new_account_number = self.generate_account_number()
        
        
        account = Account(name, new_account_number, initial_deposit)
        self.accounts[new_account_number] = account
        
        print(f"\n ACCOUNT CREATED SUCCESSFULLY.")
        print(f"Assigned Account Number: {new_account_number}")
        print(f"Initial Deposit: ₹{initial_deposit:.2f}")

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            print("ACCOUNT NOT FOUND.")
            return None

    def close_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            
            
            if account.balance != 0:
                print(f"⚠️ Account balance is ₹{account.balance:.2f}. Please withdraw the remaining amount before closing.")
                return
            
            del self.accounts[account_number]
            print(f"Account {account_number} for {account.name} closed successfully.")
        else:
            print(" ACCOUNT NOT FOUND.")

    def display_all_accounts(self):
        if not self.accounts:
            print("NO ACCOUNTS CURRENTLY IN THE BANK.")
        else:
            print("\n--- ALL ACCOUNTS ---")
            for account in self.accounts.values():
                account.display()
                print("-" * 25)

# --- Main Application Loop ---

def main():
    bank = Bank()
    
    while True:
        print("\n\n--WELCOME TO THE BANK MANAGEMENT SYSTEM -")
        print("1. CREATE NEW ACCOUNT")
        print("2. DEPOSIT MONEY")
        print("3. WITHDRAW MONEY")
        print("4. CHECK BALANCE")
        print("5. DISPLAY ACCOUNT DETAILS")
        print("6. DISPLAY ALL ACCOUNTS")
        print("7. CLOSE AN ACCOUNT")
        print("8. EXIT")
        print("-" * 45)
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '8':
            print("Thank you for using the Bank Management System. Goodbye!")
            break
        
        try:
            if choice == '1':
                name = input("Enter Account Holder Name: ").strip()
                initial_deposit = float(input("Enter Initial Deposit Amount (min 0.0): "))
                bank.create_account(name, initial_deposit)
            
            elif choice in ('2', '3', '4', '5', '7'):
                acc_num = input("Enter Account Number: ").strip()
                account = bank.get_account(acc_num)
                
                if account:
                    if choice == '2':
                        amount = float(input("Enter deposit amount: "))
                        account.deposit(amount)
                        
                    elif choice == '3':
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                        
                    elif choice == '4':
                        account.check_balance()
                        
                    elif choice == '5':
                        print("\n--- ACCOUNT DETAILS ---")
                        account.display()
                        print("-----------------------")

                    elif choice == '7':
                        bank.close_account(acc_num)
                        
            elif choice == '6':
                bank.display_all_accounts()
                
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
                
        except ValueError:
            print(" Invalid input. Please enter a valid number for amount.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
