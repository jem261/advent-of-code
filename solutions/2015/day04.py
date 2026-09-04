import hashlib

with open("inputs/2015/day04.txt") as f:
    s = f.read()

ans = ""
n = 1

while ans[:5] != "00000":
    text = s + str(n)
    ans = hashlib.md5(text.encode()).hexdigest()
    n += 1

print(n-1)
