from pytest import raises
from odd_word import solution


class TestClass:
    def __check_string(self, value: str) -> bool:
        counter = {}

        for char in value:
            try:
                counter[char] += 1
            except KeyError:
                counter[char] = 1

        return bool(counter) and not bool({k: v for k, v in counter.items() if v % 2 == 0})

    def test_argument_validation(self):
        with raises(TypeError):
            solution("3")

        with raises(ValueError):
            solution(-1)

        with raises(ValueError):
            solution(0)

        with raises(ValueError):
            solution(200001)

    def test_result(self):
        # test string length
        assert len(solution(1)) == 1
        assert len(solution(50)) == 50
        assert len(solution(200000)) == 200000

        # test string
        assert self.__check_string(solution(4)) is True
