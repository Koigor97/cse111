
new_list = []
state = 0

with open("provinces.txt") as file:
    data = file.read()
    the_provinces = data.splitlines()
    the_provinces.pop(0)
    the_provinces.pop()
    print(the_provinces)
    for names in the_provinces:
        the_names = names.replace("AB", "Alberta")
        new_list.append(the_names)
        if "Alberta" == the_names:
            state += 1

print(new_list)
print(f"Alberta occurs {state} times in the modified list")



