def part1():
  left, right = [], []
  
  with open("./input.txt", "r") as f:
    for line in f:
      l1, l2 = map(int, line.strip().split())
      left.append(l1)
      right.append(l2)
  
  left.sort()
  right.sort()
  
  total_distance = sum([abs(left[i] - right[i]) for i in range(len(left))])
  print(total_distance)


def part2():
  left, right = [], []
  
  with open("./input.txt", "r") as f:
    for line in f:
      l1, l2 = map(int, line.strip().split())
      left.append(l1)
      right.append(l2)
  
  coord_appearances = {i: 0 for i in left}
  
  for i in right:
    keys = coord_appearances.keys()
    if i in keys:
      coord_appearances[i] += 1
  
  total = sum([i * coord_appearances[i] for i in coord_appearances])
  print(total)

part1()
part2()
