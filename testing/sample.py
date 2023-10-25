import json


def main():
    the_data = trying()
    chance_sis(the_data)


def trying():
    the_dictionary = {
        "web": {
            "email": "koigorfogbawa@gmail.com",
            "password": "4dgysud299dj",
        },

        "instagram": {
            "email": "turaysamuel101@yahoo.com",
            "password": "23467wy723334"
        }
    }
    return the_dictionary

# new_dict = {
#     "xbox": {
#         "username": "samuel turay",
#         "login": "koiMongo101",
#         "password": "eyfddffiu123",
#     },
# }


def chance_sis(file):
    try:
        with open("data.json", "r") as data:
            data_file = json.load(data)
    except FileNotFoundError:
        with open("data.json", "w") as data:
            json.dump(file, data, indent=4)
    else:
        data_file.update(file)
        with open("data.json", "w") as data:
            json.dump(data_file, data, indent=4)



if __name__ == '__main__':
    main()