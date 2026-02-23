# Example list of transactions
# Positive = deposit, Negative = withdrawal
transactions = [15000, -5000, 20000, -12000, 8000, -3000, 25000]

print("Transactions:", transactions)

# 1. Calculate total balance
total_balance = sum(transactions)
print("Total Balance:", total_balance)

# 2. Find largest withdrawal
withdrawals = [t for t in transactions if t < 0]

if withdrawals:
    largest_withdrawal = min(withdrawals)  # Most negative value
    print("Largest Withdrawal:", largest_withdrawal)
else:
    print("No withdrawals found.")

# 3. Count number of deposits greater than ₹10,000
large_deposits = [t for t in transactions if t > 10000]
print("Number of Deposits > ₹10,000:", len(large_deposits))