def parse():   # parsing is turning raw text into structured data
   
   with open("inputs/2015/day02.txt") as f:
      data = f.read().splitlines()

   boxes = []

   for string in data:
      pieces = string.split("x")
      numbers = [int(p) for p in pieces]
      boxes.append(numbers)

   return boxes
    

