import hashlib

with open("inputs/2015/day04.txt") as f:
    s = f.read()

ans1 = ""
n = 1

while ans1[:5] != "00000":
    text = s + str(n)
    ans1 = hashlib.md5(text.encode()).hexdigest()
    n += 1

print(n-1)

ans2 = ""
m = 0

while ans2[:6] != "000000":
    text = s + str(m)
    ans2 = hashlib.md5(text.encode()).hexdigest()
    m += 1

print(m-1)
