with open("inputs/2015/day05.txt") as f:
    strings = f.read().splitlines()

nice_string = 0
naughty_string = 0

for string in strings:
    vowels = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
    double_letter = False
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            double_letter = True
    forbidden = string.count("ab") + string.count("cd") + string.count("pq") + string.count("xy")
    if vowels > 2 and (double_letter == True) and (forbidden == 0):
        nice_string += 1
    else:
        naughty_string += 1

print(f"There are {nice_string} nice strings!")