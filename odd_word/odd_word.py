def solution(n: int) -> str:
    if type(n) is not int:
        raise TypeError("The argument must be an integer.")

    if n < 1 or n > 200000:
        raise ValueError("The number must belong to the range from 1 to 200 000.")

    # import string
    # counter = {char: 0 for char in string.ascii_lowercase}

    return ""