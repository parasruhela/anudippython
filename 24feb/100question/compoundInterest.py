P = float(input())
R = float(input())
T = float(input())

A = P * (1 + R/100) ** T
CI = A - P

print(CI)
