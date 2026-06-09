import random

class sorting_alg:
    numbers = []

    n = input("Kolik čísel chce vygenerovat?")

    n = int(n)

    def gen(n, numbers):
        for i in range(n):
            cislo = random.randint(1, 100)
            numbers.append(cislo)

    def sort(numbers):
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    
    def print_num(numbers):
        for i in numbers:
            print(i)
    
    gen(n, numbers)
    sort(numbers)
    print_num(numbers)