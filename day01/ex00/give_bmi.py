def give_bmi(height: list[int | float], weight: list[int | float]) -> list[
        int | float]:
    if len(height) != len(weight):
        exit("Error: height and weight must have the same length.")
    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / (height[i] ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    limit_bmi = []
    for value in bmi:
        if value > limit:
            limit_bmi.append(True)
        else:
            limit_bmi.append(False)
    return limit_bmi