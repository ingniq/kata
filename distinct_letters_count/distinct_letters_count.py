def solution(s: str) -> int:
    if type(s) is not str:
        raise TypeError("The argument must be a string.")

    if len(s) > 300000:
        raise ValueError("The length of the string should not exceed 300 000 characters.")

    from collections import Counter

    chars_counter = Counter(s)
    result = 0
    _ = {}

    for count in chars_counter.values():
        try:
            while count > 0 and _[count]:
                count -= 1
                result += 1
        except KeyError:
            _[count] = True

    return result
