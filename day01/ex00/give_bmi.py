def give_bmi(height: list[int | float], weight: list[int | float]) -> list[
        int | float]:
    """
    This function calculates the Body Mass Index (BMI) for each pair of
    height and weight.

    Parameters:
    height (list[int | float]): A list of heights in meters.
    weight (list[int | float]): A list of weights in kilograms.

    Returns:
    list[int | float]: A list of calculated BMIs.
    """
    if len(height) != len(weight):
        exit("Error: height and weight must have the same length.")
    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / (height[i] ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function applies a limit to a list of BMIs and returns a
    list of booleans indicating whether each BMI exceeds the limit.

    Parameters:
    bmi (list[int | float]): A list of BMIs.
    limit (int): The limit to apply.

    Returns:
    list[bool]: A list of booleans indicating whether each BMI
    exceeds the limit.
    """
    limit_bmi = []
    for value in bmi:
        if value > limit:
            limit_bmi.append(True)
        else:
            limit_bmi.append(False)
    return limit_bmi
