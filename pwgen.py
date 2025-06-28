import random, argparse

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw_list = []
password = ""
a = False
b = False
c = False

def genPW(x, a, b, c):
    pw_length = int(x)

    if a == True:     
        for x in range(0, pw_length):
            pw_list.append(random.choice(letters))
    if b == True:
        for x in range(0, pw_length):
            pw_list.append(random.choice(numbers))
    if c == True:  
        for x in range(0, pw_length):
            pw_list.append(random.choice(symbols))
    return pw_length


# Create the parser
parser = argparse.ArgumentParser(description="A simple argument parser example.")

# Add arguments
parser.add_argument("-l", help="Length of password.")
parser.add_argument("-o", help="options: 1=letter, 2=numbers, 3=symbols. -o 123 for all, -o 12 for letters and numbers.")
parser.add_argument("-c", action="store_true", help="Make letters only lower case.")
parser.add_argument("-C", action="store_true", help="Make letters only upper case.")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.o:
    if "1" in args.o:
        a = True
    if "2" in args.o:
        b = True
    if "3" in args.o:
        c = True
else:
    a = True
    b = True
    c = True
    
if args.l:
    pw_length = genPW(args.l, a, b, c)
else:
    pw_length = genPW(int(22), a, b, c)

random.shuffle(pw_list)

for x in range(0, pw_length):
    password += str(pw_list.pop(0))

if args.c:
    password = password.lower()
if args.C:
    password = password.upper()

print(f"New password is:\n{password}")