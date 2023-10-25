
the_dict = {
    "alice": "Python",
    "james": "C",
    "johnny": "Java",
    "jerry": "javascript",
    "samuel": "Flutter",
    "kotleg": "Python",
    "brother_p": "Java",
}

is_point_value = the_dict.get("johnny", "This key-value pair doesn't exit")
print(f"{is_point_value}\n")

for names in set(sorted(the_dict.values())):
    print(f"{names}\n")

friends = {"Joe", "Jerry", "Bryan", "Joe", "Fawaz", "Bryan", "Joe"}
friends.add("Hassan")
print(friends)
