# error handling
while True:
    try:
        age = int(input('What is your age?: '))
    except ValueError:
        print('Please enter a number')
    else:
        if age >= 18:
            print("You can ride the DareExtreme-RollerCoaster ")
        break
