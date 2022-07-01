def solution(s: str) -> int:
    if type(s) is not str:
        raise TypeError("The argument must be a string.")

    if len(s) > 300000:
        raise ValueError("The length of the string should not exceed 300 000 characters.")

    return 0