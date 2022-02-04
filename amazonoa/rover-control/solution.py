from typing import List

def roverPosition(n: int, commands: List[str]) -> int:
    endBound = n - 1
    currentX = 0
    currentY = 0
    for i in commands:
        if (i in ['RIGHT', 'LEFT']):
            m = -1 if i == 'LEFT' else 1
            newX = currentX + m
            if 0 <= newX and newX <= endBound:
                currentX = newX
        else:
            m = -1 if i == 'UP' else 1
            newY = currentY + m
            if 0 <= newY and newY <= endBound:
                currentY = newY
    return currentY * n + currentX
