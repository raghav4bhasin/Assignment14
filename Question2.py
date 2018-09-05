
MaxNum = int(input('Enter the maximum number to check: '))
lst = []
lst = [num for num in range(2, MaxNum) if 0 not in [num %d for d in range(2, num)]]

print(lst)
