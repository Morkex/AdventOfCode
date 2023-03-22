
from collections import Counter

print("Advent of Code 2021 - Day 3")

with open("03\Input.txt") as fh:
    m = [a.strip() for a in fh.readlines()]

# Part 1
# most common element
gamma = "".join([Counter([x[i] for x in m]).most_common(1)[
    0][0] for i in range(len(m[0]))])
# least common element
epsilon = "".join(
    [Counter([x[i] for x in m]).most_common()[-1][0] for i in range(len(m[0]))])
# alternative:
# epsilon = 2**len(m[0])-1 - gamma
print(gamma)
print(epsilon)
#print(f"Power consumption of the submarine: {gamma * epsilon}")
