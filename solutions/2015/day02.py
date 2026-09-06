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
    total_paper = 0
    for l, w, h in list:
        sides = [l*w, w*h, l*h]
        total_paper += (2 * sum(sides)) + min(sides)
    return total_paper

def ribbon_calc(list):
    ribbon = 0
    for l, w, h in list:
        perimeter = [2*(l+w), 2*(l+h), 2*(w+h)]
        ribbon += l*w*h + min(perimeter)
    return ribbon

amount_paper = paper_calc(parse(s))
amount_ribbon = ribbon_calc(parse(s))

print(f"The elves require {amount_paper} square feet of wrapping paper and {amount_ribbon} !")