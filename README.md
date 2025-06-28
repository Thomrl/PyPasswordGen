# PyPasswordGen
A nice little password generator written in python.

-h = help.

-l = specify length of the generated password. `-l 30` for 30 character.

-o = enable letters, numbers and symbols. 1 = letters, 2 = numbers, 3 = symbols. `-o 12` for letters and numbers. `-o 31` for letters and symbols. The order does not matter.

-c = make all letters lowercase.

-C = make all letters uppercase.

`pwgen.py -l 20 -o 12 -c` will make a 20 character long password with numbers and lowercase letters.
