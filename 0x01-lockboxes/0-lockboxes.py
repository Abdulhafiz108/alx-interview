#!/usr/bin/python3
"""This module contains a function on lockbox"""


def canUnlockAll(boxes):
    """
    A function that determines if all lockboxes can be opened
    """
    keynos = list(range(1, len(boxes)))
    keys = []

    for key in boxes[0]:
        keys.append(key)

    while 1:
        cpykeynos = keynos.copy()
        currentkeys = []
        for key in keys:
            if key in keynos:
                keynos.remove(key)
                currentkeys.extend(boxes[key])
            else:
                continue
        keys = currentkeys
        if not keynos:
            break
        if len(keynos) == len(cpykeynos):
            return False

    return True
