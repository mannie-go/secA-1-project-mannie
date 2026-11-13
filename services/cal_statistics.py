import numpy as np


def parse_numbers(text):
    # "1, 2, 3" or "1 2 3" -> [1.0, 2.0, 3.0]
    numbers = []
    for item in text.replace(",", " ").split():
        try:
            value = float(item)
        except ValueError:
            raise ValueError(f"'{item}' is not a number")
        if not np.isfinite(value) or abs(value) > 1e15:
            raise ValueError(f"'{item}' is not a valid number")
        numbers.append(value)

    if len(numbers) == 0:
        raise ValueError("Please enter at least one number")
    return numbers


def cal_mean(data):
    return np.mean(data)


def cal_median(data):
    return np.median(data)


def cal_variance(data):
    return np.var(data)


def cal_sd(data):
    return np.std(data)
