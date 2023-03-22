
# Aparna Sai Nimmagadda
def encoder(x):
    encoder = ""
    for y in x:
        encoder = encoder + str((int(y)+ 3 % 10)) # takes each digit and moves it 3 places
    return encoder


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option:"))
        if option == 1:
            password = input("Please enter your password to encode:")
            print(encoder(password))
            print("Your password has been encoded and stored!")
        if option == 3:
            exit()
