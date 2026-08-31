def parse():   # parsing is turning raw text into structured data
   
   with open("inputs/2015/day02.txt") as f:
      data = f.read().splitlines()

   list = []
   for line in data:
      list.append(line.split("x"))

   for p in list:
      p = int(p) 
    

