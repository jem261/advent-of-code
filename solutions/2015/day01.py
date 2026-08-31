def char_counter(s, char):
    count = 0
    for c in s:
        if c == char:
           count += 1
    return count

with open("inputs/2015/day01.txt") as f:
   s = f.read()

char1 = "("
char2 = ")"

up = (char_counter(s, char1))
down = (char_counter(s, char2))

floor = up - down

print(f"Santa is on floor {floor}!")