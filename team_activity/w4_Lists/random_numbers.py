import random


def main():
    numbers = [16.2, 75.1, 52.3]
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 65)
    print(numbers)


def append_random_numbers(number_list, quantity=1):
    for _ in range(quantity):
        if quantity == 1:
            new_num = round(random.uniform(float(len(number_list)), float(quantity)), 1)
            number_list.append(new_num)
        elif quantity > 1:
            for _ in range(3):
                new_num = round(random.uniform(float(len(number_list)), float(quantity)), 1)
                number_list.append(new_num)
        break



if __name__ == '__main__':
    main()

