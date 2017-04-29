from deco.my_decorator import countup, countdown, add, calculate

class Target:
    def __init__(self, value=0):
        self.value = value

    @countup
    def execute_count_up(self):
        return self.value

    @countdown
    def execute_count_down(self):
        return self.value

    @add(2)
    def execute_add(self):
        return self.value

    @calculate(1, 2, 3)
    def execute_calculate_increment(self):
        return self.value

    @calculate(1, 2, 3, is_decrement=True)
    def execute_calculate_decrement(self):
        return self.value


if __name__ == '__main__':
    t = Target()
    print(t.execute_add())
