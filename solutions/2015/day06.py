import re

with open("inputs/2015/day06.txt") as f:
    strings = f.read().splitlines()

lights_on = 0
grid1 = [[False] * 1000 for _ in range(1000)]

for string in strings:
    data = re.findall(r"\d+", string)
    nums = [int(p) for p in data]
    if string.startswith("toggle"):
        for i in range(nums[1], nums[3]+1):
            for j in range(nums[0], nums[2]+1):
                grid1[i][j] = not grid1[i][j]
    elif string.startswith("turn on"):
        for i in range(nums[1], nums[3]+1):
            for j in range(nums[0], nums[2]+1):
                grid1[i][j] = True
    elif string.startswith("turn off"):
        for i in range(nums[1], nums[3]+1):
            for j in range(nums[0], nums[2]+1):
                grid1[i][j] = False
    
for i in range(1000):
    lights_on += sum(grid1[i])

print(f"There are {lights_on} lights on!")

brightness = 0
grid2 = [[0] * 1000 for _ in range(1000)]

for string in strings:
    data = re.findall(r"\d+", string)
    nums = [int(p) for p in data]
    if string.startswith("toggle"):
        for i in range(nums[1], nums[3]+1):
            for j in range(nums[0], nums[2]+1):
                grid2[i][j] += 2
    elif string.startswith("turn on"):
        for i in range(nums[1], nums[3]+1):
            for j in range(nums[0], nums[2]+1):
                grid2[i][j] += 1
    elif string.startswith("turn off"):
        for i in range(nums[1], nums[3]+1):
            for j in range(nums[0], nums[2]+1):
                if grid2[i][j] == 0:
                    pass
                elif grid2[i][j] > 0:
                    grid2[i][j] -= 1

for i in range(1000):
    brightness += sum(grid2[i])

print(f"The total brightness is {brightness}!")
