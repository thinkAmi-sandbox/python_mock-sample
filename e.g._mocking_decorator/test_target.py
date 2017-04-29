from target import Target

class TestCountUpWithoutPatch:
    def test_count_up_decorator(self):
        sut = Target()
        actual = sut.execute_count_up()
        assert actual == 1

    def test_count_down_decorator(self):
        sut = Target()
        actual = sut.execute_count_down()
        assert actual == -1

    def test_add_decorator(self):
        sut = Target()
        actual = sut.execute_add()
        assert actual == 2

    def test_increment_decorator(self):
        sut = Target()
        actual = sut.execute_calculate_increment()
        assert actual == 6

    def test_decrement_decorator(self):
        sut = Target()
        actual = sut.execute_calculate_decrement()
        assert actual == -6