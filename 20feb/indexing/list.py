z =[1,2,4,5]
print(z) 
# * is use for print list without bracket
print(*z) 
# for loop print by next line 
for num in z:
 print(num)
print("length is ", len(z))
# find the lenght of list 
length = len(z)
# for list reverse
for index in range(length-1,-1,-1):
 print(z[index])
   

n = int(input("enter the numbers"))

# for i in range(n):
#     print(" " * (2 * (n - i - 1)) + "* " * (2 * i + 1))


n = 4

for i in range(1, n + 1):
    spaces = "  " * (n - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)

# Top
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))

# Bottom
for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))
