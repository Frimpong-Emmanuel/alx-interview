#!/usr/bin/python3
"""
Method to determine if all boxes can be opened 
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for key in range(1, len(boxes) -1):
        ctr = False
        for idx in range(len(boxes)):
            ctr = (key in boxes[idx] and key != idx)
            if ctr:
                break
        if ctr is False:
            return ctr
    return True


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))


boxes = [[1, 4, 6],[2], [0, 4, 1],  [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))


boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
