from playerCharacter import PlayerCharacter

player1 = PlayerCharacter(name="Jimmy Fred", age=25)
# player1.player_stat()


# print(dir(player1))
# print(player1.__str__())
# very helpful functions to help with functional programming

def exponent_to_three(item):
    return item**3

def check_if_num_is_odd(item):
    return item % 2 != 0

old_list = [2, 4, 5, 6, 8, 9, 10, 13, 17, 19]

new_list = list(map(exponent_to_three, old_list))
print(f"The List created using map(): {new_list}")

odd_number_list = list(filter(check_if_num_is_odd, old_list))
print(f"The List created using filter(): {odd_number_list}")

zip_list = list(zip(new_list, old_list))
print(f"The List created using zip(): {zip_list}\n")

# Lambda expression
a_lambda_list = list(map(lambda  item: item * 5, odd_number_list))
print(f"The list created using a lambda function: {a_lambda_list}")