multiplication_number = []
for i in range(1, 10):
    for j in range(1, 10):
        print(i, j)
        multiplication_number.append(i * j)

multiplication_number = set(multiplication_number)
print(multiplication_number)

#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42, 45, 48, 49, 54, 56, 63, 64, 72, 81

# 1, 2, 3, 4, 5, 6, 7, 8, 9
# 10, 12, 14, 15, 16, 18
# 20, 21, 24, 25, 27, 28,
# 30, 32, 35, 36
# 40, 42, 45, 48, 49
# 54, 56
# 63, 64
# 72
# 81