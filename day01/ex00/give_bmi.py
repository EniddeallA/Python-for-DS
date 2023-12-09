import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) ->\
            list[int | float]:
    """
    This function calculates the Body Mass Index (BMI) for each pair of
    height and weight using numpy arrays.
    """
    height_np = np.array(height)
    weight_np = np.array(weight)
    if height_np.shape != weight_np.shape:
        exit("Error: height and weight must have the same shape.")
    if not all([isinstance(i, int | float) for i in height_np]) or\
        not all([isinstance(i, int | float) for i in weight_np]) or\
            np.any(height_np < 0) or np.any(weight_np < 0):
        exit("Error: Not a valid input.")
    bmi = weight_np / (height_np ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function applies a limit to a list of BMIs and returns a
    list of booleans indicating whether each BMI exceeds the limit.
    """
    limit_bmi = []
    for value in bmi:
        if value > limit:
            limit_bmi.append(True)
        else:
            limit_bmi.append(False)
    return limit_bmi


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
