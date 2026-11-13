import numpy as np


def cal_mode(data):
    # Each unique value and how many times it appears
    values, counts = np.unique(data, return_counts=True)

    # Every value appears once -> no mode
    if counts.max() == 1:
        return []

    # Return every value with the highest count
    return values[counts == counts.max()].tolist()
