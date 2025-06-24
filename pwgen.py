import random, argparse

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw_list = []
nr_letters = 0
nr_numbers = 0
nr_symbols = 0
password = ""

def genPW(x):
    pw_length = int(x)
    nr_letters = random.randint(1, pw_length-2)
    chars_left = pw_length-nr_letters
    nr_numbers = random.randint(1, chars_left-1)
    chars_left = chars_left-nr_numbers
    nr_symbols = chars_left

    for x in range(0, nr_letters):
        pw_list.append(random.choice(letters))
    for x in range(0, nr_symbols):
        pw_list.append(random.choice(symbols))
    for x in range(0, nr_numbers):
        pw_list.append(random.choice(numbers))

    random.shuffle(pw_list)


# Create the parser
parser = argparse.ArgumentParser(description="A simple argument parser example.")

# Add arguments
parser.add_argument("-l", help="Length of password")
#parser.add_argument("-c", action="store_true", help="hmm".)

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.l:
    if int(args.l) <= 2:
        print("I don't do less than 3 characters, sorry.")
    else:
        genPW(args.l)
else:
    genPW(int(22))




# Putting the password together and printing it
for x in range(0, len(pw_list)):
    password += str(pw_list.pop(0))

if len(password) <= 2:
    print("No password was generated, try again.")
else:    
    print(f"New password is:\n{password}")

