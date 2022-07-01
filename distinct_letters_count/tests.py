import pytest
from distinct_letters_count import solution


class TestClass:
    def test_argument_validation(self):
        with pytest.raises(TypeError):
            solution(123)

        with pytest.raises(ValueError):
            import string
            import random

            solution("".join(random.choice(string.ascii_lowercase + " ") for _ in range(300001)))

    def test_result(self):
        assert solution("aaaabbbb") == 1
        assert solution("ccaaffddecee") == 6
        assert solution("eeee") == 0
        assert solution("") == 0
        assert solution("example") == 4
