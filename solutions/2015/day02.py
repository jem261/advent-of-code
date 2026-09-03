def parse(input):
    data = input.splitlines()
    boxes = []
    for string in data:
       pieces = string.split("x")
       numbers = [int(p) for p in pieces]
       boxes.append(numbers)
    return boxes

with open("inputs/2015/day02.txt") as f:
    s = f.read()

def paper_calc(list):
    total = 0
    for l, w, h in list:
        sides = [l*w, w*h, l*h]
        total += (2 * sum(sides)) + min(sides)
    return total

amount = paper_calc(parse(s))

print(f"The elves require {amount}m^2 of wrapping paper!")