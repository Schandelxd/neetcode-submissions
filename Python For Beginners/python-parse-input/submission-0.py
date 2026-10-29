from typing import List

def read_integers() -> List[int]:
    lol = input()
    xd = lol.split(",")
    return [int(x) for x in xd]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())