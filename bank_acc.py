"""
Bank Account Management Module

Defines the BankAcct class to represent a simple bank account with the following features:
- Stores name, account number, balance, and interest rate
- Supports deposit, withdrawal, and interest rate adjustment
- Provides current balance and interest calculation over a number of days
- Includes a __str__ method to display balance and interest info

Also includes a test function to demonstrate and verify class functionality.
"""
# BankAcct class definition.
class BankAcct:
    # Initialize the required variables.
    def __init__(self, name, account_number, initial_balance, interest_rate):
        self.name = name
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.balance = initial_balance

    # Create a function to deposit funds.
    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount must be positive")
            return
        else:
                self.balance += amount
                print(f"Deposit of ${amount:.2f} received, new balance is ${self.balance:.2f}.")

    # Create a function to withdraw funds.
    def withdraw(self, amount):
        if amount < 0:
            print("Withdrwal amount must be positive.")
        elif amount  > self.balance:
            print("Insufficient funds.")
            return
        else :
            try:
                self.balance -= amount
                print(f"You are withdrawing ${amount:.2f} from your account.")
                print(f"Withdrawal of ${amount:.2f} successful, new balance is ${self.balance:.2f}.")
            except Exception as e:
                print("Error occurred during withdrawal transaction recording:", e)

    # Create a function to adjust interest rates.
    def adjust_interest_rate(self, new_rate):
        if new_rate < 0:
            print("Interest rate cannot be negative.")
        else:
            self.interest_rate = new_rate
            print(f"Interest rate updated to {new_rate * 100:.2f}%.")

    # Create a fubction to display account balance.
    def get_balance(self):
        return self.balance
        print(f"Current account balance: ${self.balance:.2f}")


    # Create a function to calculate interest rate given the number of days.
    def calculate_interest(self, days):
        if days < 0:
            print("Number of days must be positive.")
            return 0

        interest_rate = self.balance * self.interest_rate * (days / 365)
        return interest_rate


    # Creat a function to display balance and interest information.
    def __str__(self):
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Interest Rate: {self.interest_rate * 100:.2f}%"
        )


# Test function to demonstrate class functionality
def test_bank_acct():
    # Create an account and display initial balance
    acct = BankAcct("John Doe", "123456789", 998.75, 0.05)
    print(f"Account created for {acct.name} with initial balance ${acct.balance:.2f} and interest rate of {acct.interest_rate * 100:.2f}%.")

    # Deposit funds
    acct.deposit(500)

    # Withdraw funds
    acct.withdraw(250)

    # Calculate and adjust interest rate
    acct.calculate_interest(90)
    acct.adjust_interest_rate(0.04)



# Call the test_banck_acc function
if __name__ == '__main__':
    test_bank_acct()
