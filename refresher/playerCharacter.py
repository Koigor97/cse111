
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def player_stat(self):
        print(f"Name: {self.name}\nAge: {self.age}")

    @staticmethod
    def capitalize_key_and_array_value(param):
        return {key.capitalize() :  [value] for key, value in param.items()}