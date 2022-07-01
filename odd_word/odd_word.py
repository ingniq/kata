def solution(n: int) -> str:
    if type(n) is not int:
        raise TypeError("The argument must be an integer.")

    if n < 1 or n > 200000:
        raise ValueError("The number must belong to the range from 1 to 200 000.")

    import string
    import random

    result = ""
    char_counter = {}
    all_chars_count = 0

    # when generating a string, we will immediately provide the necessary conditions
    while all_chars_count < n:
        limit = n - all_chars_count
        char = random.choice(string.ascii_lowercase)
        char_count = random.randrange(1, limit) if limit > 1 else 1

        try:
            current_char_count = char_counter[char]
        except KeyError:
            char_counter[char] = 0
            current_char_count = 0

            # a guarantee that it will be odd
            if char_count % 2 == 0:
                char_count -= 1

        # a guarantee that it will be odd
        if char_count % 2 != 0 and current_char_count != 0:
            char_count -= 1

        # skip
        if char_count == 0:
            continue

        # a guarantee that it will be odd
        if limit == 1 and current_char_count != 0:
            continue

        result += char * char_count
        char_counter[char] += char_count
        all_chars_count += char_count

    return result
