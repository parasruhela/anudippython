balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
withdrawn_today = float(input("Enter amount already withdrawn today: "))
atm_cash = float(input("Enter ATM available cash: "))

DAILY_LIMIT = 50000

if withdraw_amount > balance:
    print("Transaction Failed: Insufficient account balance.")

elif withdrawn_today + withdraw_amount > DAILY_LIMIT:
    print("Transaction Failed: Daily withdrawal limit of ₹50,000 exceeded.")

elif withdraw_amount > atm_cash:
    print("Transaction Failed: ATM has insufficient cash.")

else:
    balance -= withdraw_amount
    atm_cash -= withdraw_amount
    print("Transaction Successful!")
    print("Remaining Balance: ₹", balance)