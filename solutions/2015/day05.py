with open("inputs/2015/day05.txt") as f:
    strings = f.read().splitlines()

nice_string1 = 0
naughty_string1 = 0

for string in strings:
    vowels = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
    double_letter = False
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            double_letter = True
    forbidden = string.count("ab") + string.count("cd") + string.count("pq") + string.count("xy")
    if vowels > 2 and (double_letter == True) and (forbidden == 0):
        nice_string1 += 1
    else:
        naughty_string1 += 1

print(f"There are {nice_string1} nice strings!")

nice_string2 = 0
naughty_string2 = 0

for string in strings:
    pair_without_overlap = False
    for i in range(len(string)-1):
        if string[i:i+2] in string[i+2:]:
            pair_without_overlap = True
    repeat_letter = False
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            repeat_letter = True
    if (repeat_letter == True) and (pair_without_overlap == True):
        nice_string2 += 1
    else:
        naughty_string2 += 1

print(f"There are {nice_string2} nice strings!")