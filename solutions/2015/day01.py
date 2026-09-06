def char_counter(s, char):
    count = 0
    for c in s:
        if c == char:
           count += 1
    return count

with open("inputs/2015/day01.txt") as f:
   s = f.read().strip()

char1 = "("
char2 = ")"

up = char_counter(s, char1)
down = char_counter(s, char2)

floor_s = up - down
floor_d = 0
position = 0

for ch in s:
    if floor_d != -1:
        position += 1
        if ch == "(":
            floor_d += 1
        elif ch == ")":
            floor_d -= 1
    elif floor_d == -1:
        break

print(f"Santa is on floor {floor_s}! He reached the basement on position number {position}")