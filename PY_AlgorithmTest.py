# Joseph Problem
import numpy as np


def safePosition(total, killPosition):
    safeLocations = np.array(range(0,killPosition - 1))
    for i in range(killPosition,total+1):
        safeLocations = (safeLocations + killPosition) % i
    return safeLocations

# Example:
print safePosition(10,6)
