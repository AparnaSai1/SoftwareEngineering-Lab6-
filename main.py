
# final file with correct print outputs,etc that matches the sample outputs.
# Aparna Sai Nimmagadda
def encoder(x):
    encoder = ""
    for y in x:
        encoder = encoder + str(((int(y)+ 3) % 10)) # takes each digit and moves it 3 places

        encoder = encoder + str(((int(y) + 3) % 10)) # takes each digit and moves it 3 places
    return encoder

def decode_str(s):
    # taking an 8 digit password
    # take each digit and move it 3 places back
    # "45678888" -> "12345555"
    
    decoded_str = ""
    for c in s:
        new_val = int(c) - 3 
        # if new_val < 0 wrap around
        if new_val < 0:
            new_val = new_val + 10
        
        decoded_str += str(new_val)
        
    return decoded_str

if __name__ == "__main__":
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoder(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            # The encoded password is 45678888, and the original password is 12345555.
            print("The encoded password is", encoder(password), "and the original password is", decode_str(encoder(password)))
        if option == 3:
            exit()

