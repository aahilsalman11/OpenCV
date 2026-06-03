def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n-1)

n = int(input("For how many numbers do you want to calculate the sum? "))
print(sum_of_numbers(n))