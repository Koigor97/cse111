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
print(f"The list created using a lambda function: {a_lambda_list}\n")

# list comprehensions
friend_names = ['Jerry', "Barry", "Gibril", "Alhajie", "Joe Krack", "Bryan", "Keanu", "Nakegdi"]
friends_with_five_letter_names = [names for names in friend_names if len(names) <= 5]
print(f"List with friend names with 5 or less than 5 letter.\n"
      f"Using list-comprehension: {friends_with_five_letter_names}")

# dictionary-comprehension
the_dict = {
    "gibril": "eat-alot, set confusion, study",
    "barry": "short-tempered, like young girls, prayerful",
    "keanu": "very-nice, God-fearing, honest, caring"
}

new_dict = PlayerCharacter.capitalize_key_and_array_value(the_dict)
print(f"Dictionary-comprehension using class method. The result: {new_dict}")
