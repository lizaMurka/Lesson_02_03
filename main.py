def my_pow(number: int, power: int) -> int:
    if power <= 1:
        return number
    else:
        return number * my_pow(number, power - 1)


print(my_pow(2, 3))

# my_pow(2, 3) -> 2 * my_pow(2, 2) => 8
# my_pow(2, 2) -> 2 * my_pow(2, 1) => 4
# my_pow(2, 1) => 2

def print_stars(n):
    if n == 0:
       return
    else:
       print("*", end="")
       print_stars(n - 1)

n = int(input("Enter the number of stars: "))

print_stars(n)

#print_stars(4) -> print_stars(4 - 1) => ****
#print_stars(3) -> print_stars(3 - 1) => ***
#print_stars(2) -> print_stars(2 - 1) => **
#print_stars(1) => *

def sum_numbers(num_1, num_2):
    print(num_1)
    if num_1 > num_2:
        return 0
    else:
        return num_1 + sum_numbers(num_1 + 1, num_2)

num_1 = int(input("Введіть число 1: "))
num_2 = int(input("Введіть число 2: "))
sum = sum_numbers(num_1, num_2)

print(f"Сума чисел від {num_1} до {num_2}: {sum}")

# sum_numbers(1, 5) -> sum_numbers(1 + 1 , 5) => 3
# sum_numbers(2, 5) -> sum_numbers(2 + 1, 5) => 6
# sum_numbers(3, 5) -> sum_numbers(3 + 1, 5) => 10
# sum_numbers(4, 5) -> sum_numbers(4 + 1, 5) => 15


