import script2_calc

class TestSum:
    def Test_sum_5_5(self):
        assert script2_calc.sum(5,5) == 10
    def Test_diff_5_5(self):
        assert script2_calc.diff(5,5) == 0
    def Test_multi_5_5(self):
        assert script2_calc.multi(5,5) == 25
    def Test_division_5_5(self):
        assert script2_calc.division(5,5) == 1

